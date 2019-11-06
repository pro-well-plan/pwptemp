# pwptemp.analysis.param_effect(*temp_distribution, well, md_length=1*) #

Calculate the effect of mud circulation, heat source terms and formation temperature.

> **Parameters:**
* **temp_distribution: class** - TempDist instance from [pwptemp.main.temp_time.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.main.temp_time.md).
* **well: class** - NewWell instance from [pwptemp.input.set_well.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.input.set_well.md).
* **md_length: int or float** - percentage (from 0 for the wellhead to 1 for the bottom) to determine the measured depth to be analyzed.

> **Returns:**

a **ParametersEffect** instance with the following features:
* **.flow: float** - Effect of the mud circulation.
* **.hs: float** - Effect of heat source terms.
* **.fm: float** - Effect of the formation.


## Example ##

```
>>> effect = pwptemp.analysis.param_effect(temp_distribution, well, md_length=0.3)
>>> effect.flow
71.64
>>> effect.hs
15.53
>>> effect.fm
12.83
```

See the [pwptemp.analysis](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.analysis.md) documentation.