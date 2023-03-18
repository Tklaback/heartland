import requests
from requests.structures import CaseInsensitiveDict
import pandas as pd
import time
import schedule
from datetime import datetime



def readData(incomingData):
    return pd.DataFrame(incomingData)

def updateCsv(date):
    currentTime = datetime.now()
    print("CREATING CSV on " +  str(currentTime.date()) + " at " + str(currentTime.time()))
    url = f"https://api.hrpos.heartland.us/v2/reports/tickets/info/{date}?includeOpenTickets=no"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer d89487c152c731ffa7444652f6ebcb93"

    resp = requests.get(url, headers=headers)

    df = readData(resp.json())
    
    df.to_csv('/Users/tyklabacka/Desktop/codePractice/pythonPrac/file.csv', index=False)



def main():
    date = datetime.today().strftime('%Y-%m-%d')
    schedule.every().day.at("22:00").do((lambda: updateCsv(date)))


    while True:
        schedule.run_pending()
        time.sleep(1)

main()
