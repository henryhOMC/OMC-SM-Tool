from facebookScheduler import *
from smText import *
from twitterScheduler import *
from makeDOC import *

from multiprocessing import Process

def main():
    #intro message
    intro = open("intr.o", "r")
    print(intro.read())
    ###################

    fName, directory, companyName = makePosts()
    
    lastScheduledDate = input("Enter the date of the last scheduled post, in the format \"YYYY-MM-DD\": ")
    scheduleDate = datetime.strptime(lastScheduledDate, "%Y-%m-%d")



    b = 4
    while b != '0':
        b = input("Check posts for grammatical errors...\nEnter 1 to schedule posts for twitter\nEnter 2 to schedule posts for facebook\nEnter 3 to create a Word Doc with the pictures and captions\nEnter 0 to quit\n\nEXPERIMENTAL!\nEnter 9 to post to facebook and twitter simultaneously\n\nINPUT: ")

        if b == '1':
            t_scheduler(fName, directory, scheduleDate)

        if b == '2':
            f_scheduler(fName, directory, scheduleDate)

        if b == '3':
            makeDOC(fName, directory, companyName)

        if b == '9':
            loginInfo = ["", ""]
            loginInfo[0] = input("Enter email used for client's twitter account: ")
            loginInfo[1] = input("Enter password used for client's twitter account: ")

            url = input("\n\nInput the client's facebook URL:\n")

            p1 = Process(target=t_scheduler, args=(fName, directory, scheduleDate, loginInfo, ))
            p1.start()
            p2 = Process(target=f_scheduler, args=(fName, directory, scheduleDate, url, ))
            p2.start()
            p1.join()
            p2.join()
            
        elif b == '0':
            quit()



if __name__ == "__main__":
    main()