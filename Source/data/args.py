from email import contentmanager
import os
from data import algorithm
from content import contentManager
#import commands


def checkForPassedArgs(args):
    #import the user
    try:
        from users import userManager
    except:
        print("could not find userManager")
    #if we want to create a new user
    try:
        if(args[1] == "-n"):
            userManager.createUser(args[2], args[3], args[4], args[5])
        elif(args[1] == "-s"):
            print(algorithm.contentRquest(args[2]))
        elif(args[1] == "-a"):
            userManager.addInterest(args[2], args[3])
        elif(args[1] == "-v"):
            contentManager.createContent(args[2].split(','))
        elif(args[1] == "-d"):
            contentManager.delAllContent()
        elif(args[1] == "-h" or args[1] == "help"):
            print('''HELP:
    commands:
        -h: show this help msg
        -n: create a new user (Ex: gsa -n usrName name birthday email)
        -s: serve content to user (Ex: gsa -s usrName)
        -d delets all content (Ex: gsa -d)
        -v: create new peice of content (Ex: gsa -v contentHashTags [MUST BE SEPARATED BY COMMA NO SPACES])
        -a: add interests to user (Ex: gsa -a usrName interest1,interest2,interest3 [MUST BE SEPARATED BY COMMA NO SPACES])
        -g get a users info (Ex: gsa -g usrName)''')
        elif(args[1] == "-g"):
            print(userManager.GetUserInfo(args[2]))
        else:
            print("command not recognized.")
        return True
    except IndexError:
        return False
