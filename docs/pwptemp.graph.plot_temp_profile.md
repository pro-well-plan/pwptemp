# pwptemp.graph.plot_temp_profile(*temp_distribution, well*) #

Generate a plot for the well temperature distribution results.

> **Parameters:** 
* **temp_distribution: class** - TempDist instance from [pwptemp.main.temp_time.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.main.temp_time.md).
* **well: class** - NewWell instance from [pwptemp.input.set_well.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.input.set_well.md).

> **Returns:** 

a plot of the well temperature distribution.

## Example ##

```
>>> pwptemp.graph.plot_temp_profile(temp_distribution, well)
```
![](https://user-images.githubusercontent.com/52009346/68156946-fedcee80-ff4c-11e9-82a8-9a969c1d64f5.png)

See the [pwptemp.graph](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.graph.md) documentation.
