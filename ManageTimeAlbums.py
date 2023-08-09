from photoprism.Session import Session
from photoprism.Photo import Photo
from datetime import date
from datetime import datetime
from datetime import timedelta
from num2words import num2words


def getDateRangeFromWeek(p_year,p_week):

    firstdayofweek = datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    lastdayofweek = firstdayofweek + timedelta(days=6.9)
    return firstdayofweek, lastdayofweek

def ManageAlbum(session, queryString, title, count=100):
    p = Photo(session)
    if p.check_if_album_exists(title):
        print("'{0}` already exists, clearing photos".format(title))
        p.remove_photos_from_album(albumname=title)
    else:
        print("Creating Album `{0}`".format(title))
        p.create_album(title)
    if p.add_to_album_from_query(query=queryString, albumname=title, count=count):
        print("Album `{0}` photos inserted".format(title))
        return True
    else:
        print("Album `{0}` photos failed to insert.  Deleteing Album.".format(title))
        p.remove_album(albumname=title)
        return False

pp_session = Session("admin", "2qG0VBiGeskD", "photos.dlgreen.com", use_https=True)
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
print("One Week Ago: Week #{0}:{1} through {2}".format(last_week, firstdate, lastdate))
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
print("One Month Ago: Week #{0}".format(last_month))
queryString = "after:\"{0}\" before:\"{1}\"".format(firstdate, lastdate)
ManageAlbum(session=pp_session, queryString=queryString, title="One Month Ago This Week")

#Create all the previous year albums
for year in range(OldestYear, CurrentYear):
    firstdate, lastdate = getDateRangeFromWeek(year, week_num)
    YearDiff = CurrentYear-year
    yearstring = "Years" if YearDiff>1 else "Year"
    title = "{0} {1} Ago This Week".format(num2words(YearDiff).capitalize(), yearstring)
    print("{1}: Week #{0}".format(week_num, title))
    queryString = "after:\"{0}\" before:\"{1}\"".format(firstdate, lastdate)
    ManageAlbum(session=pp_session, queryString=queryString, title=title)

