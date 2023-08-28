from plyer import notification
import time


if __name__=="__main__":
    while True:
        title="Learn this Vocab"
        app_icon="abc.ico"
        with open("Vocabulary2.txt") as vc:
            lines = vc.readlines()

            for vocab in lines:
                notification.notify(title= title,message= vocab.strip(),app_icon=app_icon,timeout= 10)
                time.sleep(30)