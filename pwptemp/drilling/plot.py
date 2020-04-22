import matplotlib.pyplot as plt


def behavior(Behavior):

    # Plotting Tbottom and Tout through time
    plt.plot(range(Behavior.finaltime), Behavior.tbot, 'b', label='Bottom')  # Temp. inside Annulus vs Time
    plt.plot(range(Behavior.finaltime), Behavior.tout, 'r', label='Outlet (Annular)')  # Temp. inside Annulus vs Time
    plt.axhline(y=Behavior.tfm[-1], color='k', label='Formation')  # Formation Temp. vs Time
    plt.xlim(0, Behavior.finaltime - 1)
    plt.xlabel('Time, h')
    plt.ylabel('Temperature, °C')
    title = 'Temperature behavior (%1.1f hours)' % Behavior.finaltime
    plt.title(title)
    plt.legend()  # applying the legend
    plt.show()


def profile(temp_distribution, tdsi=True, ta=True, tr=False, tcsg=False, tfm=True, sr=False):

    # Plotting Temperature PROFILE
    md = temp_distribution.md
    riser = temp_distribution.riser
    csg = temp_distribution.csgs_reach
    if tdsi:
        plt.plot(temp_distribution.tdsi, md, c='r', label='Simulated - DP')  # Temp. inside Drillpipe vs Depth
    if ta:
        plt.plot(temp_distribution.ta, md, 'b', label='Simulated - Ann')
    if riser > 0 and tr:
        plt.plot(temp_distribution.tr, md, 'g', label='Riser')  # Temp. due to gradient vs Depth
    if csg > 0 and tcsg:
        plt.plot(temp_distribution.tcsg, md, 'c', label='Casing')  # Temp. due to gradient vs Depth
    if tfm:
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


def profile_multitime(temp_dist, values, times, tdsi=True, ta=False, tr=False, tcsg=False, tfm=True, tsr=False):
    md = temp_dist.md
    riser = temp_dist.riser
    csg = temp_dist.csgs_reach
    if tfm:
        plt.plot(temp_dist.tfm, md, color='k', label='Formation - Initial')  # Temp. due to gradient vs Depth

    color = ['r', 'b', 'g', 'c', '0.4', '0.9', '0.6', '0.8', '0.2', 'r', 'b', 'g', 'c', '0.4', '0.9', '0.6', '0.8']
    if len(values) > len(color):
        color = color * round((len(values) / len(color)))
    for x in range(len(values)):
        # Plotting Temperature PROFILE
        if tdsi:
            plt.plot(values[x].tdsi, md, c=color[x], label='Fluid in Drill String at %1.1f hours' % times[x])
        if ta:
            plt.plot(values[x].ta, md, c=color[x], label='Fluid in Annulus at %1.1f hours' % times[x])
        if riser > 0 and tr:
            plt.plot(values[x].tr, md, c=color[x], label='Riser at %1.1f hours' % times[x])
        if csg > 0 and tcsg:
            plt.plot(values[x].tcsg, md, c=color[x], label='Casing at %1.1f hours' % times[x])
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


def plot_torque_drag(well, plot='torque'):
    if plot == 'torque' or plot == 'both':
        plt.plot(well.torque, well.md, c='r', label='Torque')
        plt.xlabel('Torque, kNm')
        plt.ylabel('Depth, m')
        plt.ylim(plt.ylim()[::-1])  # reversing y axis
        plt.legend()  # applying the legend
        plt.show()
    if plot == 'drag' or plot == 'both':
        plt.plot(well.drag, well.md, c='b', label='Drag')
        plt.xlabel('Drag Force, kN')
        plt.ylabel('Depth, m')
        plt.ylim(plt.ylim()[::-1])  # reversing y axis
        plt.legend()  # applying the legend
        plt.show()

