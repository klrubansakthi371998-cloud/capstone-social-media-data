import schedule
import time

def run_job():
    print("Collecting social media data...")

schedule.every().day.at("09:00").do(run_job)

print("Automation Scheduler Running")

while True:
    schedule.run_pending()
    time.sleep(1)