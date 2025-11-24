import time
import threading

def cpu_load():
    # Busy loop for CPU load
    while True:
        pass  # Keep CPU busy

# Create 2 CPU load threads (increase to 4 or 8 to load more cores)
for _ in range(2):
    t = threading.Thread(target=cpu_load)
    t.daemon = True
    t.start()

# Keep program running for 60 seconds
time.sleep(60)


# IN THE CRONTAB -  "by (crontab -e)"
# */5 * * * * /usr/bin/python3 /home/royden147/Desktop