# win10toast python library is used to show notification through windows in desktop.
print()

from win10toast import ToastNotifier
import datetime
import time 

def NotifyMe(title,message):
    n=ToastNotifier()

    n.show_toast(title=title,msg=message,duration=5)

t=datetime.datetime.now()

if __name__ == "__main__":
    NotifyMe(f'Hii  {t}','Puneet')
    # if t.hour==11 and t.minute==37:
    #     print("True")
    # else:
    #     print('False')
    
