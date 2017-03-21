#! /usr/bin/python
import json
from DataBaseService import DataBaseService

class APIManager:
    def __init__(self):
        self.db = DataBaseService()
    def registerNewClient(self, info):
        try:
            newUserData = json.loads(info)
            username = newUserData['username']
            firstName = newUserData['firstname']
            lastName = newUserData['lastname']
            password = newUserData['password']
            phone = newUserData['mobile']
            email = newUserData['email']
            print ( username + firstName )
            self.db.insertUser(username, firstName, lastName, password, phone, email)
        except ImportError as e:
            print json.dumps({"status" : "error", "APIManager.registerNewClient" : str(e)})
            exit(0)

    def authenticate(self, userData):
        try:
            '''name = userData['username']
            passwordEntered = userData['password']'''
            name = 'ionut'
            passwordEntered = 'aloha2'
            res = self.db.authenticate(name, passwordEntered)
            print res
        except ImportError as e:
            print json.dumps({"status" : "error", "APIManager.registerNewClient" : str(e)})
            exit(0)

    def createFriendship(self, friendData):
        try:
            '''friendUsername = userData['username']
               ownUsername = myUsername'''
            ownUsername = 'alex93'
            friendUsername = 'lyubo93'
            self.db.createFriendship(ownUsername, friendUsername)
        except ImportError as e:
            print json.dumps({"status" : "error", "APIManager.registerNewClient" : str(e)})
            exit(0)

    def sendMessage(self, messageData):
        try:
            '''sender = messageData['sender']
            receiver = messageData['receiver']
            message = messageData['message'] '''
            sender = 'alex93'
            receiver = 'lyubo93'
            message = 'Hi Lyubomir!'
            self.db.sendMessage(sender, receiver, message)
        except ImportError as e:
            print json.dumps({"status" : "error", "APIManager.registerNewClient" : str(e)})
            exit(0)
