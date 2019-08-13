import matplotlib.pyplot as plt

def temp_plot(finaltime,Tbot,Tout,Tfm,Tdsi,md,Ta,Tr,Tcsg,Tsr,Riser):

    # Plotting Tbottom and Tout through time
    plt.plot(range(finaltime), Tbot, 'b', label='Bottom')  # Temp. inside Annulus vs Time
    plt.plot(range(finaltime), Tout, 'r', label='Outlet (Annular)')  # Temp. inside Annulus vs Time
    plt.axhline(y=Tfm[-1], color='k', label='Formation')  # Temp. inside Formation vs Time
    plt.xlim(0, finaltime - 1)
    plt.xlabel('Time, h')
    plt.ylabel('Temperature, °C')
    plt.legend()  # applying the legend
    plt.show()

    # Plotting Temperature PROFILE
    plt.plot(Tdsi, md, c='r', label='Fluid in Drill String')  # Temp. inside Drillpipe vs Depth
    plt.plot(Ta[finaltime - 1], md, 'b', label='Fluid in Annulus')
    # plt.plot([i for i in Ta[finaltime-1]],md,'b',label='Fluid in Annulus')  #Temp. inside Annulus vs Depth
    if Riser>0:
        plt.plot(Tr, md, 'g', label='Temp. - Riser')  # Temp. due to gradient vs Depth
    plt.plot(Tcsg, md, 'c', label='Casing')  # Temp. due to gradient vs Depth
    plt.plot(Tfm, md, 'g', label='Formation')  # Temp. due to gradient vs Depth
    plt.plot(Tsr, md, c='k', ls='-', marker='', label='Surrounding Space')  # Temp. due to gradient vs Depth
    plt.xlabel('Temperature, °C')
    plt.ylabel('Depth, m')
    title = 'Temperature profile at %i hours' % finaltime
    plt.title(title)
    plt.ylim(plt.ylim()[::-1])  # reversing y axis
    plt.legend()  # applying the legend
    plt.show()