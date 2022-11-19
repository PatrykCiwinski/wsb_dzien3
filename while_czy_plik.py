import os
import time

while not os.path.exists('plik.txt'):
    print('plik nie istnieje')
    time.sleep(2)

print('plik istnieje')