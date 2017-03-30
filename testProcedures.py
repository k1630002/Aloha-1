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
        self.dbPassword = 'root'
        self.dbName = 'mydb'
        self.dbCharSet = 'utf8'
        self.connect()

    def connect(self):
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

    def testProcedure(self):
        #you can put whatever you want from existing procedures
        procedureName = None
        param1 = None
        param2 = None
        param3 = None
        param4 = None
        #......
        params = (param1, param2, param3, param4) #etc. .... put all the params here

        #for example for insert user, it will be:
        username = 'lybomir99100'
        firstname = 'Lyubomir'
        lastname = 'Vasilev'
        email = 'lyubo_bad_boy2000@yahoo.com' #lol
        password = '1234' #so smart
        phone = '0777422352'
        salt = bcrypt.gensalt()
        passwordHashed = bcrypt.hashpw(str(password).encode('utf-8'), salt)
        params = (username, firstname, lastname, email, passwordHashed, phone, salt)
        procedureName = "insertUser"
        self.executeQuery(procedureName, params)

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

    def executeQuery(self, name, params=None):
        try:
            self.cursor.close()
            self.cursor = self.dataBase.cursor()
            self.cursor.callproc(name, params)
            self.dataBase.commit()
        except ImportError as e:
            print json.dumps({"status" : "error", "DataBaseService.executeQuery" : str(e)})
            exit(0)