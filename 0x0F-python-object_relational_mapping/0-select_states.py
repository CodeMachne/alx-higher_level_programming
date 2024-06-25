#!/bin/usr/python3
import MySQLd
import sys

try:
    def states(db_username, password, db_name):
        '''writing a function that script that lists all states from the database hbtn_0e_0_usa
             
             Arguments:
             @db_username: usename to authenticate user
             @password: Password to authenticate user
             @db_name: name of database

             Return:
             return None
        '''
        __databasename__ = hbtn_0e_0_usa

        host = 'localhost'
        port =  3306
        username = db_username
        passwd = password
        database = db_name

        db = connect(host, port, username, passwd, database)

