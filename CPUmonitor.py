import psutil
import time

def monitor_cpu(threshold):
    print("Monitoring CPU usage...")
    try:

        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            time.sleep(1)
    except KeyboardInterrupt:  
# by pressing ctrl+c
        print("Monitoring stopped.")



threshold = 80  # Set your desired threshold here
monitor_cpu(threshold)



        