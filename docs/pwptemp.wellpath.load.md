# pwptemp.wellpath.load(data, deltaz=50, mode=0) #

Load an existing well profile to use the a set value of deltaz.

> **Parameters:** 
* **data: list** - List of measured depth values.
* **deltaz: int** - - Length of each step, m.
* **mode: int** - 0: if data [{md:num, tvd:num}, {...], 1: if data [md, tvd].

> **Returns:** 

a **Well_Depths** instance with the following features
* **.md: list** - List of measured depth values.
* **.tvd: list** - List of true vertical depth values.
* **.deltaz: int** - Length of each cell, m.
* **.zstep: int** - Number of cells.

## Example ##

```
>>> len(data[0])
1000
>>> depths = pwptemp.wellpath.load(data, mode=1)
>>> len(depths.md)
21
>>> len(depths.tvd)
21
>>> depths.deltaz
51
>>> depths.zstep
21
```

See the [pwptemp.wellpath](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.wellpath.md) documentation.
