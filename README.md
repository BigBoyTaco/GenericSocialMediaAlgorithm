# GenericSocialMediaAlgorithm
A small algorithm designed for social media use.

# About
Generic Social Media Algorithm is test peice of software that can decide peices of content to show to a user based off a their interests.

# Future of GSA
Currently, GSA's algorithm isn't very advanced. I plan to make the algorithm more advanced in order to make currated content more relavent to the user. This advanced mode will be a togglable.

# How it works
        1. When creating a peice of content you specify hashtags related to what the content is about. All the folders under \\content\\content are hashtags with content in them, under a hashtag folder is the peice of content with the hash tag. (SUBJECT TO CHANGE) (Ex: \\content\\content\\dogs\\IdOfContent.txt)
        2. After a user is created, you can add interests to the user. When the algorithm is deciding what peice of content it should show to the user it looks for similar interests and hashtags between the user and content.
        3. (NOT IMPLEMENTED) After a user is shown a peice of content they can either like or dislike the peice of content. If the user likes the content the algorithm will pick up on this and show content with this hashtag less.

# Ussage
Commands:

        -h: show this help msg
        -n: create a new user (Ex: gsa -n usrName name birthday email)
        -s: serve content to user (Ex: gsa -s usrName)
        -d delets all content (Ex: gsa -d)
        -v: create new peice of content (Ex: gsa -v contentHashTags [MUST BE SEPARATED BY COMMA NO SPACES])
        -a: add interests to user (Ex: gsa -a usrName interest1,interest2,interest3 [MUST BE SEPARATED BY COMMA NO SPACES])
        -g get a users info (Ex: gsa -g usrName)
# Using the Api:
        ![apiDemoImage](apiDemo.png)
