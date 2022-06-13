import webbrowser
import time
import random


x='y'
y='n'


z=input('Are You A Hacker? (y or n)  ')

if z == x:
    while True:
        site = random.choice(['google.com' , 'facebook.com'])
        visit = "http://{}".format(site)
        webbrowser.open(visit)
        seconds = random.randrange(0,10)
        time.sleep(seconds)
        exit

elif z == y:
    while True:
        site = random.choice(['google.com' , 'facebook.com'])
        visit = "http://{}".format(site)
        webbrowser.open(visit)
        seconds = random.randrange (0,10)
        time.sleep (seconds)
        exit
else:
   print('visit our site to learn hack:          ')
