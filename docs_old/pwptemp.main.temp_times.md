# pwptemp.main.temp_times(*n, x, well*) #

Create well temperature profiles for several times.

> **Parameters:**
* **n: int** - Circulation time, h.
* **x: float** - Time steps duration, h.
* **well: class** - NewWell instance from [pwptemp.input.set_well.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.input.set_well.md).

> **Returns:**
* **temps: list** - list of Well temperature distributions [pwptemp.main.temp_time.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.main.temp_time.md)..

## Example ##

```
>>> temps = pwptemp.main.temp_times(10, 0.5, well)  #for 10 hours (each 0.5 hours) of drilling fluid circulation
>>> len(temps)
20
>>> type(temps[0].tdsi)  #tdsi: temperature of fluid inside the drill string
<class 'list'>
>>> type(temps[0].tds)  #tds: temperature of drill string wall
<class 'list'>
>>> type(temps[0].ta)  #ta: temperature of fluid inside the annular
<class 'list'>
>>> type(temps[0].tr)  #tr: temperature of riser wall
<class 'list'>
>>> type(temps[0].tcsg)  #tcsg: temperature of casing wall
<class 'list'>
>>> type(temps[0].toh)  #toh: temperature of open hole (zone below the casing)
<class 'list'>
>>> type(temps[0].tsr)  #tsr: temperature of surrounding space
<class 'list'>
>>> type(temps[0].tfm)  #tfm: temperature of formation
<class 'list'>
>>> temps[18].time
9.5
```

See the [pwptemp.main](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.main.md) documentation.
