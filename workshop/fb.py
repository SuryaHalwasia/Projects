import fbchat
from getpass import getpass
user=input("Enter your username")
client=fbchat.Client(user,getpass())
print(fbchat.client(user))
'''no=int(input("Enter the number of friends"))
for i in range(no):
    name=input("name")
    friend=fbchat.ClientsearchForUsers(name)
    friends=friend[0]
    mgs=input("msg")
    sent=client.send(friend.uid,msg)'''
    
