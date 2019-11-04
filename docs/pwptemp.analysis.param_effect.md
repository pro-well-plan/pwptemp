# pwptemp.analysis.param_effect(*temp_distribution, well*) #

Calculate the effect of mud circulation, heat source terms and formation temperature.

> **Parameters:**
* **temp_distribution: class** - TempDist instance from [pwptemp.main.temp_time.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.main.temp_time.md).
* **well: class** - NewWell instance from [pwptemp.input.set_well.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.input.set_well.md).

> **Returns:**

a **ParametersEffect** instance with the following features:
* **.flow: float** - Effect of the mud circulation.
* **.hs: float** - Effect of heat source terms.
* **.fm: float** - Effect of the formation.


## Example ##

```
>>> effect = pwptemp.analysis.param_effect(temp_distribution, well)
>>> effect.flow
56.25
>>> effect.hs
22.1
>>> effect.fm
21.65
```

See the [pwptemp.analysis](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.analysis.md) documentation.