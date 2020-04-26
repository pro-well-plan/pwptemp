import matplotlib.pyplot as plt


def profile(temp_distribution, tft=True, tt=False, ta=True, tc=False, tr=False, sr=False, units='metric'):

    # Plotting Temperature PROFILE
    md = temp_distribution.md
    riser = temp_distribution.riser
    csg = temp_distribution.csgs_reach
    if tft:
        plt.plot(temp_distribution.tft, md, c='r', label='Fluid in Tubing')  # Temp. inside Tubing vs Depth
    if ta:
        plt.plot(temp_distribution.ta, md, 'b', label='Fluid in Annulus')  # Temp. of annulus
    if riser > 0 and tr:
        plt.plot(temp_distribution.tr, md, 'g', label='Riser')  # Temp. due to gradient vs Depth
    if csg > 0:
        plt.plot(temp_distribution.tc, md, 'c', label='Casing')  # Temp. due to gradient vs Depth
    if tc:
        plt.plot(temp_distribution.tc, md, 'c', label='Casing')  # Temp. of first casing layer vs Depth
    plt.plot(temp_distribution.tfm, md, color='k', label='Formation')  # Temp. due to gradient vs Depth
    if tt:
        plt.plot(temp_distribution.tt, md, color='k', label='Tubing')  # Temp. of Tubing wall vs Depth
    if sr:
        # Temp. due to gradient vs Depth
        plt.plot(temp_distribution.tsr, md, c='0.6', ls='-', marker='', label='Surrounding Space')
    if units == 'metric':
        plt.xlabel('Temperature, °C')
        plt.ylabel('Depth, m')
    else:
        plt.xlabel('Temperature, °F')
        plt.ylabel('Depth, ft')
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


def profile_multitime(temp_dist, values, times, tft=True, ta=False, tr=False, tc=False, tfm=True, tsr=False):
    md = temp_dist.md
    riser = temp_dist.riser
    csg = temp_dist.csgs_reach
    if tfm:
        plt.plot(values[0].tfm, md, color='k', label='Formation - Initial')  # Temp. due to gradient vs Depth

    color = ['r', 'b', 'g', 'c', '0.4', '0.9', '0.6', '0.8', '0.2', 'r', 'b', 'g', 'c', '0.4', '0.9', '0.6', '0.8']
    if len(values) > len(color):
        color = color * round((len(values) / len(color)))
    for x in range(len(values)):
        # Plotting Temperature PROFILE
        if tft:
            plt.plot(values[x].tft, md, c=color[x], label='Fluid in Tubing at %1.1f hours' % times[x])
        if ta:
            plt.plot(values[x].ta, md, c=color[x], label='Fluid in Annulus at %1.1f hours' % times[x])
        if riser > 0 and tr:
            plt.plot(values[x].tr, md, c=color[x], label='Riser at %1.1f hours' % times[x])
        if csg > 0 and tc:
            plt.plot(values[x].tc, md, c=color[x], label='Casing at %1.1f hours' % times[x])
        if tsr:
            # Temp. due to gradient vs Depth
            plt.plot(values[x].tsr, md, c=color[x], ls='-', marker='', label='Surrounding Space')
    plt.xlabel('Temperature, °C')
    plt.ylabel('Depth, m')
    title = 'Temperature Profiles'
    plt.title(title)
    plt.ylim(plt.ylim()[::-1])  # reversing y axis
    plt.legend()  # applying the legend
    plt.show()