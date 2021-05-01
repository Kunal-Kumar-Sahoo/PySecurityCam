from plyer import notification
from pushbullet import Pushbullet


def desktop_notify(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=5
        )
    except Exception:
        return desktop_notify(title, message)


def mobile_notify(title, message):
    file = open("credentials.txt")
    api_key = file.readlines()[0]
    pb = Pushbullet(api_key)
    pb.push_note(title, message)
    file.close()

