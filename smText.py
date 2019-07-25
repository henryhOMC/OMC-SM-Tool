from itertools import zip_longest
from shutil import copyfile
from time import sleep

import sys
import os


#copyfile(src, dst)
#cwd+"/"+companyName+"/"

def makeLawPosts(fName, clientName, companyName, site, phone):
    needsCategories = input("Enter 'Y' to select specific law practice (i.e. criminal, family law) or enter 'N' for generic posts only: ")
    needsCategories = needsCategories.lower()
    
    cwd = os.getcwd()

    gen = open(cwd+"/originals/SM-lawyer-generic.orig", "r")
    outfile = open(fName, "w")

    crim = open("empty", "r")
    fam = open("empty", "r")
    est = open("empty", "r")
    inj = open("empty", "r")
    rel = open("empty", "r")


    if needsCategories == "y":
        isCriminal = input("Criminal Defense? Enter 'Y' or 'N': ")
        isCriminal = isCriminal.lower()
        if isCriminal == 'y':
            crim.close()
            crim = open(cwd+"/originals/SM-lawyer-criminal.orig", "r")
            

        isFamily = input("Family Law? Enter 'Y' or 'N': ")
        isFamily = isFamily.lower()
        if isFamily == 'y':
            fam = open(cwd+"/originals/SM-lawyer-family.orig", "r")
            

        isEstatePlanning = input("Estate Planning Law? Enter 'Y' or 'N': ")
        isEstatePlanning = isEstatePlanning.lower()
        if isEstatePlanning == 'y':
            est = open(cwd+"/originals/SM-lawyer-estate.orig", "r")
            

        isInjury = input("Injury Law? Enter 'Y' or 'N': ")
        isInjury = isInjury.lower()
        if isInjury == 'y':
            inj = open(cwd+"/originals/SM-lawyer-injury.orig", "r")

        isRealEstate = input("Real Estate? Enter 'Y' or 'N': ")
        isRealEstate = isRealEstate.lower()
        if isRealEstate == 'y':
            rel = open(cwd+"/originals/SM-lawyer-realestate.orig", "r")    
        
    i = 1
    for lines in zip_longest(gen, crim, fam, est, inj, rel):
        for line in lines:
            if line is not None and line[-2] != ')':
                path = line.split(")")
                line = path[1]
                path = path[0]
                
                imagePath =  cwd + "/originals/" + "".join(path[1:])


                copyfile(imagePath, cwd + "/" + companyName + "/" + str(i) + ".png")

                line = line.replace('$OFFICE', companyName)
                line = line.replace('$PHONE', phone)
                line = line.replace('$NAME', clientName)
                line = line.replace('$SITE', site)

                if len(line) > 255: #mark posts with an asterik if they exceed twitter's character limit
                    line = "* "+line

                print(line, file=outfile, end='')

                i+=1

    gen.close()
    outfile.close()
    
    crim.close()
    fam.close()
    est.close()
    inj.close()
    rel.close()


    print("Success!\nLaw posts created!\n")
    





def makeTravelPosts(fName, clientName, companyName, site, phone):
    exit()





def makeChiroPosts(fName, clientName, companyName, site, phone):
    cwd = os.getcwd()
    
    outfile = open(fName, "w")
    original = open(cwd+"/originals/SM-chiro.orig", "r")

    i = 1

    for line in original:
        if line is not None and line[-2] != ')':
            path = line.split(")")
            line = path[1]
            
            path = path[0]
            
            imagePath =  cwd + "/originals/" + "".join(path[1:])


            copyfile(imagePath, cwd + "/" + companyName + "/" + str(i) + ".png")

            line = line.replace('$OFFICE', companyName)
            line = line.replace('$PHONE', phone)
            line = line.replace('$NAME', clientName)
            line = line.replace('$SITE', site)

            if len(line) > 255: #mark posts with an asterik if they exceed twitter's character limit
                line = "* "+line

            print(line, file=outfile, end='')

            i+=1
    
    original.close()
    outfile.close()


    print("Success!\nChiropractor posts created!\n")





def makeInsurancePosts(fName, clientName, companyName, site, phone):
    cwd = os.getcwd()
    
    outfile = open(fName, "w")
    original = open(cwd+"/originals/SM-insurance.orig", "r")

    i = 1

    for line in original:
        if line is not None and line[-2] != ')':
            path = line.split(")")
            line = path[1]
            
            path = path[0]
            
            imagePath =  cwd + "/originals/" + "".join(path[1:])


            copyfile(imagePath, cwd + "/" + companyName + "/" + str(i) + ".png")

            line = line.replace('$OFFICE', companyName)
            line = line.replace('$PHONE', phone)
            line = line.replace('$NAME', clientName)
            line = line.replace('$SITE', site)

            if len(line) > 255: #mark posts with an asterik if they exceed twitter's character limit
                line = "* "+line

            print(line, file=outfile, end='')

            i+=1
    
    original.close()
    outfile.close()





def makeDentistPosts(fName, clientName, companyName, site, phone):
    cwd = os.getcwd()
    
    outfile = open(fName, "w")
    original = open(cwd+"/originals/SM-ped-dentist.orig", "r")

    i = 1

    for line in original:
        if line is not None and line[-2] != ')':
            path = line.split(")")
            line = path[1]
            
            path = path[0]
            
            imagePath =  cwd + "/originals/" + "".join(path[1:])


            copyfile(imagePath, cwd + "/" + companyName + "/" + str(i) + ".png")

            line = line.replace('$OFFICE', companyName)
            line = line.replace('$PHONE', phone)
            line = line.replace('$NAME', clientName)
            line = line.replace('$SITE', site)

            if len(line) > 255: #mark posts with an asterik if they exceed twitter's character limit
                line = "* "+line

            print(line, file=outfile, end='')

            i+=1
    
    original.close()
    outfile.close()


    print("Success!\nDentist posts created!\n")





def makePosts():
    #determine industry
    clientType = input("Enter type of company (law firm, insurance agency, travel agency, dentist, or chiropractor): ")
    clientType.lower()
    
    companyName = input ("Name of Company: ")

    cwd = os.getcwd()
    directory = os.path.join(cwd, companyName)
    fName = companyName+"-SM-text.txt"
    
    exists = False
    try:
        os.mkdir(cwd+"/"+companyName+"/")
        test = open(companyName+"/"+fName, "x")
        test.close()
    except FileExistsError:
        print("\n\nPosts for this company already exist.\nCheck to make sure the posts have not been used yet.\n\n")
        print("Defaulting to existing posts.\n\n")
        exists = True

    if exists == False:    
        clientName = input ("(To be used in social posts. Probably NOT the office manager...)\nClient Name: ")
        site = input ("Website: ")
        phone = input ("Phone Number: ")

    
    

    

    if exists == False:
        if clientType == "law firm":
            makeLawPosts(companyName+"/"+fName, clientName, companyName, site, phone)
        elif clientType == "insurance agency":
            makeInsurancePosts(companyName+"/"+fName, clientName, companyName, site, phone)
        elif clientType == "travel agency":
            makeTravelPosts(companyName+"/"+fName, clientName, companyName, site, phone)
        elif clientType == "dentist":
            makeDentistPosts(companyName+"/"+fName, clientName, companyName, site, phone)
        elif clientType == "chiropractor":
            makeChiroPosts(companyName+"/"+fName, clientName, companyName, site, phone)
        else:
            print("Business type not supported")
            quit()    


    return fName, directory, companyName