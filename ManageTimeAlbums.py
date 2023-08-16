#!/usr/local/bin/python3
from photoprism.Session import Session
from photoprism.Photo import Photo
from datetime import date
from datetime import datetime
from datetime import timedelta
from num2words import num2words
from os import environ
from dotenv import load_dotenv

def createInPastAlbums():
    load_dotenv()

    def log(message):
        print ("In The Past: {0}".format(message))

    def getDateRangeFromWeek(p_year,p_week):

        firstdayofweek = datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
        lastdayofweek = firstdayofweek + timedelta(days=6.9)
        return firstdayofweek, lastdayofweek


    def update_album(uid, title, category):
        data = {"Title":title,"Favorite":False, "Category":category}
        status_code, output = pp_session.req(f"/albums/{uid}", "PUT", data=data)

        if status_code == 200:
            return output
        
        return False

    def create_album(title, description="", category=""):
        data = {"Title":title,"Favorite":False, "Notes": description, "Category":category}
        status_code, output = pp_session.req("/albums", "POST", data=data)

        if status_code == 200:
            return output
        
        return False

    def ManageAlbum(session, queryString, title, count=100):
        p = Photo(session)
        if p.check_if_album_exists(title):
            log("'{0}` already exists, clearing photos".format(title))
            if environ.get('TRIALRUN')=="False":
                p.remove_photos_from_album(albumname=title)
        else:
            log("Creating Album `{0}`".format(title))
            if environ.get('TRIALRUN')=="False":
                body = create_album(title, category="In The Past")
                uid = body['UID']
                update_album(uid, title, category="In The Past")
        #Unlike all the other places where if TRIAL run is False we want to perform an action, 
        #in this case the second half of the if statement should only be run if trial run isnt' true. 
        #The OR should result in p.add... only being run if TRIALRUN is False
        if environ.get('TRIALRUN')=="True" or p.add_to_album_from_query(query=queryString, albumname=title, count=count):
            log("Album `{0}` photos inserted".format(title))
            return True
        else:
            #cleanup if photos can't be inserted....usually becuase there are no photos, so we won't have a album for this week.
            log("Album `{0}` photos failed to insert.  Deleteing Album.".format(title))
            if environ.get('TRIALRUN')=="False":
                p.remove_album(albumname=title)
            return False

    if environ.get('TRIALRUN')=="False":
        log( "TRIALRUN is False, commiting changes")
    else:
        log( "TRIALRUN is True, no changes will be commited")

    pp_session = Session(environ.get('USER'), environ.get('PASS'), environ.get('DOMAIN'), use_https=True)
    pp_session.create()

    #get the oldest photo in library
    p = Photo(pp_session)
    OldestYear = 0
    photos = p.search(query="original:*", count=1,  order="oldest")
    if len(photos) == 1:
        OldestYear = photos[0]["Year"]


    # Create Last Week Album
    CurrentYear, week_num, day_of_week = date.today().isocalendar()
    print("Week #" + str(week_num))
    last_week = week_num-1
    if last_week < 0:
        last_week = last_week+52
        CurrentYear = CurrentYear-1
    firstdate, lastdate = getDateRangeFromWeek(CurrentYear, last_week)
    log("One Week Ago: Week #{0}:{1} through {2}".format(last_week, firstdate, lastdate))
    queryString = "after:\"{0}\" before:\"{1}\"".format(firstdate, lastdate)
    ManageAlbum(session=pp_session, queryString=queryString, title="Last Week")

    # Create Last Month Album
    CurrentYear, week_num, day_of_week = date.today().isocalendar()
    last_month = week_num-4
    if last_month < 0:
        last_month = last_month+52
        CurrentYear = CurrentYear-1
    firstdate, lastdate = getDateRangeFromWeek(CurrentYear, last_month)
    # @TODO Need to handle negitive weeks
    log("One Month Ago: Week #{0}".format(last_month))
    queryString = "after:\"{0}\" before:\"{1}\"".format(firstdate, lastdate)
    ManageAlbum(session=pp_session, queryString=queryString, title="One Month Ago This Week")

    #Create all the previous year albums
    for year in range(OldestYear, CurrentYear):
        firstdate, lastdate = getDateRangeFromWeek(year, week_num)
        YearDiff = CurrentYear-year
        yearstring = "Years" if YearDiff>1 else "Year"
        title = "{0} {1} Ago This Week".format(num2words(YearDiff).capitalize(), yearstring)
        log("{1}: Week #{0}".format(week_num, title))
        queryString = "after:\"{0}\" before:\"{1}\"".format(firstdate, lastdate)
        ManageAlbum(session=pp_session, queryString=queryString, title=title)

    log("Done")

if __name__=="__main__":
    createInPastAlbums()