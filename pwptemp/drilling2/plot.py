import plotly.graph_objects as go


def plot_distribution(temp_distribution, operation='drilling'):
    pipe_name = {'drilling': 'Drill String',
                 'production': 'Production Tubing',
                 'injection': 'Injection Tubing'}

    # Plotting Temperature PROFILE

    fig = go.Figure()
    md = temp_distribution.temperatures['md']
    riser = temp_distribution.riser_cells
    csg = temp_distribution.casings[0, 2]

    fig.add_trace(go.Scatter(x=temp_distribution.temperatures['in_pipe'], y=md,
                             mode='lines',
                             name='Fluid in ' + pipe_name[operation]))

    fig.add_trace(go.Scatter(x=temp_distribution.temperatures['annulus'], y=md,
                             mode='lines',
                             name='Fluid in Annulus'))

    if riser > 0:
        fig.add_trace(go.Scatter(x=temp_distribution.temperatures['riser'], y=md,
                                 mode='lines',
                                 name='Riser'))
    if csg > 0:
        fig.add_trace(go.Scatter(x=temp_distribution.temperatures['casing'], y=md,
                                 mode='lines',
                                 name='Casing'))
    fig.add_trace(go.Scatter(x=temp_distribution.temperatures['formation'], y=md,
                             mode='lines',
                             name='Formation'))  # Temp. due to gradient vs Depth

    fig.update_layout(
        xaxis_title='Temperature, °C',
        yaxis_title='Depth, m')

    title = 'Temperature Profile at %1.1f hours' % temp_distribution.time + ' of ' + operation
    fig.update_layout(title=title)

    fig.update_yaxes(autorange="reversed")

    return fig


def plot_behavior(temp_behavior, title=True):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=temp_behavior.time, y=temp_behavior.bottom, mode='lines', name='Bottom'))
    fig.add_trace(go.Scatter(x=temp_behavior.time, y=temp_behavior.outlet, mode='lines', name='Outlet - annulus'))
    fig.add_trace(go.Scatter(x=temp_behavior.time, y=temp_behavior.max, mode='lines', name='Max. temp'))
    fig.add_trace(go.Scatter(x=temp_behavior.time, y=temp_behavior.formation_td, mode='lines', name='Formation at TD'))
    fig.update_layout(
        xaxis_title='time, h',
        yaxis_title='Temperature, °C')
    if title:
        fig.update_layout(title=str(temp_behavior.time[-1]) + ' hours of operation')

    return fig
