# pwptemp.wellpath.get(*mdt, deltaz=50, profile='V', build_angle=1, kop=0, eob=0, sod=0, eod=0, kop2=0, eob2=0*) #

Create a well profile.

> **Parameters:** 
* **mdt: int** - Measured depth of the target, m.
* **deltaz: float** - Length of each cell, m.
* **profile: string** - type of well:
  * 'V': vertical well.
  * 'J': J-type well.
  * 'S': S-type well.
  * 'H1': horizontal single-curve well.
  * 'H2': horizontal double-curve well.
* **build_angle: float** - angle of the build section, degrees.
* **kop: float** - kick-off point, m.
* **eob: float** - end of build, m.
* **sod: float** - start of drop, m.
* **eod: float** - end of drop, m.
* **kop2: float** - kick-off point 2, m.
* **eob2: float** - end of build 2, m.

> **Returns:** 

a **Well_Depths** instance with the following features:
* **.md: list** - List of measured depth values.
* **.tvd: list** - List of true vertical depth values.
* **.deltaz: float** - Length of each cell, m.
* **.zstep: int** - Number of cells.

## Example ##

```
>>> depths = pwptemp.wellpath.get(1000, deltaz=100, kop=100, eob=300, build_angle=30, profile='H2', kop2=600, eob2=800)
>>> depths.md
[0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
>>> depths.tvd
[0, 100, 198.86, 290.98, 377.58, 464.18, 550.78, 646.27, 716.18, 716.18, 716.18]
```

See the [pwptemp.wellpath](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.wellpath.md) documentation.
