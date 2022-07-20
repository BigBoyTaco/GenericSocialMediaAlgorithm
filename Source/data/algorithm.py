from users import userManager
from content import contentManager
import os, random

def show(content):
    points = 0
    #for every item in content
    for item in content:
        #if the item in content is also in user
        if(item in userManager.interests):
            points += 1
    #retun points of content for user
    return points

def comparePoints(points):
    #get largest value index in points
    return points.index(max(points))

#returns the content id of a peice of content fit for the viewer
def contentRquest(user):
    #get user info
    userInfo = userManager.GetUserInfo(user)
    interests = userInfo.get("interests")
    #get available content
    potentialContent = contentManager.getAvalableContent()
    #remove all items that are not in users interests
    for i in potentialContent:
        if(i not in interests):
            potentialContent.remove(i)
            print('removed ' + i)
    #find all the content in potentialContent
    content = []
    for i in potentialContent:
        #for every item in a potential content folder add it to content
        for c in os.listdir(os.getcwd() + "\\content\\content\\" + str(i)):
            content.append(c)
    #return a random content id that fits user interests
    return content[random.randint(0, int(len(content)) - 1)]