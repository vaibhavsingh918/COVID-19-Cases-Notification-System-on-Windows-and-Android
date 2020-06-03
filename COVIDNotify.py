from plyer import notification
from bs4 import BeautifulSoup
import requests
import time
from notify_run import Notify

def notifyAlert(title, message) :
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:/Users/hp/COVID19_Cases_Notification_System/COVID_icon.ico",
        timeout = 15
    )

def getData(url) :
    req = requests.get(url)
    return req.text 

if __name__ == "__main__" :
    while True :
        # notifyAlert("COVID 19 Disease", "Stay Safe !")
        notify = Notify() # To notify through web push notifications to android mobile phones
        htmlData = getData('https://www.mohfw.gov.in/')
        
        soup = BeautifulSoup(htmlData, 'html.parser')
        # print(soup.prettify())
        cases = ""
        for tr in soup.find_all('tbody')[0].find_all('tr') :
            cases = cases + tr.get_text()
        cases = cases[1:]
        caselist = cases.split("\n\n")
        states = ["Uttar Pradesh","Madhya Pradesh","Maharashtra","Delhi","Rajasthan","Bihar"]
        statewiseCases = []
        for item in caselist :
            statewiseCases.append(item.split("\n"))
        Title = "Total COVID-19 Cases in India"
        Message = "Total Cases : "+statewiseCases[40][1]+"\nActive Cases : "+statewiseCases[37][2]+"\nCured/Discharged Cases : "+statewiseCases[38][0]+"\nDeaths : "+statewiseCases[39][1]
        notifyAlert(Title, Message)
        notify.send(Title+'\n'+Message+'\n'+'This is a real-time data notification of COVID-19 cases created by Vaibhav Singh')
        time.sleep(2)
        for statelist in statewiseCases[0:34] :
            if statelist[1] in states :
                # print(statelist)
                Title = "COVID-19 Cases in India - Statewise"
                Message = statelist[1]+":-\n"+"Active Cases : "+statelist[2]+"\n"+"Cured/Discharged Cases : "+statelist[3]+"\n"+"Deaths : "+statelist[4]+"\n"+"Total Confirmed Cases : "+statelist[5]
                notifyAlert(Title, Message)
                notify.send(Title+'\n'+Message+'\n'+'This is a real-time data notification of COVID-19 cases created by Vaibhav Singh')
                time.sleep(2)
        time.sleep(7200)
            
