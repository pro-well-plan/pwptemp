# pwptemp.main.temp_time(*n, well*) #

Generate the well temperature profile for a certain circulation time **n**.

> **Parameters:**
* **n: int** - Circulation time, h.
* **well: class** - NewWell instance from [pwptemp.input.set_well.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.input.set_well.md).

> **Returns:**

a **TempDist** instance with the following features:
* **.tdsi: list** - Temperature values (fluid in the drill string).
* **.tds: list** - Temperature values (drill string wall).
* **.ta: list** - Temperature values (fluid in the annular).
* **.tr: list** - Temperature values (riser wall).
* **.tcsg: list** - Temperature values (first casing wall).
* **.toh: list** - Temperature values (section below the first casing).
* **.tsr: list** - Temperature values (surrounding space).
* **.tfm: list** - Temperature values (formation).
* **.time: int** - Circulation time, h.

## Example ##

```
>>> temp_distribution = pwptemp.main.temp_time(5, well)  #for 5 hours of drilling fluid circulation
>>> type(temps.tdsi)
<class 'list'>
>>> type(temps.tds)
<class 'list'>
>>> type(temps.ta)
<class 'list'>
>>> type(temps.tr)
<class 'list'>
>>> type(temps.tcsg)
<class 'list'>
>>> type(temps.toh)
<class 'list'>
>>> type(temps.tsr)
<class 'list'>
>>> type(temps.tfm)
<class 'list'>
>>> temps.time
5
```

See the [pwptemp.main](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.main.md) documentation.
