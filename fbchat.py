import fbchat
from getpass import getpass
username = str(input('Username: '))
client = fbchat.Client(username, getpass())
no_of_frn  =int(input('Number of Friend: '))
for i in range(no_of_frn):
    name= str(input('Name: '))
    friend = client.getUsers(name)
    friend = friend[0]
    msg = str(input('Message: '))
    sent = client.send(friend.uid, msg)
    if sent:
        print('Message Sent!!')
