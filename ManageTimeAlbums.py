#!/usr/local/bin/python3
from datetime import date
from datetime import datetime
from datetime import timedelta
from num2words import num2words
from os import environ
from dotenv import load_dotenv

import swagger_client
from swagger_client.rest import ApiException
from swagger_client import FormAlbum, FormPhoto

from pprint import pprint

def createInPastAlbums():
    # Configure Photoprism_Swagger_Client
    swagger_configuration = swagger_client.Configuration()
    swagger_configuration.api_key =  {"Authorization":environ.get("PHOTOPRISM_API_KEY")}
    swagger_configuration.api_key_prefix = {"Authorization":"Bearer"}
    swagger_configuration.host = environ.get("PHOTOPRISM_URI")

    # create an instance of the API class
    albums_api = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration = swagger_configuration))
    photos_api = swagger_client.PhotosApi(swagger_client.ApiClient(configuration = swagger_configuration))

    def log(message):
        print ("In The Past: {0}".format(message))

    def getDateRangeFromWeek(p_year,p_week):

        firstdayofweek = datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
        lastdayofweek = firstdayofweek + timedelta(days=6.9)
        return firstdayofweek, lastdayofweek

    def search(query="", scope="", count=100, offset=0, order="newest"):
        data = photos_api.search_photos(count=count, offset=offset, merged=True, order=order, q=query, s=scope, public=True, quality=3)
        return data

    def create_album(title, description="", category=""):
        try:
            output = albums_api.create_album(FormAlbum(title=title, favorite=False, description=description, category=category))
            return output
        except:
            return False

    def update_album(uid, title, category):
        try:
            output = albums_api.update_album(uid=uid, album=FormAlbum(title=title, favorite=False, category=category))
            return output
        except:
            return False
        
    def find_album_by_title(title):
        albumlist = albums_api.search_albums(1000)
        uid = ""
        for album in albumlist:
            album = album.to_dict()
            if album['title']==title:
                uid = album['uid']
        return uid
    
    def remove_photos_from_album_by_uid(album_uid, count=1000000):
        try:
            photos_in_album = []
            if photos == False:
                photos = search(scope=album_uid, count=count)
                for photo in photos:
                    photos_in_album.append(photo.uid)
            albums_api.remove_photos_from_album(uid=album_uid, photos={"photos":photos_in_album})
            return True
        except:
            return False
        
    def add_to_album_from_query(query, album_uid, count=1000000):
        photos_in_album = []
        photos = search(query=query, count=count)
        for photo in photos:
            photos_in_album.append(photo.uid)


        result = albums_api.add_photos_to_album(uid=album_uid, photos={"photos":photos_in_album})
        return result

    def ManageAlbum(queryString, title, count=100):
        album_uid = find_album_by_title(title)
        if album_uid:
            log("'{0}` already exists, clearing photos".format(title))
            if environ.get('TRIALRUN')=="False":
                remove_photos_from_album_by_uid(album_uid)
        else:
            log("Creating Album `{0}`".format(title))
            if environ.get('TRIALRUN')=="False":
                body = create_album(title, category="In The Past")
                uid = body['UID']
                update_album(uid, title, category="In The Past")
        #Unlike all the other places where if TRIAL run is False we want to perform an action, 
        #in this case the second half of the if statement should only be run if trial run isnt' true. 
        #The OR should result in p.add... only being run if TRIALRUN is False
        if environ.get('TRIALRUN')=="True" or add_to_album_from_query(query=queryString, album_uid=album_uid, count=count):
            log("Album `{0}` photos inserted".format(title))
            return True
        else:
            #cleanup if photos can't be inserted....usually becuase there are no photos, so we won't have a album for this week.
            log("Album `{0}` photos failed to insert.  Deleteing Album.".format(title))
            if environ.get('TRIALRUN')=="False":
                albums_api.delete_album(album_uid)
            return False

    if environ.get('TRIALRUN')=="False":
        log( "TRIALRUN is False, commiting changes")
    else:
        log( "TRIALRUN is True, no changes will be commited")

    #get the oldest photo in library
    OldestYear = 0
    photos = search(query="original:*", count=1, order="oldest")
    if len(photos) == 1:
        OldestYear = photos[0].year

    #Create all the previous year albums
    for year in range(OldestYear, CurrentYear):
        firstdate, lastdate = getDateRangeFromWeek(year, week_num)
        YearDiff = CurrentYear-year
        yearstring = "Years" if YearDiff>1 else "Year"
        title = "{0} {1} Ago This Week".format(num2words(YearDiff).capitalize(), yearstring)
        log("{1}: Week #{0}".format(week_num, title))
        queryString = "after:\"{0}\" before:\"{1}\"".format(firstdate, lastdate)
        ManageAlbum(queryString=queryString, title=title)

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
    ManageAlbum(queryString=queryString, title="One Month Ago This Week")

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
    ManageAlbum(queryString=queryString, title="Last Week")

    log("Done")

if __name__=="__main__":
    load_dotenv()
    createInPastAlbums()