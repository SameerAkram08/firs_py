import time
from plyer import notification

def drink_water_reminder():
    interval = 60 * 60  # 1 hour in seconds
    while True:
        time.sleep(interval)
        notification.notify(
            title="Drink Water Reminder",
            message="Stay hydrated! It's time to drink water.",
            timeout=10  # Notification timeout in seconds
        )

# drink_water_reminder()

# from plyer import notification

# def send_test_notification():
#     notification.notify(
#         title="Test Notification",
#         message="This is a test notification to check if the system is working.",
#         timeout=10  # Notification timeout in seconds
#     )

# send_test_notification()
# import winsound

# def send_test_beep():
#     winsound.Beep(1000, 1000)  # Beep sound for 1 second

# send_test_beep()

