import schedule
import time
from datetime import datetime



def abd():
    now=(datetime.today())
    print("current time is ",now)
    print("This is test Schedule")

#schedule.every(10).seconds.do(abd)
#schedule.every(10).minutes.do(abd)
#schedule.every(10).hours.do(abd)
#schedule.every().day.at("15:18").do(abd)
#schedule.every(5).weeks.at("15:18").do(abd)
schedule.every().monday.at("15:18").do(abd)

while True:
        schedule.run_pending()
        time.sleep(1)



