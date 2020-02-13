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
    plt.plot(temp_distribution.tfm, md, color='k', label='Formation')  # Temp. due to gradient vs Depth
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


def profile_multitime(temps, tdsi=True, ta=False, tr=False, tcsg=False, tfm=True, tsr=False):
    md = temps.values[0].md
    riser = temps.values[0].riser
    csg = temps.values[0].csgs_reach
    if tfm:
        plt.plot(temps.values[0].tfm, md, color='k', label='Formation - Initial')  # Temp. due to gradient vs Depth

    color = ['r', 'b', 'g', 'c', '0.4', '0.9', '0.6', '0.8', '0.2']
    if len(temps.values) > len(color):
        color = color * round((len(temps.values) / len(color)))
    for x in range(len(temps.values)):
        # Plotting Temperature PROFILE
        if tdsi:
            plt.plot(temps.values[x].tdsi, md, c=color[x], label='Fluid in Drill String at %1.1f hours' % temps.times[x])
        if ta:
            plt.plot(temps.values[x].ta, md, c=color[x], label='Fluid in Annulus at %1.1f hours' % temps.times[x])
        if riser > 0 and tr:
            plt.plot(temps.values[x].tr, md, c=color[x], label='Riser at %1.1f hours' % temps.times[x])
        if csg > 0 and tcsg:
            plt.plot(temps.values[x].tcsg, md, c=color[x], label='Casing at %1.1f hours' % temps.times[x])
        if tsr:
            # Temp. due to gradient vs Depth
            plt.plot(temps.values[x].tsr, md, c=color[x], ls='-', marker='', label='Surrounding Space')
    plt.xlabel('Temperature, °C')
    plt.ylabel('Depth, m')
    title = 'Temperature Profiles'
    plt.title(title)
    plt.ylim(plt.ylim()[::-1])  # reversing y axis
    plt.legend()  # applying the legend
    plt.show()
