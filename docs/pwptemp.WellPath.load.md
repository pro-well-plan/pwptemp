# pwptemp.WellPath.load(md, tvd, delta_step) #

Load an existing well profile to use the default value of deltaz.

> **Parameters:** 
* **md: list** - List of measured depth values.
* **tvd: list** - List of true vertical depth values.
* **delta_step: int** - Length of each step, m.

> **Returns:** 
* **md: list** - List of measured depth values.
* **tvd: list** - List of true vertical depth values.
* **deltaz: int** - Length of each cell, m.
* **zstep: int** - Number of cells.

## Example ##

```
>>> len(md)
1000
>>> md, tvd, deltaz, zstep = pwptemp.WellPath.get(md, tvd, 1)
>>> len(md)
20
>>> len(tvd)
20
>>> deltaz
50
>>> zstep
20
```

See the [pwpetmp.WellPath](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.WellPath.md) documentation.
