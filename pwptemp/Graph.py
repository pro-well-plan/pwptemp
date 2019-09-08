import matplotlib.pyplot as plt


def plot_temp_time(finaltime,Tbot,Tout,Tfm):

    # Plotting Tbottom and Tout through time
    plt.plot(range(finaltime), Tbot, 'b', label='Bottom')  # Temp. inside Annulus vs Time
    plt.plot(range(finaltime), Tout, 'r', label='Outlet (Annular)')  # Temp. inside Annulus vs Time
    plt.axhline(y=Tfm[-1], color='k', label='Formation')  # Formation Temp. vs Time
    plt.xlim(0, finaltime - 1)
    plt.xlabel('Time, h')
    plt.ylabel('Temperature, °C')
    plt.legend()  # applying the legend
    plt.show()


def plot_temp_profile(Tdsi,Ta,Tr,Tcsg,Tfm,Tsr,Riser,md,time):

    # Plotting Temperature PROFILE
    plt.plot(Tdsi, md, c='r', label='Fluid in Drill String')  # Temp. inside Drillpipe vs Depth
    plt.plot(Ta, md, 'b', label='Fluid in Annulus')
    if Riser > 0:
        plt.plot(Tr, md, 'g', label='Riser')  # Temp. due to gradient vs Depth
    plt.plot(Tcsg, md, 'c', label='Casing')  # Temp. due to gradient vs Depth
    plt.plot(Tfm, md, 'g', label='Formation')  # Temp. due to gradient vs Depth
    plt.plot(Tsr, md, c='k', ls='-', marker='', label='Surrounding Space')  # Temp. due to gradient vs Depth
    plt.xlabel('Temperature, °C')
    plt.ylabel('Depth, m')
    title = 'Temperature Profile at %i hours' % time
    plt.title(title)
    plt.ylim(plt.ylim()[::-1])  # reversing y axis
    plt.legend()  # applying the legend
    plt.show()


def create_plot(ax, step, mw_riser, md, riser=1):
    """
    Takes in an axis and plots the temperature data from the timestep
    """
    ax.plot(step['Tdsi'], md, c='r', label='Fluid in Drill String')  # Temp. inside Drillpipe vs Depth
    ax.plot(step['Ta'], md, 'b', label='Fluid in Annulus')
    if riser > 0:
        ax.plot(step['Tr'], md, 'g', label='Temp. - Riser')  # Temp. due to gradient vs Depth
    ax.plot(step['Tcsg'], md, 'c', label='Casing')  # Temp. due to gradient vs Depth
    ax.plot(step['Tfm'], md, 'g', label='Formation')  # Temp. due to gradient vs Depth
    ax.plot(step['Tsr'], md, c='k', ls='-', marker='', label='Surrounding Space')  # Temp. due to gradient vs Depth
    return ax


def create_temp_time_plot(ax, finaltime,Tbot,Tout,Tfm):

    # Plotting Tbottom and Tout through time
    ax.plot(range(finaltime), Tbot, 'b', label='Bottom')  # Temp. inside Annulus vs Time
    ax.plot(range(finaltime), Tout, 'r', label='Outlet (Annular)')  # Temp. inside Annulus vs Time
    ax.axhline(y=Tfm[-1], color='k', label='Formation')  # Formation Temp. vs Time
    ax.set_xlim(0, finaltime - 1)
    ax.set_xlabel('Time, h')
    ax.set_ylabel('Temperature, °C')
    ax.legend()  # applying the legend
    return ax