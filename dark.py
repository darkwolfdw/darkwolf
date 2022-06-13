import webbrowser
import time
import random


x='y'
y='n'


z=input('Are You A Hacker? (y or n)  ')

if z == x:
    while True:
        #you can put any other site or beef link to hack
        site = random.choice(['google.com' , 'facebook.com'])
        visit = "http://{}".format(site)
        webbrowser.open(visit)
        seconds = random.randrange(0,5)
        time.sleep(seconds)
        exit

elif z == y:
    while True:
         #you can put any other site or beef link to hack
        site = random.choice(['google.com' , 'facebook.com'])
        visit = "http://{}".format(site)
        webbrowser.open(visit)
        seconds = random.randrange (0,5)
        time.sleep (seconds)
        exit
else:
   print('try again with (y or n))          ')
