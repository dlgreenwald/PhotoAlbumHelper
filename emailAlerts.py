from pathlib import Path
from chameleon import PageTemplateLoader
import datetime as dt  
from dotenv import load_dotenv
from os import environ
from photoprism.Session import Session
from photoprism.Photo import Photo
from lib.photocollage.UserCollage import UserCollage, Options
import lib.photocollage.render as render
from PIL import Image
import random
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def emailAlert():
    def log(message):
        print ("Email Events: {0}".format(message))

    load_dotenv()
    if environ.get('TRIALRUN')=="False":
        log( "TRIALRUN is False, commiting changes")
    else:
        log( "TRIALRUN is True, no changes will be commited")

    if not os.path.exists(environ.get('FILEPATH')):
        os.makedirs(environ.get('FILEPATH'))
    
    workingDir = "{0}/{1}-{2}".format(environ.get('FILEPATH') ,dt.date.today().isocalendar().week, dt.date.today().isocalendar().year)
    if not os.path.exists(workingDir):
        os.makedirs(workingDir)
    

    pp_session = Session(environ.get('USER'), environ.get('PASS'), environ.get('DOMAIN'), use_https=True)
    pp_session.create()
    p = Photo(pp_session)

    week_num = dt.date.today().isocalendar().week-1
    log("WeekNum = {0}".format(week_num))

    def search(query, count=100, offset=0, order="newest"):
        _, data = pp_session.req(f"/photos?count={count}&offset={offset}&merged=true&country=&camera=0&lens=0&label=&year=0&month=0&color=&order={order}&q={query}&public=true&quality=3", "GET")
        return data

    def getAlbumsFromThisWeekInPast():
        matchedAlbums = []
        albumlist = p.list_albums()
        uid = ""
        for album in albumlist:
            if album['Type']=="album":
                photos = search(query="type:image|live album:\"{0}\"".format(album['UID']), count=1, offset=0,  order="newest")
                # format 2023-08-15T22:17:34Z
                date = dt.datetime.strptime(photos[0]['TakenAt'], '%Y-%m-%dT%H:%M:%SZ')
                album["startDate"] = date
                enddate = dt.datetime.strptime(photos[-1]['TakenAt'], '%Y-%m-%dT%H:%M:%SZ')
                album["endDate"] = enddate
                if date.isocalendar().week==week_num:
                    log("Candidate Album: {0} Date:{1} Week:{2}".format(album['Title'], date, date.isocalendar().week))
                    matchedAlbums.append(album)
        return matchedAlbums
    
    def sortAlbumsByPriority(albums):
        for album in albums:
            score = 0
            match album['Category']:
                case "In the Past":
                    score = album['PhotoCount']/7
                case "Generated Event":
                    score = album['PhotoCount']*2
                case _:
                    score = album['PhotoCount']*3
            album['score'] = score
        albums.sort(key= lambda x: x['score'], reverse=True)
        return albums
    
    def downloadPhotosFromList(selection):
        filelist= []
        for photos in selection:
            try:
                p.download_file(photos["Hash"], path=workingDir, filename=photos["UID"])
            except:
                continue

            filename = ""
            if os.path.exists("{0}/{1}.{2}".format(workingDir, photos["UID"], "jpg")):
                filename = photos["UID"]+".jpg"
            elif os.path.exists("{0}/{1}.{2}".format(workingDir, photos["UID"], "png")):
                filename = photos["UID"]+".png"
            else:
                continue
            filelist.append("{0}/{1}".format(workingDir,filename))
        return filelist
    
    def deleteFilesFromList(filelist):
        for filename in filelist:
            try:
                os.remove(filename)
            except:
                print("Error deleting file: {0}".format(filename))


    def downloadRandomPhotosFromAlbum(album):
        data = search(query="type:image|live album:\"{0}\"".format(album['UID']), count=100, offset=0,  order="newest")

        size = 0
        if len(data)<10:
            size = len(data)
        else:
            size = random.sample( [3,4,5,5,6,6,6,7,7,7,8,8,9,10] , 1)[0]
            
        selection = random.sample(data, size)
        pairselection = random.sample(data, 2)

        filelist= downloadPhotosFromList(selection)
        pair= downloadPhotosFromList(pairselection)

        return filelist, pair

    def generateCollageForAlbum(title, uid, filelist, size_x, size_y):
        photolist = render.build_photolist(filelist)

        options = Options()
        options.out_w = size_x
        options.out_h = size_y
        options.border_c = "white"

        new_collage = UserCollage(photolist)
        new_collage.make_page(options)
        new_collage.page.target_ratio = 1.0 * options.out_h / options.out_w
        new_collage.page.adjust_cols_heights()
        enlargement = float(options.out_w) / new_collage.page.w
        new_collage.page.scale(enlargement)

        def on_update(img, fraction_complete):
            return

        def on_complete(img):
            log("Rendering Complete")

        def on_failure(e):
            log(e)

        log("Rendering Collage for {0}".format(title))
        t = render.RenderingTask(
            new_collage.page, 
            quality=render.QUALITY_BEST,
            output_file="{3}/{0}-{1}x{2}.jpg".format(uid, size_x, size_y, workingDir),
            border_width=options.border_w * max(new_collage.page.w, new_collage.page.h),
            border_color=options.border_c,
            on_update=on_update,
            on_complete=on_complete,
            on_fail=on_failure
            )
        t.run()

        return "{0}-{1}x{2}.jpg".format(uid, size_x, size_y)

    def renderHTML(leader, uri, title, events):
        templates_path = Path(__file__).resolve().parent / "templates"
        template_loader = PageTemplateLoader(
            str(templates_path),
            ".html",
        )

        template = template_loader["index"]

        with open("{0}/{1}-{2}/email-{1}-{2}.html".format(environ.get('FILEPATH') ,dt.date.today().isocalendar().week, dt.date.today().isocalendar().year), "w", encoding="utf-8") as text_file:
            text_file.write(template(leader=leader, mainuri=uri, title=title, events=events))
        return template(leader=leader, mainuri=uri, title=title, events=events)

    def send_email(subject, html, text, sender, recipients, password):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Message sent!")

    candidates = getAlbumsFromThisWeekInPast()
    scoredCandidate = sortAlbumsByPriority(candidates)


    renderData = [] # [ bannerPhoto:bannerphoto  ["title": title, "date":date, "mainPhoto":mainphoto, "secondaryPhoto":secondaryphoto]]
    allFiles = []
    for candidate in scoredCandidate:
        filelist, pair = downloadRandomPhotosFromAlbum(candidate)
        allFiles = allFiles + filelist
        allFiles = allFiles + pair

        record = dict()
        record["mainphoto"] = "{0}/{1}-{2}/{3}".format(environ.get('URIPREFIX'), dt.date.today().isocalendar().week, dt.date.today().isocalendar().year, generateCollageForAlbum(candidate["Title"], candidate["UID"], filelist, 640, 853))
        record["secondaryphoto"] = "{0}/{1}-{2}/{3}".format(environ.get('URIPREFIX'), dt.date.today().isocalendar().week, dt.date.today().isocalendar().year, generateCollageForAlbum(candidate["Title"], candidate["UID"], pair, 405, 188))
        record["title"] = candidate["Title"]
        record["uri"] = "{0}/library/albums/{1}/view".format(environ.get('PHOTOPRISMURI'), candidate["UID"])
        record["dateString"] = "{0} - {1}".format(candidate["startDate"], candidate["endDate"])
        renderData.append(record)

    size = random.sample( [3,4,5,5,6,6,6,7,7,7,8,8,9,10] , 1)[0]
    selection = random.sample(allFiles, size)
    bannerTitle = "Banner-{0}-{1}".format(dt.date.today().isocalendar().week, dt.date.today().isocalendar().year)
    bannerFile = generateCollageForAlbum(bannerTitle, bannerTitle, selection, 600, 750)

    background = Image.open("{0}/{1}".format(workingDir, bannerFile))
    foreground = Image.open("Overlay.png")
    background.paste(foreground, (0, 0), foreground)
    background.save("{0}/{1}-final.jpg".format(workingDir, bannerFile))

    body = renderHTML("{0}/{1}-{2}/{3}-final.jpg".format(environ.get('URIPREFIX'), dt.date.today().isocalendar().week, dt.date.today().isocalendar().year, bannerFile), environ.get('PHOTOPRISMURI'),  "This Week in the Past", renderData)
    subject = "This Week in the Past"
    sender = environ.get('SENDER')
    recipients = environ.get('RECIPIENTS').split(",")
    log(recipients)
    smtppass = environ.get('SMTPPASS')
    if environ.get('TRIALRUN')=="False":
        send_email(subject, body, "fixme", sender, recipients, smtppass)

    deleteFilesFromList(allFiles)

# Steps
# Determine albums to highlight
    # find Generated Albums from this week in the past
    # score
        # Self Created Album 3 * number of photos
        # Generated Album 2 * number of photos
        # Week in Past Always Last Sort by number of photos
# Generate Sub collage for each album
# Generate Photo pair for each album
# Generate Main collage
    # Add text to image
# Save to configured path so static webserver can host images
# Generate html with links to photos (including titles)
# Send email

if __name__=="__main__":
    emailAlert()