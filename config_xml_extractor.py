#!/usr/bin/python
import os
import sys
from sys import argv
from os.path import exists
import re
from collections import deque
from itertools import chain

FLAG = "OFF"
mylist = []
repo = {}
parents = []
servername = ""
# Testing the Startup Arguments for the script
if not (len(argv) > 1 ):
        print "Argument is must"
        sys.exit()

filename = argv[1].rstrip();

if exists(filename):
        #with open(filename,"r+") as fo
        fo = open(filename,"r+")
        os.system("clear")
        print "..Reading the file..",filename
        filecontent = fo.readlines()
        for str in filecontent:
                #print " Processing Line: \n",str
                match1 = re.search(r'\<server\>', str)
                if match1:
                        #print str
                        FLAG = "ON"
                match2 = re.search(r'\<\/server\>', str)
                if match2:
                        #print str
                        FLAG = "OFF"
                        #print str.strip()
                        mylist.append(str.strip())
                if (FLAG == "ON"):
                        #print str.strip()
                        mylist.append(str.strip())
        fo.close()
else:
        print "File is not present"
        sys.exit()


elements={}

class parent(object):
        def addelement(self,key,value):
                self.__dict__[key]=value


servers=[]
class server(object):
        def addelement(self,key,value):
                self.__dict__[key]=value

mode="parent"
print "------------------------------------------------------------"
try:

        for line in mylist:

                if re.search(r'(^\<)(.+)(\>)(.+)(\<\/)(.+)(\>)',line):
                        mode="child"
                        match=re.search(r'(^\<)(.+)(\>)(.+)(\<\/)(.+)(\>)',line)
                        if match:
                                if not ( "/" in root ):
                                        print root+"_"+match.group(2),":", match.group(4)
                                        elements[root].addelement(match.group(2),match.group(4)) #adding new element to the dict
                                        key=root+"_"+match.group(2)
                                        repo[key]=match.group(4)
                                else:
                                        print "DID IT EVER COME HERE"
                                        root = root.split("/")[1].strip()
                                        print root+"_"+match.group(2),":", match.group(4)
                                        elements[root].addelement(match.group(2),match.group(4)) #adding new element to the dict
                                        key=root+"_"+match.group(2)
                                        repo[key]=match.group(4)



                elif re.search(r'(^\<)(.+)(\>)(\<\/)(.+)(\>)',line):
                        mode="child"
                        match=re.search(r'(^\<)(.+)(\>)(\<\/)(.+)(\>)',line)
                        if match:
                                if not ( "/" in root ):
                                        print root+"_"+match.group(2),": NO VALUE"
                                        elements[root].addelement(match.group(2),"NO VALUE")
                                        key=root+"_"+match.group(2)
                                        repo[key]="NO VALUE"

                                else:
                                        root = root.split("/")[1].strip()
                                        print root+"_"+match.group(2),": NO VALUE"
                                        elements[root].addelement(match.group(2),"NO VALUE")
                                        key=root+"_"+match.group(2)
                                        repo[key]="NO VALUE"


                elif re.search(r'(^\<|^\<\/)(.+)(\>$)',line):
                        mode="parent"
                        match=re.search(r'(^\<)(.+)(\>)',line)
                        if match:
                                if not "/" in match.group(2) :
                                        mode = "child"
                                        root=match.group(2)
                                        parents.append(root)
                                        #print "ADDED NEW ELEMENT", parents
                                else:
                                        root=match.group(2)
                                        mode = "child"
                                        tmpstr=match.group(2).split("/")[1]
                                        #print tmpstr;
                                        if tmpstr in parents:
                                                parents.remove(tmpstr)
                                                #print "REMOVED ELEMENT", parents
                                                #print parents
                                                if len(parents) > 0:
                                                        root=parents[len(parents)-1]
                        if root not in elements.keys():
                                #print "Adding new element object", root
                                elements[root] = parent()
                        if root == "/server":
                                if "server_name" in repo.keys():
                                        print "----------------------------------------------------------"
                                        #servername=repo['server_name']
                                        servers.append(repo.copy())
                                        #print "DEBUG==>",servers[len(servers)-1]['server'].name
                                        #print '{"'+repo['server_name']+":['"
                                        #for entry in servers:
                                                #print entry
                                                #print
                                        #print ']}'
                        #if repo['server_name']:
                                #root=repo['server_name']


except IndexError:
        print "- "

print "----------------------------------------------------------"
'''

