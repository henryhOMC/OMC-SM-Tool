from datetime import date
import time

def getLastScheduledPost():
    return 1559304000

ep =  getLastScheduledPost()

readable = time.ctime(ep)

i =0
for i in range(0,10):
    with open("stamps.csv", "wt") as f:
        f.write(ep +"," + readable)        

#ep += (86400*6)

#d = date.fromtimestamp(ep / 1000)
#print(d.strftime('%A')) 

# i = 0
# for i in range(0,10):
#     d = date.fromtimestamp(ep / 1000)
#     if d.strftime('%A') is 'Friday':
#         print('True')
#     else:
#         print(False)
#     #ep += (86400*7) 




