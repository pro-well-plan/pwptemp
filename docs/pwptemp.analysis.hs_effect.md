# pwptemp.analysis.hs_effect(*well*) #

Calculate the effect of friction and drill string rotation.

> **Parameters:**
* **well: class** - NewWell instance from [pwptemp.input.set_well.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.input.set_well.md).

> **Returns:**

a **HeatSourceEffect** instance with the following features:
* **.ds_rot1: float** - Effect of Drill String Rotation in Heat Source Term Qp.
* **.fric1: float** - Effect of Friction in Heat Source Term Qp.
* **.ds_rot2: float** - Effect of Drill String Rotation in Heat Source Term Qa.
* **.fric2: float** - Effect of Friction in Heat Source Term Qa.
* **.hsr: float** - #Pipe-Annular heat source ratio.

## Example ##

```
>>> effect = pwptemp.analysis.hs_effect(well)
>>> effect.ds_rot1
96.54
>>> effect.fric1
3.46
>>> effect.ds_rot2
4.1
>>> effect.fric2
95.9
>>> effect.hsr
0.05
```

See the [pwptemp.analysis](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.analysis.md) documentation.
