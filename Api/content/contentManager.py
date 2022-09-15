from asyncore import write
import os, random, shutil
#returns available content
def getAvalableContent():
    return os.listdir(os.getcwd() + "/content/content")

#creates new content
def createContent(hashtags):
    id = random.randint(0, 98987878787674456655654247645643982826242322214192)
    #for every hashtag write a content file
    for i in hashtags:
        if i in getAvalableContent():
            with open("content/content/" + i + '/' + str(id) + ".meta", "a") as f:
                for h in hashtags:
                    f.write("#" + h + "\n")
        else:
            os.makedirs("content/content/" + i)
            with open("content/content/" + i + '/' + str(id) + ".meta", "a") as f:
                for h in hashtags:
                    f.write("#" + h + "\n")
    print('created content with the id of: ' + str(id), 'and the tags of', hashtags)

def delAllContent():
    yn = input("WARING are you sure you want to delete all content (y/n) ")
    if yn == "y":
        shutil.rmtree(os.getcwd() + "/content/content")
        os.makedirs(os.getcwd() + "/content/content")
        print("all content successfully deleted.")
    else:
        print("operation canceled.")
