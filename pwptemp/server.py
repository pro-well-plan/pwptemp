import io

from flask import Flask, Response, render_template, session, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from Graph import create_plot
from Input import WellTemperature, temp_dict
from Main import temp_time
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
    for time in session['timesteps']:
        Tdsi,Ta,Tr,Tcsg,Tsr,Tfm = temp_time(time,mw,tvd,deltaz,zstep)
        res.append(dict(Tdsi=Tdsi,Ta=Ta,Tr=Tr,Tcsg=Tcsg,Tsr=Tsr,Tfm=Tfm))

    fig = Figure(dpi=150)
    axis=fig.add_subplot(1,1,1)

    for step in res:
        create_plot(axis, step, mw.riser, md)
    axis.set_ylim(axis.get_ylim()[::-1])  # reversing y axis
    axis.legend()
    return fig
