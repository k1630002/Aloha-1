#!/usr/bin/python

import os
import sys
import MySQLdb
import MySQLdb.cursors
import json
import bcrypt
from time import gmtime, strftime

class DataBaseService:
    def __init__(self):
        self.dbHost = '127.0.0.1'
        self.dbPort = 3306
        self.dbUser = 'root'
        self.dbPassword = self.getInfoFromFile("password")
        self.dbName = self.getInfoFromFile("dbName")
        self.dbCharSet = 'utf8'
        self.connectDB()

    def connectDB(self):
        try:
            self.dataBase = MySQLdb.connect (host    = self.dbHost,
                                           port    = self.dbPort,
                                           user    = self.dbUser,
                                           passwd  = self.dbPassword,
                                           db      = self.dbName,
                                           charset = self.dbCharSet)
            self.cursor = self.dataBase.cursor()

        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.connect" : str(e)})
            exit(0)

    def getInfoFromFile(self, filename):
        if os.path.isfile(filename):
            f = open(filename, 'r')
            return f.read()
        return False

    def executeQuery(self, name, params=None):
        try:
            self.cursor.close()
            self.cursor = self.dataBase.cursor()
            self.cursor.callproc(name, params)
            self.dataBase.commit()
        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.executeQuery" : str(e)})
            exit(0)

    def fetchData(self, query, params=None):
        result = None
        try:
            self.cursor.close()
            self.cursor = self.dataBase.cursor()
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.fetchData" : str(e)})
            exit(0)

    def insertUser(self, username, firstname, lastname, password, phone, email):
        try:
            salt = bcrypt.gensalt()
            passwordHashed = bcrypt.hashpw(str(password).encode('utf-8'), salt)
            settingId = 1
            params = (username, firstname, lastname, email, passwordHashed, phone, salt)
            name = "insertUser"
            self.executeQuery(name, params)
        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.insertUser" : str(e)})
            exit(0)

    def authenticate(self, username, enteredPassword):
        try:
            salt = self.getSalt(username)
            passwordHashed = bcrypt.hashpw(enteredPassword, salt)
            passwordDB = self.getHashedPasswordDB(username)
            if passwordDB == passwordHashed:
                return True
            else:
                return False

        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.authenticate" : str(e)})
            exit(0)

    def createFriendship(self, username1, username2):
        try:
            userID1 = self.getUserID(username1)
            userID2 = self.getUserID(username2)
            params = (userID1, userID2)
            name = "createFriendship"
            self.executeQuery(name, params)
        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.createFriendship" : str(e)})
            exit(0)

    def getSalt(self, username):
        try:
            query = "SELECT salt         \
               FROM user_view \
               WHERE username='" + username + "'"
            return self.fetchData(query, None)[0][0]
        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.getSalt" : str(e)})
            exit(0)

    def getHashedPasswordDB(self, username):
        try:
            query = "SELECT password         \
               FROM user_view \
               WHERE username='" + username + "'"
            return self.fetchData(query, None)[0][0]
        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.getHashedPasswordDB" : str(e)})
            exit(0)

    def getUserID(self, username):
        try:
            query = "SELECT id         \
               FROM user_view \
               WHERE username='" + username + "'"
            return self.fetchData(query, None)[0][0]
        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.getUserID" : str(e)})
            exit(0)

    def sendMessage(self, sender, receiver, text):
        try:
            senderID = self.getUserID(sender)
            receiverID = self.getUserID(receiver)
            currentTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            params = (senderID, receiverID, text, currentTime)
            procName = "sendMessage"
            self.executeQuery(procName, params)
        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.getUserID" : str(e)})
            exit(0)

