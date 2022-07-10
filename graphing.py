import pygal
import datetime

def nameGen():
    return str(datetime.time())

def graph(x, data):
    drawgraph = getattr(pygal, x)
    line_chart = drawgraph()

    i = 0
    for q in data[0]:
        m = []
        for k in data[1:]:
            if k[i] == '':
                continue
            m.append(float(k[i]))
        line_chart.add(q, m)
        i += 1

    name = nameGen()
    line_chart.render_to_file('static/' + name + '.svg')
    return name

if __name__ == "__main__":
    graph(sys.args[1], sys.args[2])
