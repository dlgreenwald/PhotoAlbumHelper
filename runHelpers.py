import datetime as dt

from scheduler import Scheduler
from scheduler.trigger import Saturday, Sunday
import time
import timelineEvents
import ManageTimeAlbums
import heartbeat


schedule = Scheduler()
schedule.cyclic(dt.timedelta(minutes=30), heartbeat.beat)
schedule.weekly(Saturday, timelineEvents.detectAndCreateEvents)
schedule.weekly(Sunday, ManageTimeAlbums.createInPastAlbums)

print(schedule)

while True:
    schedule.exec_jobs()
    time.sleep(1)