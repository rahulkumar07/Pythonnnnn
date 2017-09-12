# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def index(request):
    x=5
    usernameloggedin='usertst'
    directorytmp='/Users/NeeruRohilla/pypr/olmstest/olmswebapp/tmp/' + usernameloggedin;
    if not os.path.exists(directorytmp):
        os.makedirs(directorytmp)
    z=os.system("javac %s/Test.java 2> %s/Test.err" % (directorytmp, directorytmp))
    y=os.system("java -classpath '/Users/NeeruRohilla/pypr/olmstest/olmswebapp' Test ")
    return HttpResponse("Hello, world. You're at the polls index."+"new"+str(z))
