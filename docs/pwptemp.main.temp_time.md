# pwptemp.main.temp_time(n, well) #

Create a vertical well profile.

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

See the [pwpetmp.main](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.main.md) documentation.