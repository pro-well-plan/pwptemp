# TUTORIAL - Using 'pwptemp'

## Index ##

* [Create a Well Profile.](#create-a-well-profile)  
* [Load a Well Profile.](#load-a-well-profile)
* [Set and load parameters.](#set-and-load-parameters)
* [Calculating.](#calculating)
* [Plotting](#plotting)
* [Effects.](#effects)

## Create a Well Profile 
At first we will need the well profile (TVD and MD), the function pwp.WellPath.get() allow us to generate it for a vertical well case 
(at the moment). 
```
md, tvd, deltaz, zstep = pwptemp.WellPath.get(3000)
```

## Load a Well Profile
Loading a Well Profile
```
md, tvd, deltaz, zstep = pwptemp.WellPath.load(md, tvd, delta_step)
tdata = pwptemp.Input.temp_dict
well = pwptemp.Input.WellTemperature(tdata)
```

## Set and load parameters
We need all the well design data in order to set the parameters and conditions, for this we are importing the 
default dataset (temp_dict) from pwp.Input and finally just load this data to a new WellTemperature() instance (well for this example.)
```
tdata = pwptemp.Input.temp_dict
well = pwptemp.Input.WellTemperature(tdata)
```

### How to set different values for the parameters?
You can modify each parameter before load the dataset, for example:
```
tdata = pwptemp.Input.temp_dict
tdata['wd'] = 200    # Setting Water Depth = 200 m,  before loading the dataset
well = pwptemp.Input.WellTemperature(tdata)   # Dataset is now loaded with wd = 200 instead of the default value.  
```

## Calculating

### Calculating the Well Temperature Distribution for a set circulation time
Once a WellTemperature instance is created, it's possible to calculate the temperature distribution for a certain circulation time.
For example, let's do it for 24 hours.
```
Tdsi, Ta, Tr, Tcsg, Toh, Tsr, Tfm, time = pwptemp.Main.temp_time(24,mw,tvd,deltaz,zstep)
```
Here we get 7 lists with the temperature values for the different sections (inside drill string, drill string wall, riser wall, 
casing wall, open hole, surrounding space and formation).

### Calculating the stabilization time of the temperature profile
pwptemp also allows to calculate the circulation time when the temperature profile keep constant. The function stab_time() returns
the final time in hours, a list with the temperature value at bottom for each hour and another list for the output temperature.

```
finaltime, Tbot, Tout = pwptemp.Main.stab_time(well, tvd, deltaz, zstep)
```

## Calculating the Well Temperature Distributions for n timesteps
The function temp_times() allows to get an array with the temperature distributions for several timesteps. For example, let's do it
for 10 hours divided in 1 hour per timestep.
```
temps = temp_times(10, 1, well, tvd, deltaz, zstep)
```
## Plotting

### Plotting the Well Temperature Distribution for n hours
```
plot_temp_profile(Tdsi, Ta, Tr, Tcsg, Tfm, Tsr, Riser, md, time)
```

### Plotting the temperature at bottom/output up to stabilization time
```
plot_temp_time(finaltime, Tbot, Tout, Tfm)
```

## Effects

### Calculating the effect of main parameters on the Temperature Distribution
``` 
effect1 = param_effect(Tdsi, Ta, Toh, well)
```

### Calculating the effect of main parameters on the Heat Source Terms
```
effect2 = hs_effect(well)
```
