#!/usr/local/bin/python3
import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, USLaborDay, USMemorialDay, USThanksgivingDay
from pandas.tseries.offsets import Easter
from pandas import DateOffset
from os import environ
from dotenv import load_dotenv
import hashlib
import datetime as dt  
import json
from dateutil.relativedelta import (
    FR,
    MO,
    SA,
    SU,
    TH,
    TU,
    WE,
)

import swagger_client
from swagger_client.rest import ApiException
from swagger_client import FormAlbum, FormPhoto

class FamilyCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday("New Year's Day", month=1, day=1),
        USMemorialDay,
        Holiday("Independence Day", month=7, day=4),
        USLaborDay,
        USThanksgivingDay,
        Holiday("Christmas Day", month=12, day=25),
        Holiday("Easter", month=1, day=1, offset=[Easter()]),
        Holiday("Valentine's Day", month=2, day=14),
        Holiday("Halloween", month=10, day=31 ),
        Holiday("St. Patrick's Day", month=3, day=17 ),
        Holiday("Mother's Day", month=5, day=1, offset=DateOffset(weekday=SU(2))),
        Holiday("Father's Day", month=6, day=1, offset=DateOffset(weekday=SU(3))),
    ]

weekphrase = "A Week in {0} {1} {2}"
shorttripphrase = "A short trip to {0} {1} {2}"
daytripphrase = "A day in {0} {1} {2} {3}"
holidayphrase = "{0} in {1} {2}"

def detectAndCreateEvents():
    def log(message):
        print ("Timeline Events: {0}".format(message))

    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    load_dotenv()
    if environ.get('TRIALRUN')=="False":
        log( "TRIALRUN is False, commiting changes")
    else:
        log( "TRIALRUN is True, no changes will be commited")

    # Configure Photoprism_Swagger_Client
    swagger_configuration = swagger_client.Configuration()
    swagger_configuration.api_key =  {"Authorization":environ.get("PHOTOPRISM_API_KEY")}
    swagger_configuration.api_key_prefix = {"Authorization":"Bearer"}
    swagger_configuration.host = environ.get("PHOTOPRISM_URI")

    # create an instance of the API class
    albums_api = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration = swagger_configuration))
    photos_api = swagger_client.PhotosApi(swagger_client.ApiClient(configuration = swagger_configuration))

    def search(query="", scope="", count=100, offset=0, order="newest"):
        data = photos_api.search_photos(count=count, offset=offset, merged=True, order=order, q=query, s=scope, public=True, quality=3)
        return data
    
    def create_album(title, jsonData:dict, category):
        try:
            output = albums_api.create_album(FormAlbum(title=title, favorite=False, notes=json.dumps(jsonData), category=category))
            return output
        except:
            return False

    def update_album(uid, title, jsonData:dict, category):
        try:
            output = albums_api.update_album(uid=uid, album=FormAlbum(title=title, favorite=False, notes=json.dumps(jsonData), category=category))
            return output
        except:
            return False
        
    def updateOrCreateAlbumByHash(name, jsonData:dict, category):
        albumlist = albums_api.search_albums(1000, q=name)
        uid = ""
        for album in albumlist:
            album = album.to_dict()
            if album['notes'] != "" and json.loads(album['notes'])['Hash']==jsonData['Hash']:
                uid = album['uid']
        if uid == "":
            body = create_album(name, jsonData, category)
            uid = body['uid']
            update_album(uid, name, jsonData, category) # why did I do this?!
        return uid

    def find_album_by_note(note):
        albumlist = albums_api.search_albums(1000)
        uid = ""
        for album in albumlist:
            album = album.to_dict()
            if album['notes']==note:
                uid = album['uid']
        return uid

    # iterate across all albums, looking at hidden notes field for metadata about the album date string
    def find_most_recent_album_date_in_category(category):
        albumlist = albums_api.search_albums(1000)
        uid = ""
        recentDate = dt.datetime.strptime("1900-01-01T00:00:00Z", '%Y-%m-%dT%H:%M:%SZ')
        for album in albumlist:
            album = album.to_dict()
            if album['category']==category:
                jsonData = json.loads(album['notes'])
                albumdatestring = "{0}-{1}-{2}".format(jsonData['year'], jsonData['month'], jsonData["day"])
                albumdate = dt.datetime.strptime(albumdatestring, '%Y-%m-%d')
                if albumdate > recentDate:
                    recentDate = albumdate
        return recentDate

    def replace_album_from_query(query, albumname, jsonData:dict, albumcategory, count=1000000):
            album_uid = updateOrCreateAlbumByHash(albumname, jsonData, albumcategory)
            remove_photos_from_album_by_uid(album_uid)
            

            photos_in_album = []
            photos = search(query=query, count=count)
            for photo in photos:
                photos_in_album.append(photo.uid)


            result = albums_api.add_photos_to_album(uid=album_uid, photos={"photos":photos_in_album})
            return result

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

    def count_elements(seq) -> dict:
        hist = {}
        for i in seq:
            hist[i] = hist.get(i, 0) + 1

        sorted_hist = sorted(hist.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(sorted_hist)
        return converted_dict

    def determineName(PossibleCities, PossibleStates, PossibleCountries):
        PossibleName = ""
        #evaluate Cities for possible names
        counted = count_elements(PossibleCities)
        countedTotal = sum(counted.values())
        if PossibleName == "" and len(PossibleCities)>0:
            for city in counted:
                if counted[city]/countedTotal > .75:
                    PossibleName = city
            if PossibleName == "":
                keys = list(counted)
                if (counted[keys[0]]+counted[keys[1]])/countedTotal > .75:
                    PossibleName = "{0} and {1}".format(keys[0], keys[1])
        
        if PossibleName == "" and len(PossibleStates)>0:
            # Cities didn't work, evalate State now
            counted = count_elements(PossibleStates)
            countedTotal = sum(counted.values())
            for state in counted:
                if counted[state]/countedTotal > .75:
                    PossibleName = state
            if PossibleName == "":
                keys = list(counted)
                if (counted[keys[0]]+counted[keys[1]])/countedTotal > .75:
                    PossibleName = "{0} and {1}".format(keys[0], keys[1])
        
        if PossibleName == "" and len(PossibleCountries)>0:
            # State didn't work, evalate Country now
            counted = count_elements(PossibleCountries)
            countedTotal = sum(counted.values())
            for country in counted:
                if counted[country]/countedTotal > .75:
                    PossibleName = country
            if PossibleName == "":
                keys = list(counted)
                if (counted[keys[0]]+counted[keys[1]])/countedTotal > .75:
                    PossibleName = "{0} and {1}".format(keys[0], keys[1])

        if PossibleName == "":
            # Nothing worked...perhaps we are looking at untagged photos.  Regardless, set possibleName to "Unknown"
            PossibleName = "Unknown"    

    
        return PossibleName
    

    #
    # Main Logic
    #
    count = 5000
    offset = 0
    timeline = []
    ones = []
    startDate = '' if environ.get('EARLIESTDATE') is None else str(environ.get('EARLIESTDATE'))
    endDate = '' if environ.get('LATESTDATE') is None else str(environ.get('LATESTDATE'))

    while data := search(query="type:image|live after:{0} before:{1}".format(startDate, endDate), count=count, offset=offset):
        if not len(data)>0:
            log("Done building complete timeline")
            break
        log("Building complete timeline:+{0}".format(len(data)))

        #collect all photos into a timeline
        for photo in data:
            photo = photo.to_dict()
            timeline.append(photo['taken_at'])
            ones.append(1)
        offset = offset+count

    log("Number of Photos in timeline:{0}".format(len(timeline)))

    #turn the timeline into a dataframe
    df = pd.DataFrame(list(zip(timeline, ones)), columns=['Date', 'Count'])
    df['Date']= pd.to_datetime(df['Date'])

    df_daily = df.set_index('Date').resample('D')["Count"].sum().to_frame().reset_index()

    #build holiday calendar
    cal = FamilyCalendar()
    holidays = cal.holidays(return_name=True)
    holidays = holidays.reset_index(name='holiday').rename(columns={'index':'Date'})
    holidays['Date'] = holidays['Date'].dt.date

    #mark days as holidays
    df_daily['day'] = df_daily['Date'].dt.date
    df_daily = pd.merge(df_daily, holidays, left_on="day", right_on="Date", how="left")
    df_daily.drop(columns=['Date_y', 'day'], inplace=True)
    df_daily.rename(columns={'Date_x':'Date'}, inplace=True)

    #calculate the min and max based on quartile
    col='Count'
    Q1 = df_daily[col].quantile(0.25)
    Q3 = df_daily[col].quantile(0.75)
    IQR = Q3- Q1
    c = 2
    min_t = Q1 - c*IQR
    max_t = Q3 + c*IQR

    log("Calculating Anomoly Thresholds (min_t:{0} max_t:{1})".format(min_t, max_t))
    if max_t < 10:
        log("Threshold for an event is calculated below 10.  This will result in a large number of events.  Exiting...")
        return

    #mark rows which exceed threshold
    df_daily[col+'threshold_alarm'] = (df_daily[col].clip(lower = min_t,upper=max_t) != df_daily[col])

    #filter out any dates which don't cross the threshold
    rslt_df = df_daily[df_daily['Countthreshold_alarm']].reset_index()
    log("Finding Anomolies in timeline (Count:{0})".format(len(rslt_df)))

    #Setup for merging contigious dates.  Each column has a start and and end that match.
    #ID column is needed for groupby later
    rslt_df['end_date']=rslt_df['Date']
    rslt_df['id'] = 1
    rslt_df.rename(columns={'Date':'start_date'}, inplace=True)

    #Merge contigious events into single events.  Maintain Holiday tag if it already exists.  Copy holiday tag if it doesn't
    event_date_ranges = rslt_df.groupby("id", as_index=False).apply(
        lambda d: d.sort_values(["start_date", "end_date"])
        .groupby(
            ["id", (~(d["start_date"] <= (d["end_date"].shift() + pd.Timedelta(days=1)))).cumsum()],
            as_index=False
        )
        .agg({"start_date": "min", "end_date": "max", "holiday":"first"})
    ).reset_index(drop=True)
    log("Merging contigious dates(Count:{0})".format(len(event_date_ranges)))

    #If the photos ramp up or down slowly or there is a single day in the middle we want to include those.  
    #Attempting to get it on the contigious gets missed days, but doesn't handle the rising/falling edge.
    df_daily['DateP1'] = df_daily['Date'] - pd.Timedelta(days=1)
    df_daily['DateM1'] = df_daily['Date'] + pd.Timedelta(days=1)

    log("Applying rising edge event expansion")
    #Find Edges out by minus one day.
    DayMinus1 = pd.merge(event_date_ranges, df_daily, left_on="start_date", right_on="DateM1").drop(columns=[  'DateM1', 'DateP1', 'Countthreshold_alarm'])
    mask = DayMinus1["Count"]>=10
    maskholiday = DayMinus1["holiday_y"].notnull()
    maskboth = mask & maskholiday
    DayMinus1.loc[mask, "start_date"] = DayMinus1.loc[mask, "Date"]
    DayMinus1.loc[maskboth, "holiday_x"] = DayMinus1.loc[maskboth, "holiday_y"]
    DayMinus1.rename(columns={'holiday_x':'holiday'}, inplace=True)
    DayMinus1.drop(columns=[ 'holiday_y', 'Count', 'Date'], inplace=True)

    #Find Edges out by minus two days.
    DayMinus2 = pd.merge(DayMinus1, df_daily, left_on="start_date", right_on="DateM1").drop(columns=[ 'DateM1', 'DateP1', 'Countthreshold_alarm'])
    mask = DayMinus2["Count"]>=10
    maskholiday = DayMinus2["holiday_y"].notnull()
    maskboth = mask & maskholiday
    DayMinus2.loc[mask, "start_date"] = DayMinus2.loc[mask, "Date"]
    DayMinus2.loc[maskboth, "holiday_x"] = DayMinus2.loc[maskboth, "holiday_y"]
    DayMinus2.rename(columns={'holiday_x':'holiday'}, inplace=True)
    DayMinus2.drop(columns=[ 'holiday_y', 'Count', 'Date'], inplace=True)


    log("Applying falling edge event expansion")
    #Find Edges out by plus one days.
    DayPlus1 = pd.merge(DayMinus2, df_daily, left_on="end_date", right_on="DateP1").drop(columns=[ 'DateM1', 'DateP1', 'Countthreshold_alarm'])
    mask = DayPlus1["Count"]>=10
    maskholiday = DayPlus1["holiday_y"].notnull()
    maskboth = mask & maskholiday
    DayPlus1.loc[mask, "end_date"] = DayPlus1.loc[mask, "Date"]
    DayPlus1.loc[maskboth, "holiday_x"] = DayPlus1.loc[maskboth, "holiday_y"]
    DayPlus1.rename(columns={'holiday_x':'holiday'}, inplace=True)
    DayPlus1.drop(columns=[ 'holiday_y', 'Count', 'Date'], inplace=True)

    #Find Edges out by plus two days.
    DayPlus2 = pd.merge(DayPlus1, df_daily, left_on="end_date", right_on="DateP1").drop(columns=[ 'DateM1', 'DateP1', 'Countthreshold_alarm'])
    mask = DayPlus2["Count"]>=10
    maskholiday = DayPlus2["holiday_y"].notnull()
    maskboth = mask & maskholiday
    DayPlus2.loc[mask, "end_date"] = DayPlus2.loc[mask, "Date"]
    DayPlus2.loc[maskboth, "holiday_x"] = DayPlus2.loc[maskboth, "holiday_y"]
    DayPlus2.rename(columns={'holiday_x':'holiday'}, inplace=True)
    DayPlus2.drop(columns=[ 'holiday_y', 'Count', 'Date'], inplace=True)

    #Now redo the contiguous ranges step on the new ranges.  Catches an edge case where the rising and falling edges cause two ranges to merge.
    event_date_ranges2 = DayPlus2.groupby("id", as_index=False).apply(
        lambda d: d.sort_values(["start_date", "end_date"])
        .groupby(
            ["id", (~(d["start_date"] <= (d["end_date"].shift() + pd.Timedelta(days=1)))).cumsum()],
            as_index=False
        )
        .agg({"start_date": "min", "end_date": "max", "holiday":"first"})
    ).reset_index(drop=True)
    log("Recheck for contigious events post rising/falling edge expansion (Count:{0})".format(len(event_date_ranges2)))

    #Now we have a dataframe with good date ranges, holidays for anomolys in the rate of picture taking.  Lets do a few more operations to make later code a bit easier
    event_date_ranges2['end_date+1'] = event_date_ranges2['end_date'] + pd.Timedelta(days=1)
    event_date_ranges2['length'] = (event_date_ranges2['end_date']-event_date_ranges2['start_date']).dt.days+1
    event_date_ranges2['year'] = event_date_ranges2['start_date'].dt.year
    event_date_ranges2['month'] = event_date_ranges2['start_date'].dt.month
    event_date_ranges2['day'] = event_date_ranges2['start_date'].dt.day
    event_date_ranges2["start_date"] = event_date_ranges2["start_date"].dt.date
    event_date_ranges2["end_date+1"] = event_date_ranges2["end_date+1"].dt.date
    event_date_ranges2["end_date"] = event_date_ranges2["end_date"].dt.date
    event_date_ranges2.fillna("None",inplace=True)

    #Determine the most recent event that was already created...and filter out the older events
    mostRecentDate = find_most_recent_album_date_in_category("Generated Event")
    event_date_ranges2 = event_date_ranges2[event_date_ranges2["start_date"]>mostRecentDate.date()]
    log("Drop any event with a start date earlier than the most recent generated album(Count:{0}, Date:{1})".format(len(event_date_ranges2), mostRecentDate))

    #Filter out any event which ends on today's date...it's still ongoing.
    event_date_ranges2 = event_date_ranges2[event_date_ranges2["end_date"]!=dt.date.today]
    log("Drop any event with an end date of today (Count:{0})".format(len(event_date_ranges2)))

    #and now we will make an array of the information to process.
    queries = []
    for index, row in event_date_ranges2.iterrows():
        start_date = row["start_date"]
        end_date = row["end_date"]
        if start_date == end_date:
            query = "year:{0} month:{1} day:{2}".format(start_date.year, start_date.month, start_date.day)
            queries.append({'query':query, 'length':row['length'], 'year':row['year'], 'month':row['month'], 'day':row['day'], 'holiday':row['holiday']})
        else:
            start_date = row["start_date"]
            end_date = row["end_date+1"]
            query = "after:\"{0}\" before:\"{1}\"".format(start_date, end_date)
            queries.append({'query':query, 'length':row['length'], 'year':row['year'], 'month':row['month'], 'day':row['day'], 'holiday':row['holiday']})
 
    # for each query calucate a location string, select a phrase to use, and check if an album with note=query hash already exists and if not create the album
    log("Creating Event Albums")
    counter = 0
    for query in queries:
        if query['length'] < int(environ.get('SHORTESTEVENT')):
            continue
        data = search(query=query['query'], count=1000, offset=0,  order="newest")
        PossibleCities = []
        PossibleStates = []
        PossibleCountries = []
        for photo in data:
            photo = photo.to_dict()
            PossibleCities.append(photo['place_city'])
            PossibleStates.append(photo['place_state'])
            PossibleCountries.append(photo['place_country'])
        location = determineName(PossibleCities, PossibleStates, PossibleCountries)

        if query['holiday']!=("None"):
            Phrase = holidayphrase.format(query['holiday'], location, query['year'])
        elif query['length'] == 1 :
            Phrase = daytripphrase.format(location, query['day'], months[query['month']-1], query['year'])
        elif query['length'] <= 3:
            Phrase = shorttripphrase.format(location, months[query['month']-1], query['year'])

        else:
            Phrase = weekphrase.format(location, months[query['month']-1], query['year'])
        m = hashlib.sha256()
        m.update(query['query'].encode('UTF-8'))
        hash = m.hexdigest()
        query['Hash'] = hash

        uid = find_album_by_note(hash)
        if uid=='':
            log("Album with query '{0}' (Hash:{1}) does not exist".format(query['query'], hash))
            if environ.get('TRIALRUN')=="False":
                log("\tGenerating "+Phrase.format(location, query['year'])+":{0}".format(query['query'], hash))
                replace_album_from_query(query['query'], Phrase, query , "Generated Event")
                counter = counter+1
            else:
                log("\tTRIAL RUN: Generate "+Phrase.format(location, query['year'])+":{0}".format(query['query'], hash))
        else:
            log("Album with query '{0}' (Hash:{1}) already created...ignoring".format(query['query'], hash))
    log("{0} Events created.  Job Complete.".format(counter))

if __name__=="__main__":
    load_dotenv()
    detectAndCreateEvents()