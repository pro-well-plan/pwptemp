from .input import data, set_well
from .main import temp_time
from .. import wellpath
from .input import info


def temp(n, mdt=3000, casings=[], wellpath_data=[], bit=0.216, deltaz=50, profile='V', build_angle=1, kop=0, eob=0,
             sod=0, eod=0, kop2=0, eob2=0, wellpath_mode=0, wellpath_load_mode=0, change_input={}):
    tdata = data(casings, bit)
    for x in change_input:   # changing default values
        if x in tdata:
            tdata[x] = change_input[x]
        else:
            raise TypeError('%s is not a parameter' % x)
    if wellpath_mode == 0:
        depths = wellpath.get(mdt, deltaz, profile, build_angle, kop, eob, sod, eod, kop2, eob2)
    if wellpath_mode == 1:
        depths = wellpath.load(wellpath_data, deltaz, wellpath_load_mode)
    well = set_well(tdata, depths)
    temp_distribution = temp_time(n, well)
    return temp_distribution


def input_info(about='all'):
    info(about)
