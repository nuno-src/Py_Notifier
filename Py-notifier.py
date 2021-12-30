import time
from plyer import notification






def pynotification(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "",
        timeout = 10,
    )



if __name__ == '__main__':
    while True:
        time.sleep(7200)
        pynotification("Drink Water!!", "It has been more than two hours since you last drank water")



