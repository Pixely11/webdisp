import sys
import extract, graphing
from bottle import route, run, template, static_file

data = []
topbar = 0
graphs = []

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
def home():
    return template('home', data=data, topbar=topbar, graphs=graphs)

def initialize(filepath, graphinput = ['Line', 0], topbarinput = 0):
    global data, topbar, graphs
    data = extract.main(filepath) # input('file-path: ')
    topbar = int(topbarinput)
    graphs = []

    for i in range(0, len(graphinput), 2):
        graphs.append(graphing.graph(graphinput[i], data[graphinput[i+1]]))

    if type(data) == str:
        print('ERROR: ' + data)
        sys.exit()
    elif type(topbar) != int:
        print('ERROR: topbar is ' + str(type(topbar)) + ', needed type int')
        sys.exit()
    else:
        run(host='localhost', port=8080)

#initialize(sys.argv[1], [sys.argv[2], 0, sys.argv[3], 0]) # not: topbar not finished
initialize(sys.argv[1]) # not: topbar not finished
