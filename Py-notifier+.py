import time
from plyer import notification

print("""
    
 ____          _   _       _   _  __ _                
|  _ \ _   _  | \ | | ___ | |_(_)/ _(_) ___ _ __  _   
| |_) | | | | |  \| |/ _ \| __| | |_| |/ _ \ '__|| |_ 
|  __/| |_| | | |\  | (_) | |_| |  _| |  __/ | |_   _|
|_|    \__, | |_| \_|\___/ \__|_|_| |_|\___|_|   |_|  
       |___/                                       
    
""")




print("Python notifier is running...")


def pynotification(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "",
        timeout = 10,
    )



def water_reminder(tinter):
    while True:
        print("You will be notify in", tinter/60, "minutes!")
        time.sleep(tinter)
        pynotification("Drink Water!!", "It has been more than two hours since you last drank water")



def notify3(tlt, msg, ti):
    while True:
        print("You will be notify in", ti/60, "minutes")
        time.sleep(ti)
        pynotification(tlt, msg)




opc = ""
while opc != "exit":
    print("\n1) Water reminder")
    print("2) Custom reminder")


    opc = input("Insert option: ")

    if opc == "1":
        wt = int(input("Insert the time interval for the reminder (minutes): "))
        wt2 = wt * 60
        water_reminder(wt2)
    elif opc == "2":
        tt = input("Insert the title for the reminder: ")
        m = input("Insert the message for the reminder: ")
        t = int(input("Insert the time interval for the reminder (minutes): "))
        t2 = t * 60
        notify3(tt, m, t2)
    elif opc == "exit":
        print("Stoping...")
    else:
        print("ERROR! - INVALID OPTION!")













