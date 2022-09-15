from content import contentManager
from data import algorithm
from users import userManager

def createUsr(usrName, name, birthday, email):
    userManager.createUser(usrName, name, birthday, email)

def contentRequest(user):
    algorithm.contentRequest(user)

def addInterest(user, interests):
    userManager.addInterest(user, interests)

def createContent(tags):
    contentManager.createContent(tags)

def delAllContent():
    contentManager.delAllContent()
