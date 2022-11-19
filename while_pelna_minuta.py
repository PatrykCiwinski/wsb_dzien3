import datetime
import time

print(datetime.datetime.now().second)

while datetime.datetime.now().second<50:
    print('czekam na pełną minutę')
    time.sleep(2)
print('pełna minuta zaraz...')