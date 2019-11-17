from . import input
from . import initcond
from . import heatcoefficients
from . import linearsystem
from . import main


def temp(n, mdt=3000, casings=[], wellpath_data=[], bit=0.216, deltaz=50, profile='V', build_angle=1, kop=0, eob=0,
         sod=0, eod=0, kop2=0, eob2=0, wellpath_mode=0, wellpath_load_mode=0):
    import pwptemp
    tdata = pwptemp.drilling.input.data(casings, bit)
    if wellpath_mode == 0:
        depths = pwptemp.wellpath.get(mdt, deltaz, profile, build_angle, kop, eob, sod, eod, kop2, eob2)
    if wellpath_mode == 1:
        depths = pwptemp.wellpath.load(wellpath_data, deltaz, wellpath_load_mode)
    well = pwptemp.drilling.input.set_well(tdata, depths)
    temp = pwptemp.drilling.main.temp_time(n, well)

    return temp
