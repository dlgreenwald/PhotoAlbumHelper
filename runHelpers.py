import datetime as dt

import schedule
import time
import timelineEvents
import ManageTimeAlbums
import heartbeat
import sys
import threading

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


# I didn't like the format of the print output of the schedule so the format has been lifted and reused.
def format(job):
        def format_time(t):
            return t.strftime("%Y-%m-%d %H:%M:%S") if t else "[never]"

        def is_repr(j):
            return not isinstance(j, schedule.Job)

        timestats = "(last run: %s, next run: %s)" % (
            format_time(job.last_run),
            format_time(job.next_run),
        )

        if hasattr(job.job_func, "__name__"):
            job_func_name = job.job_func.__name__
        else:
            job_func_name = repr(job.job_func)

        if job.job_func is not None:
            args = [repr(x) if is_repr(x) else str(x) for x in job.job_func.args]
            kwargs = ["%s=%s" % (k, repr(v)) for k, v in job.job_func.keywords.items()]
            call_repr = job_func_name + "(" + ", ".join(args + kwargs) + ")"
        else:
            call_repr = "[None]"

        if job.at_time is not None:
            return "Every %s %s at %s do %s %s" % (
                job.interval,
                job.unit[:-1] if job.interval == 1 else job.unit,
                job.at_time,
                call_repr,
                timestats,
            )
        else:
            fmt = (
                "Every %(interval)s "
                + ("to %(latest)s " if job.latest is not None else "")
                + "%(unit)s do %(call_repr)s %(timestats)s"
            )

            return fmt % dict(
                interval=job.interval,
                latest=job.latest,
                unit=(job.unit[:-1] if job.interval == 1 else job.unit),
                call_repr=call_repr,
                timestats=timestats,
            )


print("Schedualing Jobs:")
schedule.every(30).minutes.do(run_threaded, heartbeat.beat)
schedule.every().saturday.do(run_threaded, timelineEvents.detectAndCreateEvents)
schedule.every().sunday.do(run_threaded, ManageTimeAlbums.createInPastAlbums)
all_jobs = schedule.get_jobs()
for job in all_jobs:
    print(format(job))

while True:
    schedule.run_pending()
    #explicit flush to get logging in docker to work
    sys.stdout.flush()
    time.sleep(1)