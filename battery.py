import psutil

battery = psutil.sensors_battery()
percent = str(battery.percent)
print('your device have ' + percent + 'Charge!!')