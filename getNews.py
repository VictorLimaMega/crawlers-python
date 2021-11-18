import schedule
import time
from LoginOns import main as getNews

def job():
	getNews()

schedule.every(30).seconds.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)