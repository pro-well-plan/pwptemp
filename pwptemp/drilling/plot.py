import matplotlib.pyplot as plt


def behavior(stab_data):

    # Plotting Tbottom and Tout through time
    plt.plot(range(stab_data.finaltime), stab_data.tbot, 'b', label='Bottom')  # Temp. inside Annulus vs Time
    plt.plot(range(stab_data.finaltime), stab_data.tout, 'r', label='Outlet (Annular)')  # Temp. inside Annulus vs Time
    plt.axhline(y=stab_data.tfm[-1], color='k', label='Formation')  # Formation Temp. vs Time
    plt.xlim(0, stab_data.finaltime - 1)
    plt.xlabel('Time, h')
    plt.ylabel('Temperature, °C')
    title = 'Temperature behavior before stabilization (%1.1f hours)' % stab_data.finaltime
    plt.title(title)
    plt.legend()  # applying the legend
    plt.show()


def profile(temp_distribution, sr=False):

    # Plotting Temperature PROFILE
    md = temp_distribution.md
    riser = temp_distribution.riser
    csg = temp_distribution.csgs_reach
    plt.plot(temp_distribution.tdsi, md, c='r', label='Fluid in Drill String')  # Temp. inside Drillpipe vs Depth
    plt.plot(temp_distribution.ta, md, 'b', label='Fluid in Annulus')
    if riser > 0:
        plt.plot(temp_distribution.tr, md, 'g', label='Riser')  # Temp. due to gradient vs Depth
    if csg > 0:
        plt.plot(temp_distribution.tcsg, md, 'c', label='Casing')  # Temp. due to gradient vs Depth
    plt.plot(temp_distribution.tfm, md, 'g', label='Formation')  # Temp. due to gradient vs Depth
    if sr:
        # Temp. due to gradient vs Depth
        plt.plot(temp_distribution.tsr, md, c='k', ls='-', marker='', label='Surrounding Space')
    plt.xlabel('Temperature, °C')
    plt.ylabel('Depth, m')
    title = 'Temperature Profile at %1.1f hours' % temp_distribution.time
    plt.title(title)
    plt.ylim(plt.ylim()[::-1])  # reversing y axis
    plt.legend()  # applying the legend
    plt.show()
