from flask import Flask, Response, render_template, Markup, request, redirect
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from threading import Thread
import datetime
# openpyxl

from data import read_data, plot_data, table_html

export = False
read = False

app = Flask(__name__)

def read_bt():
    global tab, df_tab, read
    while True:
        if read:
            data_df, data_np = connect_bt_serial()

            fig = plot_data(data)
            tab, df_tab = table_html(data)
            read = False
            # return tab, df_tab

def export_excel():
    global export, df_tab
    while True:
        if export:
            df_tab.to_excel('messung.xlsx')
            export = False

@app.route('/', methods=['POST', 'GET'])
def index():
    global read, export

    if request.method == 'POST':
        if request.form['button'] == 'Neu':
            read = True
        elif request.form['button'] == 'Export':
            export = True
        return redirect(request.url)
    elif request.method == 'GET':
        return render_template('index.html', table_vals=Markup(tab))

@app.route('/plot')
def plot():
    # fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    fname = 'Beispielwerte aus einer Messung'
    df = read_data(fname)
    X = df.to_numpy()
    fig = plot_data(X)
    tab, df_tab = table_html(X)
    
    # read_thread = Thread(target=read_bt)
    # export_thread = Thread(target=export_excel)
    # read_thread.start()
    # export_thread.start()

    app.run()
