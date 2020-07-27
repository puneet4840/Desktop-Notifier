# Downloading https://pvsc.azureedge.net/python-language-server-stable/Python-Language-Server-win-x64.0.5.51.nupkg...

# Project-2 (Desktop Notifier)
# Main file for Desktop Notifier project.
# win10toast python library is used to display notification in desktop.
print()

from win10toast import ToastNotifier
from datetime import time,datetime
from threading import Thread
from bs4 import BeautifulSoup
import requests
from newspaper import article
from time import sleep
import wolframalpha


def Notify(title,message):
    n=ToastNotifier()
    n.show_toast(title=title,msg=message,duration=8)

t=datetime.now().strftime('Time:  %I:%M  %p')

t2=datetime.now()
t3=datetime.now()
def Water():
    Notify(f'Drink Water   ({t})','Please Drink 2 Cups Of Water')
def D_W():
    while True:
        if t2.hour==9 and t2.minute==55:
            Water()
        elif t2.hour==10 and t2.minute==50:
            Water()
        elif t2.hour==11 and t2.minute==45:
            Water()
        elif t2.hour==12 and t2.minute==40:
            Water()
        elif t2.hour==13 and t2.minute==35:
            Water()
        elif t2.hour==14 and t2.minute==30:
            Water()
        elif t2.hour==15 and t2.minute==25:
            Water()
        elif t2.hour==16 and t2.minute==20:
            Water()
        elif t2.hour==17 and t2.minute==15:
            Water()
        elif t2.hour==18 and t2.minute==10:
            Water()

def Eyes_Exe():
    Notify(f'Eyes Exercise  ({t})',"It's Time To Do Eyes Exercise")
def D_E():
    while True:
        if str(t3.hour)==9 and t3.minute==45:
            Eyes_Exe()
        elif t3.hour==10 and t3.minute==30:
            Eyes_Exe()
        elif t3.hour==11 and t3.minute==15:
            Eyes_Exe()
        elif t3.hour==12 and t3.minute==00:
            Eyes_Exe()
        elif t3.hour==00 and t3.minute==45:
            Eyes_Exe()
        elif t3.hour==13 and t3.minute==30:
            Eyes_Exe()
        elif t3.hour==14 and t3.minute==15:
            Eyes_Exe()
        elif t3.hour==15 and t3.minute==00:
            Eyes_Exe()
        elif t3.hour==15 and t3.minute==45:
            Eyes_Exe()
        elif t3.hour==16 and t3.minute==30:
            Eyes_Exe()
        elif t3.hour==17 and t3.minute==15:
            Eyes_Exe()
        elif t3.hour==18 and t3.minute==00:
            Eyes_Exe()
        elif t3.hour==18 and t3.minute==45:
            Eyes_Exe()


def Phy_Exe():
    Notify(f"Physical Exercise   ({t})","It's Time To Do Some Physical Exercise")

def D_PE():
    while True:
        if t3.hour==10 and t3.minute==10:
            Phy_Exe()
        elif t3.hour==11 and t3.minute==9:
            Phy_Exe()
        elif t3.hour==12 and t3.minute==8:
            Phy_Exe()
        elif t3.hour==13 and t3.minute==1:
            Phy_Exe()
        elif t3.hour==14 and t3.minute==5:
            Phy_Exe()
        elif t3.hour==15 and t3.minute==4:
            Phy_Exe()
        elif t3.hour==16 and t3.minute==6:
            Phy_Exe()
        elif t3.hour==17 and t3.minute==7:
            Phy_Exe()
        elif t3.hour==18 and t3.minute==22:
            Phy_Exe()

def News():
    url="https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=52afef4f44314099adb8a2b5841009df"
    bbc=requests.get(url).json()
    article=bbc["articles"]
    results=[]

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        print(i+1,':',results[i]) 
    for head in results:
        Notify(f"Headline   ({t})",head)
        sleep(240)

def get_n():
    time1=datetime.now()
    while True:
        if time1.hour==10 and time1.minute==2:
            News()
        elif time1.hour==12 and time1.minute==2:
            News()
        elif time1.hour==14 and time1.minute==2:
            News()
        elif time1.hour==16 and time1.minute==2:
            News()
        elif time1.hour==17 and time1.minute==2:
            News()

def temperature():
    app_id='JE47GT-G2l459KLh6'
    client=wolframalpha.Client(app_id)
    result=client.query('Temeprature of Dibai')
    ans=next(result.results).text
    Notify(f'Dibai   ({t})',f'Temperature:  {ans}')

def get_temp():
    time4=datetime.now()
    while True:
        if time4.hour==9 and time4.minute==10:
            temperature()
        elif time4.hour==11 and time4.minute==11:
            temperature()
        elif time4.hour==13 and time4.minute==13:
            temperature()
        elif time4.hour==15 and time4.minute==15:
            temperature()
        elif time4.hour==16 and time4.minute==16:
            temperature()

def Covid_19():
    try:
        url='https://www.mohfw.gov.in/'
        html_1=requests.get(url).content
        soup=BeautifulSoup(html_1,'html.parser')
        for table in soup.find_all('tbody')[0].find_all('tr'):
            data=table.get_text()
            data_list=data.split("\n")
            data_list=data_list[1:7]
            active_cases=""
            cured=""
            death=""
            t_c_c=""
            if data_list[1] in ["Delhi"]:
                # print(data_list[1:])
                for _ in data_list:
                    delhi=data_list[1]
                    active_cases=data_list[2]
                    cured=data_list[3]
                    death=data_list[4]
                    t_c_c=data_list[5]
                    Notify("Covid-19  ",f'{delhi}  ({t}): \nActive Cases: {active_cases}\nCured: {cured}\nDeath: {death}\nTotal Confirmed Cases: {t_c_c}')
                    break
            if data_list[1] in ["Uttar Pradesh"]:
                # print(data_list[1:])
                for _ in data_list:
                    UP=data_list[1]
                    active_cases1=data_list[2]
                    cured1=data_list[3]
                    death1=data_list[4]
                    t_c_c1=data_list[5]
                    Notify("Covid-19  ",f'{UP}  ({t}): \nActive Cases: {active_cases1}\nCured: {cured1}\nDeath: {death1}\nTotal Confirmed Cases: {t_c_c1}')
                    break
    except:
        Notify("Connection Error","Check Your Internet Connection")

def get_co():
    time2=datetime.now()
    while True:
        if time2.hour==10 and time2.minute==10:
            Covid_19()


if __name__ == "__main__":

    
    thread1=Thread(target=D_W)
    thread2=Thread(target=D_E)
    thread3=Thread(target=D_PE)
    thread4=Thread(target=get_n)
    thread5=Thread(target=get_co)
    thread6=Thread(target=get_temp)
        
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    # Notify('Puneet',str(t2))
    # Water()
    # News()
    # Covid_19()
    # temperature()