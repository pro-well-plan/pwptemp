import plotly.graph_objects as go
from numpy import polyfit, poly1d


def profile(temp_distribution, units='metric', operation='drilling'):

    pipe_name = {'drilling': 'Drill String',
                 'production': 'Production Tubing',
                 'injection': 'Injection Tubing'}

    # Plotting Temperature PROFILE

    fig = go.Figure()
    md = temp_distribution.md
    if units == 'english':
        md = [i * 3.28 for i in md]
    riser = temp_distribution.riser
    csg = temp_distribution.csgs_reach

    if operation == 'drilling':
        pipe_fluid = temp_distribution.tdsi

    else:
        pipe_fluid = temp_distribution.tft

    fig.add_trace(go.Scatter(x=pipe_fluid, y=md,
                             mode='lines',
                             name='Fluid in ' + pipe_name[operation]))
    fig.add_trace(go.Scatter(x=temp_distribution.ta, y=md,
                             mode='lines',
                             name='Fluid in Annulus'))

    if riser > 0:
        fig.add_trace(go.Scatter(x=temp_distribution.tr, y=md,
                                 mode='lines',
                                 name='Riser'))
    if csg > 0:
        fig.add_trace(go.Scatter(x=temp_distribution.tcsg, y=md,
                                 mode='lines',
                                 name='Casing'))
    fig.add_trace(go.Scatter(x=temp_distribution.tfm, y=md,
                             mode='lines',
                             name='Formation'))  # Temp. due to gradient vs Depth

    if units == 'metric':
        fig.update_layout(
            xaxis_title='Temperature, °C',
            yaxis_title='Depth, m')
    else:
        fig.update_layout(
            xaxis_title='Temperature, °F',
            yaxis_title='Depth, ft')

    title = 'Temperature Profile at %1.1f hours' % temp_distribution.time + ' of ' + operation
    fig.update_layout(title=title)

    fig.update_yaxes(autorange="reversed")

    return fig


def behavior(Behavior, operation='drilling'):
    """
    Plotting Tbottom and Tout through time
    """

    fig = go.Figure()

    time = Behavior.time

    if Behavior.finaltime <= 10:
        poly_order = 2
    else:
        poly_order = 10

    if operation == 'drilling' or operation == 'injection':
        tbot_smooth = polyfit(time, Behavior.tbot, poly_order)
        tbot = poly1d(tbot_smooth)(time)
        fig.add_trace(go.Scatter(x=time, y=tbot,
                                 mode='lines',
                                 name='Bottom'))    # Temp. Bottom vs Time

    if operation == 'drilling' or operation == 'production':
        tout_smooth = polyfit(time, Behavior.tout, poly_order)
        tout = poly1d(tout_smooth)(time)
        fig.add_trace(go.Scatter(x=time, y=tout,
                                 mode='lines',
                                 name='Outlet'))    # Temp. Oulet vs Time

    fig.add_trace(go.Scatter(x=time, y=[Behavior.tfm[-1]]*len(time),
                             mode='lines',
                             name='Formation @ TD'))  # Formation Temp. vs Time

    fig.update_layout(
        xaxis_title='Time, h',
        yaxis_title='Temperature, °C')

    title = 'Temperature behavior (%1.1f hours)' % Behavior.finaltime + ' Operation: ' + operation
    fig.update_layout(title=title)

    return fig
