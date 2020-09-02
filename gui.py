from flask import Flask, Response, render_template, Markup, request, redirect
import io
import os
import matplotlib
matplotlib.use('agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from threading import Thread
import datetime
import time
# openpyxl

from data import read_data, plot_data, table_html
# from connect_device import SerialPort

export = False
selected_option = None

app = Flask(__name__)

def read_excel_data():
    global measurements_dict, selected_option
    files = []
    while True:
        _files = [f for f in os.listdir('measurements') if f[-4:] == 'xlsx']

        if _files != files:
            files = _files
            measurements_dict = {}

            for f in files:
                df = read_data('measurements/%s' % f)
                X = df.to_numpy()
                fig = plot_data(X)
                tab, df_tab = table_html(X)
                measurements_dict[f] = [tab, df_tab, fig]
                if selected_option == None:
                    selected_option = f

        time.sleep(1)

def export_excel():
    global export, df_tab
    while True:
        if export:
            measurements_dict[selected_option][1].to_excel('table_summaries/%s' % selected_option)
            export = False
        time.sleep(1)

@app.route('/', methods=['POST', 'GET'])
def index():
    global read, export, selected_option, measurements_dict

    if request.method == 'POST':
        if request.form['button'] == 'Export':
            export = True
        elif request.form['button'] == 'Select':
            selected_option = "%s.xlsx" % request.form.get('measurement')
        return redirect(request.url)
    elif request.method == 'GET':
        keys = [key for key in measurements_dict.keys()]
        return render_template('index.html', table_vals=Markup(measurements_dict[selected_option][0]), measurements_dict=measurements_dict)

@app.route('/plot')
def plot():
    output = io.BytesIO()
    FigureCanvas(measurements_dict[selected_option][2]).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':

    measurements_dict = {}
    read_thread = Thread(target=read_excel_data)
    export_thread = Thread(target=export_excel)
    read_thread.start()

    time.sleep(1)
    export_thread.start()

    app.run()
