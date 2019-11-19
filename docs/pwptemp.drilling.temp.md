# pwptemp.drilling.temp(*n, mdt=3000, casings=[], wellpath_data=[], bit=0.216, deltaz=50, profile='V', build_angle=1, kop=0, eob=0, sod=0, eod=0, kop2=0, eob2=0, wellpath_mode=0, wellpath_load_mode=0, change_input={}*)

Generate the well temperature profile for a certain circulation time **n**.

> **Parameters:** 
* **n: int** - Circulation time, h.
* **mdt: int** - Measured depth of the target, m.
* **casings: array** - casings-related data [[od, id, depth]]
* **wellpath_data: list** - MD and TVD data [{md:num, tvd:num},{...}].
* **bit: float** - - Diameter of the hole. *Only required there are not casings.
* **deltaz: int** - Length of each cell, m.
* **profile: str** - type of well:
  * 'V': vertical well.
  * 'J': J-type well.
  * 'S': S-type well.
  * 'H1': horizontal single-curve well.
  * 'H2': horizontal double-curve well.
* **build_angle: int** - angle of the build section, degrees.
* **kop: int** - kick-off point, m.
* **eob: int** - end of build, m.
* **sod: int** - start of drop, m.
* **eod: int** - end of drop, m.
* **kop2: int** - kick-off point 2, m.
* **eob2: int** - end of build 2, m.
* **wellpath_mode: int** - 0: create wellpath, 1: load wellpath.
* **wellpath_load_mode: int** - 0: if data [{md:num, tvd:num}, {...], 1: if data [md, tvd].
* **change_input: dict** - change default values {id:value, id2:value2...}

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
>>> import pwptemp.drilling as ptd
>>> temp = ptd.temp(10)
```

See the [pwptemp.drilling](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.drilling.md) documentation.


## Methods ##
###.plot()
Plotting the well temperature distribution.
```
>>> import pwptemp.drilling as ptd
>>> temp = ptd.temp(10)
>>> temp.plot()
```
![](https://user-images.githubusercontent.com/52009346/69182995-5fa22480-0b12-11ea-98cc-8331aeed5c1c.png)

###.well()
Returns the well instance with all the parameters.
```
>>> import pwptemp.drilling as ptd
>>> temp = ptd.temp(10)
>>> well = temp.well().effect().plot()
```
![](https://user-images.githubusercontent.com/52009346/69183029-70eb3100-0b12-11ea-9a94-36b849a55a90.png)

```
>>> import pwptemp.drilling as ptd
>>> temp = ptd.temp(10)
>>> well = temp.well().stab().plot()
```
![](https://user-images.githubusercontent.com/52009346/69183056-7f394d00-0b12-11ea-89e7-e8c206925222.png)

###.effect(*md_length=1*)
Returns the effect instance with the relevance of the respective factor on the temperature calculation.
```
>>> import pwptemp.drilling as ptd
>>> temp = ptd.temp(10)
>>> temp.effect().plot()
```
![](https://user-images.githubusercontent.com/52009346/69183085-8f512c80-0b12-11ea-8fa2-bc032674fd08.png)

###.stab()
Returns the temperature behavior until the stabilization time.
```
>>> import pwptemp.drilling as ptd
>>> temp = ptd.temp(10)
>>> temp.stab().plot()
```
![](https://user-images.githubusercontent.com/52009346/69183056-7f394d00-0b12-11ea-89e7-e8c206925222.png)
