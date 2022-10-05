
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Descansa weeee ya paso un prro minuto!!!!!!!",
            timeout = 10
        )
        time.sleep(60)
        
        