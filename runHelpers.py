import time
import threading
import sys

import schedule
from dotenv import load_dotenv

import timelineEvents
import ManageTimeAlbums
import emailAlerts

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


# I didn't like the format of the print output of the schedule so the format has been lifted and reused.
def format(job):
    def format_time(t):
        return t.strftime("%Y-%m-%d %H:%M:%S") if t else "[never]"

    def is_repr(j):
        return not isinstance(j, schedule.Job)

    timestats = f"(last run: {format_time(job.last_run)}, next run: {format_time(job.next_run)})"

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
        return f"Every {job.interval} {job.unit[:-1] if job.interval == 1 else job.unit} at {job.at_time} do {call_repr} {timestats}"
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

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def schedule_and_run():
    print("Scheduling Jobs:")
    schedule.every(1).day.at("01:00").do(run_threaded, timelineEvents.detectAndCreateEvents)
    schedule.every().sunday.do(run_threaded, ManageTimeAlbums.create_in_past_albums)
    schedule.every().sunday.do(run_threaded, emailAlerts.emailAlert)

    init = True
    progress = 0
    sleep_len = 1
    while True:
        next_job = schedule.idle_seconds()
        if next_job > 0 and not init:
            # We are continuing to progress towards the next job
            progress = progress +1
            sys.stdout.write(ERASE_LINE) 
            print("*" * progress)
            sys.stdout.write(CURSOR_UP_ONE) 
        else:
            # We will start a new job
            print("\n")
            schedule.run_pending()
            next_job = schedule.idle_seconds()

            #setup progress bar for next job
            init = False
            progress = 0
            sleep_len =  next_job/40
            all_jobs = schedule.get_jobs()
            for job in all_jobs:
                print(format(job))
            print("0                 50                 100")
            print("----------------------------------------")
        time.sleep(sleep_len)


if __name__=="__main__":
    load_dotenv()
    schedule_and_run()
