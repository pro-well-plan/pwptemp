import matplotlib.pyplot as plt


def profile(temp_distribution, sr=False):

    # Plotting Temperature PROFILE
    md = temp_distribution.md
    plt.plot(temp_distribution.tft, md, c='r', label='Fluid in Drill String')  # Temp. inside Tubing vs Depth
    plt.plot(temp_distribution.ta, md, 'b', label='Fluid in Annulus')  # Temp. of annulus
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