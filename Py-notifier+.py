import time
import multiprocessing
import threading
from plyer import notification


print("""
    
 ____          _   _       _   _  __ _                
|  _ \ _   _  | \ | | ___ | |_(_)/ _(_) ___ _ __  _   
| |_) | | | | |  \| |/ _ \| __| | |_| |/ _ \ '__|| |_ 
|  __/| |_| | | |\  | (_) | |_| |  _| |  __/ | |_   _|
|_|    \__, | |_| \_|\___/ \__|_|_| |_|\___|_|   |_|  
       |___/                                       
    
""")

processos = []

z = []
ttt = []

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
        print("You will be notify to drink water in", tinter/60, "minutes!")
        time.sleep(tinter)
        #pynotification("Drink Water!!", "It has been a while since you last drank water... Stay hydrated!!")
        notification.notify(
            title="drink water",
            message="drink water",
            app_icon="",
            timeout=10,
        )



def reminder(kkk):
    while True:
        print("You will be notify in", kkk/60, "minutes!")
        time.sleep(kkk)
        notification.notify(
            title="bcbcbcb",
            message="rtrtetetqseew",
            app_icon="",
            timeout=10,
        )


def notify3(tlt, msg, ti):
    while True:
        print("You will be notify in", ti/60, "minutes")
        time.sleep(ti)
        pynotification(tlt, msg)




opc = ""
while opc != "exit":
    print("\n1) Water reminder")
    print("2) Custom reminder")
    print("3) Set multiple reminders")


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
    elif opc == "3":

        tt = input("Insert the title for the reminder: ")
        m = input("Insert the message for the reminder: ")
        t = int(input("Insert the time interval for the reminder (minutes): "))
        t2 = t * 60

        #threading.Thread(target=water_reminder(t2)).start()
        #threading.Thread(target=notify3(tt, m, t2)).start()

        #for x in range(2):

        #p2 = multiprocessing.Process(target=notify3(tt, m, t2))
        p2 = multiprocessing.Process(target=reminder(t2))
        p1 = multiprocessing.Process(target=water_reminder(t2))

        if __name__ == '__main__':
            p1.start()
            p2.start()
            processos.append(p1)
            processos.append(p2)

        for p in processos:
            p.join()

        # p1 = multiprocessing.Process(target=water_reminder(t2))
        # p2 = multiprocessing.Process(target=notify3(tt, m, t2))
        #
        # if __name__ == '__main__':
        #     p1.start()
        #     p2.start()


            # p = multiprocessing.Queue(target=notify3(tt,m,t2))#, args=['tt','m',t2])
            # p.start()
            # print("zip: " ,z)
            # print(ttt)
            # print(dados)


        #if __name__ == "__main__":
            #p.start()
            #processos.append(p)

        # for p in processos:
        #     p.join()
        #threading.Timer


    elif opc == "exit":
        print("Stoping...")
    else:
        print("ERROR! - INVALID OPTION!")













