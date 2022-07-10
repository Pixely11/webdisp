# supports csv, json, sqlitedb, markdown or latex
# tabularform, piechart, graph, images(image modifiers)

import csv
import sqlite3
import json

# illegal function (note: printing in functions is not encouraged)
def printdata(data):
    for i in data:
        for j in i:
            print(str(j), end=' ')
        print(end='\n')

def unpacker(k, keys, values):
    for j in k:
        for i in j:
            if type(j[i]) == list:
                keys.append(i)
                keys.append([])
                unpacker(j[i], keys[-1], values)
            else:
                keys.append(i)
                values.append(j[i])

def main(path):
    supportedfiletypes = ['csv', 'json', 'md', 'tex', 'pdf']
    name, ext = path.split('.', 1) # assumes no '.' in path besides extention

    if ext == 'csv':
        with open(path, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        #printdata(data)
        return [data] 

    elif ext == 'db':
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [i[0] for i in cursor.fetchall()]
        data = []
        
        for i in tables:
            data.append([])
            a = conn.execute('select * from ' + i)
            columns = [j[0] for j in a.description]
            data[-1].append(columns)
            for j in a.fetchall():
                data[-1].append(list(j))
        
        conn.close()
        
#        print(data)
        return data

    elif ext == 'json':
        keys = []
        values = []

        with open(path, 'r') as f:
            data = json.load(f)

        unpacker([data], keys, values)
        return [[keys, values]]

    else:
        return "filetype not supported, supported filetypes: " + repr(supportedfiletypes)

if __name__ == "__main__":
    import sys
    print(main(sys.argv[1])) #input("file_path: ")
