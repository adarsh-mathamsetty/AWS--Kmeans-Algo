import csv
import os
from flask import Flask, request, redirect, url_for,render_template,flash
from time import time
import numbers
import re
from scipy.cluster.vq import *
from random import *
import numpy

app = Flask(__name__)
app.secret_key = 'checkmate test'




regDigit = m = re.compile("^\\-{0,1}\d+\\.{0,1}\d*$")  

csvfname = "quakes"
regexused = regDigit;

regex = re.compile("^\\-{0,1}\d+\\.{0,1}\d*$")


def loadData(a1,a2):
    x,y = 0,0
    c = 0
    data = []
    csvfile = csv.reader(open('/home/ubuntu/flaskapp/' + csvfname + '.csv', 'U'), dialect="excel")
    csvfile.next()
    for t in csvfile:
        c+=1
        x =  t[a1] if regex.match(t[a1]) else 0
        y =  t[a2] if regex.match(t[a2]) else 0
        data.append([float(x),float(y)])
        # if (c == 1000):
        #     break
    return data


@app.route('/')
def hello_world():
    return render_template('index.html')





@app.route('/exec_query',methods=['GET','POST'])
def query():
	a1 = int(request.form['att1'])
    	a2 = int(request.form['att2'])
    	clusters = int(request.form['clusters'])
    	data = loadData(a1,a2)
    	c,l = kmeans2(data,clusters,minit='random')
    	num = []
    	listc = l.tolist()
    	for x in range(0,len(c)):
        num.append(listc.count(x))

    return render_template('query.html',data = num)




if  __name__ == '__main__':
    app.run()
