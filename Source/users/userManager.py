import json, os

def createUser(usrName, name, birthday, email):
    try:
        os.makedirs(os.getcwd() + "\\users\\users")
    except:
        pass
    print("Creating", usrName + "'s account...")
    x = {
        "userName": usrName,
        "name": name,
        "birthday": birthday,
        "email": email,
        "interests": []
    }
    # Serializing json/ convert dict to json
    json_object = json.dumps(x, indent=4)
    # Writing to file
    with open("users\\users\\" + usrName + ".json", "w") as outfile:
        outfile.write(json_object)
    print("completed.")

def addInterest(user, interests):
    print("Adding interests to", user + "'s account...")
    with open("users\\users\\" + user + ".json", "r") as f:
        # Reading from json file
        userJson = json.load(f)
    #add new interests
    interests = interests.split(",")
    tmp = userJson.get("interests") + interests
    userJson.__setitem__("interests", tmp)
    #convert dict to json
    json_object = json.dumps(userJson, indent=4)
    # Writing to file
    with open("users\\users\\" + user + ".json", "w") as outfile:
        outfile.write(json_object)

#returns user info
def GetUserInfo(usrName):
    with open("users\\users\\" + usrName + ".json", "r") as f:
        # Reading from json file
        return json.load(f)
