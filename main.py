from datetime import datetime

now = datetime.now()

time = now.strftime("%H:%M:%S")
date = now.strftime("%d.%m.%Y")

print(time)
print(date)
