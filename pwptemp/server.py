from flask import Flask, render_template, Response
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from Input import WellTemperature, temp_dict
from WellPath import wellpath
from Main import temp_time
from Graph import create_plot

app = Flask(__name__)

@app.route('/')
def show_temp_plot():
    """
    Renders template which calls for figure
    """
    return render_template('plot.html', timesteps = [.1,.2,.5,1])

@app.route('/plot.png')
def plot_png():
    """
    Creates figure and returns to template
    """
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    """
    Loads dataset and create Matplotlib figure using create_ax from Graph library
    """
    tdata=temp_dict 
    mw=WellTemperature(tdata)  

    md,tvd,deltaz,zstep=wellpath(mw.mdt)  # Getting depth values

    res = []
    for time in [.1,.2,.5,1]:
        Tdsi,Ta,Tr,Tcsg,Tsr,Tfm = temp_time(time,mw,tvd,deltaz,zstep)
        res.append(dict(Tdsi=Tdsi,Ta=Ta,Tr=Tr,Tcsg=Tcsg,Tsr=Tsr,Tfm=Tfm))

    fig = Figure(dpi=150)
    axis=fig.add_subplot(1,1,1)

    for step in res:
        create_plot(axis, step, mw.riser, md)
    axis.set_ylim(axis.get_ylim()[::-1])  # reversing y axis
    axis.legend()
    return fig