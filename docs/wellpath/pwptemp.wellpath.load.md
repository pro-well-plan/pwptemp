# pwptemp.wellpath.load(data, deltaz=50) #

Load an existing well profile to use the a set value of deltaz.

> **Parameters:** 
* **data: list** - List of measured depth values. [{md:num, tvd:num}, {...] or [md, tvd]
* **deltaz: int** - - Length of each step, m.

> **Returns:** 

an object with the following features:
* **.md: list** - List of measured depth values.
* **.tvd: list** - List of true vertical depth values.
* **.deltaz: int** - Length of each cell, m.
* **.zstep: int** - Number of cells.

## Example ##

```
>>> len(data[0])
1000
>>> depths = pwptemp.wellpath.load(data)
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
