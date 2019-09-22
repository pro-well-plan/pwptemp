# pwptemp.wellpath.load(md, tvd, delta_step) #

Load an existing well profile to use the a set value of deltaz.

> **Parameters:** 
* **md: list** - List of measured depth values.
* **tvd: list** - List of true vertical depth values.
* **delta_step: int** - Length of each step, m.

> **Returns:** 

a **Well_Depths** instance with the following features
* **.md: list** - List of measured depth values.
* **.tvd: list** - List of true vertical depth values.
* **.deltaz: int** - Length of each cell, m.
* **.zstep: int** - Number of cells.

## Example ##

```
>>> len(md)
1000
>>> depths = pwptemp.wellpath.load(md, tvd, 50)
>>> len(depths.md)
20
>>> len(depths.tvd)
20
>>> depths.deltaz
50
>>> depths.zstep
20
```

See the [pwpetmp.wellpath](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.wellpath.md) documentation.
