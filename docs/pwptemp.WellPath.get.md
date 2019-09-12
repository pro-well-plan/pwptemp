# pwptemp.WellPath.get(mdt) #

Create a vertical well profile.

> **Parameters:** 
* **mdt: int** - Measured depth of the target.

> **Returns:** 
* **md: list** - List of measured depth values.
* **tvd: list** - List of true vertical depth values.
* **deltaz: int** - Length of each cell, m.
* **zstep: int** - Number of cells.

## Example ##

```
>>> md, tvd, deltaz, zstep = pwptemp.WellPath.get(500)
>>> md
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
>>> tvd
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
>>> deltaz
50
>>> zstep
10
```
