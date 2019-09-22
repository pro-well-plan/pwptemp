# pwptemp.wellpath.get(mdt, deltaz) #

Create a vertical well profile.

> **Parameters:** 
* **mdt: int** - Measured depth of the target.
* **deltaz: int** - Length of each cell, m.

> **Returns:** 

a **Well_Depths** instance with the following features:
* **.md: list** - List of measured depth values.
* **.tvd: list** - List of true vertical depth values.
* **.deltaz: int** - Length of each cell, m.
* **.zstep: int** - Number of cells.

## Example ##

```
>>> depths = pwptemp.wellpath.get(500, 50)
>>> depths.md
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
>>> depths.tvd
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
>>> depths.deltaz
50
>>> depths.zstep
10
```

See the [pwpetmp.wellpath](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.wellpath.md) documentation.
