import psutil
import time

def monitor_cpu(threshold):
    print("Monitoring CPU usage...")
    try:

        while True:
            cpu_usage = psutil.cpu_percent(interval=5)
            mem_usage= psutil.virtual_memory().percent
            cpustat=psutil.cpu_stats()
            cpufreq=psutil.cpu_freq()
            # diskusages=psutil.disk_usage("C:\Users\Ravik").percent
            
            if cpu_usage > threshold or mem_usage >80:
            
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%,{mem_usage}")
                print('\n',cpustat)
                print('\n',cpufreq)
                # print(diskusages)

            time.sleep(5)
    except KeyboardInterrupt:  
# by pressing ctrl+c
        print("Monitoring stopped.")



threshold = 80  # Set your desired threshold here
monitor_cpu(threshold)



        