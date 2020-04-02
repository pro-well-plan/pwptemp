import matplotlib.pyplot as plt


def profile(temp_distribution, sr=False):

    # Plotting Temperature PROFILE
    md = temp_distribution.md
    riser = temp_distribution.riser
    csg = temp_distribution.csgs_reach
    plt.plot(temp_distribution.tft, md, c='r', label='Fluid in Drill String')  # Temp. inside Tubing vs Depth
    plt.plot(temp_distribution.ta, md, 'b', label='Fluid in Annulus')  # Temp. of annulus
    if riser > 0:
        plt.plot(temp_distribution.tr, md, 'g', label='Riser')  # Temp. due to gradient vs Depth
    if csg > 0:
        plt.plot(temp_distribution.tc, md, 'c', label='Casing')  # Temp. due to gradient vs Depth
    plt.plot(temp_distribution.tc, md, 'c', label='Casing')  # Temp. of first casing layer vs Depth
    plt.plot(temp_distribution.tfm, md, color='k', label='Formation')  # Temp. due to gradient vs Depth
    plt.plot(temp_distribution.tt, md, color='k', label='Tubing')  # Temp. of Tubing wall vs Depth
    if sr:
        # Temp. due to gradient vs Depth
        plt.plot(temp_distribution.tsr, md, c='0.6', ls='-', marker='', label='Surrounding Space')
    plt.xlabel('Temperature, °C')
    plt.ylabel('Depth, m')
    title = 'Temperature Profile at %1.1f hours' % temp_distribution.time
    plt.title(title)
    plt.ylim(plt.ylim()[::-1])  # reversing y axis
    plt.legend()  # applying the legend
    plt.show()


def behavior(Behavior):

    # Plotting Tbottom and Tout through time
    plt.plot(range(Behavior.finaltime), Behavior.tout, 'r', label='Outlet (Tubing)')  # Temp. outlet vs Time
    plt.axhline(y=Behavior.tfm[-1], color='k', label='Formation')  # Formation Temp. vs Time
    plt.xlim(0, Behavior.finaltime - 1)
    plt.xlabel('Time, h')
    plt.ylabel('Temperature, °C')
    title = 'Temperature behavior (%1.1f hours)' % Behavior.finaltime
    plt.title(title)
    plt.legend()  # applying the legend
    plt.show()