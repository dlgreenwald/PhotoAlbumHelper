#!/usr/local/bin/python3
from os import environ

from datetime import date, datetime, timedelta
from num2words import num2words
from dotenv import load_dotenv

import swagger_client
from retry import retry
from swagger_client.rest import ApiException
from swagger_client import FormAlbum

def create_in_past_albums():
    # Configure Photoprism_Swagger_Client
    swagger_configuration = swagger_client.Configuration()
    swagger_configuration.api_key =  {"Authorization":environ.get("PHOTOPRISM_API_KEY")}
    swagger_configuration.api_key_prefix = {"Authorization":"Bearer"}
    swagger_configuration.host = environ.get("PHOTOPRISM_URI")

    # create an instance of the API class
    albums_api = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration = swagger_configuration))
    photos_api = swagger_client.PhotosApi(swagger_client.ApiClient(configuration = swagger_configuration))

    def log(message):
        print (f"In The Past: {message}")

    def get_date_range_from_week(p_year,p_week):
        firstdayofweek = datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
        lastdayofweek = firstdayofweek + timedelta(days=6.9)
        return firstdayofweek, lastdayofweek

    def search(query="", scope="", count=100, offset=0, order="newest"):
        data = photos_api.search_photos(count=count, offset=offset, merged=True, order=order, q=query, s=scope, public=True, quality=3)
        return data

    def create_album(title, description="", category=""):
        output = albums_api.create_album(FormAlbum(title=title, favorite=False, description=description, category=category))
        return output

    def find_album_by_title(title):
        albumlist = albums_api.search_albums(1000)
        uid = ""
        for album in albumlist:
            album = album.to_dict()
            if album['title']==title:
                uid = album['uid']
        return uid

    def remove_photos_from_album_by_uid(album_uid, count=100000):
        photos_in_album = []
        photos = search(scope=album_uid, count=count)
        for photo in photos:
            photos_in_album.append(photo.uid)
        albums_api.remove_photos_from_album(uid=album_uid, photos={"photos":photos_in_album})

    @retry(exceptions=ApiException)
    def manage_album(query_string, title, count=100):

        photos_in_album = []
        photos = search(query=query_string, count=count)
        for photo in photos:
            photos_in_album.append(photo.uid)

        if len(photos_in_album) > 0 :
            album_uid = find_album_by_title(title)
            if album_uid:
                log(f"'{title}` already exists, clearing photos")
                if environ.get('TRIALRUN')=="False":
                    remove_photos_from_album_by_uid(album_uid)
            else:
                log(f"Creating Album `{title}`")
                if environ.get('TRIALRUN')=="False":
                    body = create_album(title, category="In The Past")
                    album_uid = body.uid
                    # update_album(uid, title, category="In The Past")

            if environ.get('TRIALRUN')=="False":
                albums_api.add_photos_to_album(uid=album_uid, photos={"photos":photos_in_album})
                log(f"Album `{title}` photos inserted")

        else:
            album_uid = find_album_by_title(title)
            if album_uid:
                log(f"'{title}` already exists and is empty, Deleting")
                if environ.get('TRIALRUN')=="False":
                    albums_api.delete_album(album_uid)


    if environ.get('TRIALRUN')=="False":
        log( "TRIALRUN is False, commiting changes")
    else:
        log( "TRIALRUN is True, no changes will be commited")

    #get the oldest photo in library
    oldest_year = 0
    photos = search(query="original:*", count=1, order="oldest")
    if len(photos) == 1:
        oldest_year = photos[0].year

    current_year, week_num, _ = date.today().isocalendar()
    log("Week #" + str(week_num))

    #Create all the previous year albums
    current_year, week_num, _ = date.today().isocalendar()
    for year in range(oldest_year, current_year):
        firstdate, lastdate = get_date_range_from_week(year, week_num)
        year_diff = current_year-year
        yearstring = "Years" if year_diff>1 else "Year"
        title = f"{num2words(year_diff).capitalize()} {yearstring} Ago This Week"
        log(f"{title}: Week #{week_num}")
        query_string = f"after:\"{firstdate}\" before:\"{lastdate}\""
        manage_album(query_string=query_string, title=title)

    # Create Last Month Album
    current_year, week_num, _ = date.today().isocalendar()
    last_month = week_num-4
    if last_month < 0:
        last_month = last_month+52
        current_year = current_year-1
    firstdate, lastdate = get_date_range_from_week(current_year, last_month)
    # @TODO Need to handle negitive weeks
    log(f"One Month Ago: Week #{last_month}".format(last_month))
    query_string = f"after:\"{firstdate}\" before:\"{lastdate}\""
    manage_album(query_string=query_string, title="One Month Ago This Week")

    # Create Last Week Album
    current_year, week_num, _ = date.today().isocalendar()
    last_week = week_num-1
    if last_week < 0:
        last_week = last_week+52
        current_year = current_year-1
    firstdate, lastdate = get_date_range_from_week(current_year, last_week)
    log(f"One Week Ago: Week #{last_week}:{firstdate} through {lastdate}")
    query_string = f"after:\"{firstdate}\" before:\"{lastdate}\""
    manage_album(query_string=query_string, title="Last Week")

    log("Done")

if __name__=="__main__":
    load_dotenv()
    create_in_past_albums()
