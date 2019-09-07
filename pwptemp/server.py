import io

from flask import Flask, Response, render_template, session, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
# from matplotlib.figure import Figure

from Graph import create_plot, create_temp_time_plot
from Input import WellTemperature, temp_dict
from Main import temp_time, stab_time
from WellPath import wellpath

app = Flask(__name__)
app.secret_key = b'\xba\x1d\x88\x98\xa0\x06\xce\x98g\x1d\xd4s\x81\x92@\xc6'

@app.route('/', methods=['GET', 'POST'])
def show_temp_plot():
    """
    Renders template which calls for figure
    """
    if request.method == 'POST':
            steps=request.form['timesteps']
            session['timesteps']=[float(n) for n in steps.split(',')]
    if 'timesteps' not in session:
        session['timesteps'] = [6]
    if 'show_variables' not in session:
        session['show_variables'] = True
    return render_template('plot.html', timesteps = session['timesteps'], show_variables = session['show_variables'], variables=temp_dict)

@app.route('/plot.png')
def depth_profile():
    """
    Creates figure and returns to template
    """
    fig = plot_depth_profile()
    return return_figure(fig)


@app.route('/stab_plot.png')
def time_profile():
    """
    Creates the temperature vs time plot
    """
    well, md, tvd, deltaz, zstep = create_default_well()
    
    Tdsi, Ta, Tr, Tcsg, Tsr, Tfm, time = temp_time(5, well, tvd, deltaz, zstep)
    
    finaltime, Tbot, Tout = stab_time(well, tvd, deltaz, zstep)

    fig = plt.figure(dpi=150)
    axis=fig.add_subplot(1,1,1)

    create_temp_time_plot(axis,finaltime,Tbot,Tout,Tfm)
    return return_figure(fig)

def plot_depth_profile():
    """
    Loads dataset and create Matplotlib figure using create_ax from Graph library
    """
    well, md, tvd, deltaz, zstep = create_default_well()
    res = []
    for time in session['timesteps']:
        Tdsi,Ta,Tr,Tcsg,Tsr,Tfm, time = temp_time(time,well,tvd,deltaz,zstep)
        res.append(dict(Tdsi=Tdsi,Ta=Ta,Tr=Tr,Tcsg=Tcsg,Tsr=Tsr,Tfm=Tfm))

    fig = plt.figure(dpi=150)
    axis=fig.add_subplot(1,1,1)

    for step in res:
        create_plot(axis, step,well.riser, md)
    axis.set_ylim(axis.get_ylim()[::-1])  # reversing y axis
    axis.legend()
    return fig

def create_default_well():
    tdata=temp_dict 
    well=WellTemperature(tdata)
    md,tvd,deltaz,zstep=wellpath(well.mdt)  # Getting depth values
    return well, md, tvd, deltaz, zstep

def return_figure(fig):
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
