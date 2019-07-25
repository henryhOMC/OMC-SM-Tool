import facebook

import json
import time
import datetime

import os

def addWeek(u_time):
    return u_time + (86400*7)


def get_api(cfg):
    
    graph = facebook.GraphAPI(cfg["access_token"])
    return graph

def getMostRecentScheduled(graph):
    r = graph.request('me?fields=scheduled_posts')
    
    ##j = json.dumps(r)

    ##print(j)

    if "scheduled_posts" in r:
        s_time = r["scheduled_posts"]["data"][0]["created_time"] #gets time of latest scheduled post
        s_time = "".join(s_time[0:10])

        u_time = time.mktime(datetime.datetime.strptime(s_time, "%Y-%m-%d").timetuple())

        return u_time
    
    elif "scheduled_posts" not in r:
        print("NO SCHEDULED POSTS.\nDEFAULTING TO COMING FRIDAY.\n\n")
        d = datetime.date.today()
        while d.weekday() != 4:
            d += datetime.timedelta(-1)
        return time.mktime(d.timetuple()) #returns LAST friday so that when addWeek is called the post will be scheduled for the coming friday

def searchJson(pageName):
    cfg = {
    "page_id"      : "",  
    "access_token" : ""  
    }
    
    with open('fb.json') as json_file:  
        data = json.load(json_file)
        for p in data['data']:
            if p['name'] == pageName:
                print('Found match with name: ' + p['name'] + "\n\n")
                cfg["page_id"] = p['name']
                cfg["access_token"] = p['access_token']

    return cfg

def schedulePosts(nextPostTime, api, fName, directory, cfg):
    os.chdir(directory)
    iterator = 1
    with open(fName, "r") as r:
        for line in r:
            r_time = datetime.datetime.utcfromtimestamp(nextPostTime).facestrftime('%Y-%m-%d')
            print("Scheduling post for " + r_time + "\n\n")
            
            photo_id = api.put_photo(image=open(str(iterator)+".png", "rb"))

            api.put_object(
                parent_object="me",
                connection_name="feed",
                message=line,
                object_attachment=photo_id,
                published="false",
                scheduled_publish_time=str(nextPostTime))
    
            iterator += 1
            nextPostTime = addWeek(nextPostTime)

    # print(nextPostTime)

    # r_time = datetime.datetime.utcfromtimestamp(nextPostTime).strftime('%Y-%m-%d')
    # print(r_time + "\n\n")


    # api.put_object(
    #     parent_object="me",
    #     connection_name="feed",
    #     message="This is a great website. Everyone should visit it.",
    #     link="https://www.facebook.com",
    #     published="false",
    #     scheduled_publish_time=str(nextPostTime))

    # postForm = "/" + cfg["page_id"] + "/feed"

    #api.put_object(postForm, json.dumps(attachment))    

    #"/"+cfg['page_id']+"" + 
    #message = "/feed?message=I%20love%20the%20rain!&published=false&scheduled_publish_time="+str(nextPostTime)
    #api.put_object("/feed?access_token="+cfg["access_token"] +"&message=I%20love%20the%20rain!&published=false&scheduled_publish_time="+str(nextPostTime)[:-2], connection_name="feed")

"""     attachment =  {
        'name': 'Link name'
        'link': 'https://www.example.com/',
        'caption': 'Check out this example',
        'description': 'This is a longer description of the attachment',
        'picture': 'https://www.example.com/thumbnail.jpg'
    } """



def mainScheduler(fName, directory):
    pageName = input("Facebook Page Name: ")
    cfg = searchJson(pageName)

    api = get_api(cfg)

    nextPostTime = addWeek(getMostRecentScheduled(api))

    schedulePosts(nextPostTime, api, fName, directory, cfg)