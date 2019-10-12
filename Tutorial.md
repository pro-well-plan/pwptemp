# TUTORIAL - Using 'pwptemp'

## Index ##

* [Create a Well Profile.](#create-a-well-profile)  
* [Load a Well Profile.](#load-a-well-profile)
* [Set and load parameters.](#set-and-load-parameters)
* [Calculating.](#calculating)
* [Analysis.](#analysis)

## Create a Well Profile 
At first we will need the well profile (TVD and MD), the function pwp.wellPath.get() allow us to generate it for a vertical well case 
(at the moment). 

> depths = pwptemp.wellpath.get(3000, 50)

## Load a Well Profile
Loading a Well Profile

> depths = pwptemp.wellpath.load(md, tvd, 50)

## Set and load parameters
We need all the well design data in order to set the parameters and conditions, for this we are importing the 
default dataset (temp_dict) from pwp.input and finally just load this data to a new WellTemperature() instance (well for this example.)

> tdata = pwptemp.input.temp_dict(50)
> well = pwptemp.input.set_well(tdata, depths)

### How to set different values for the parameters?
You can modify each parameter before load the dataset, for example:

> tdata = pwptemp.input.temp_dict(50)
> tdata['wd'] = 200    # Setting Water Depth = 200 m,  before loading the dataset
> well = pwptemp.input.set_well(tdata)   # Dataset is now loaded with wd = 200 instead of the default value.  

## Calculating

### Calculating the Well Temperature Distribution for a set circulation time
Once a WellTemperature instance is created, it's possible to calculate the temperature distribution for a certain circulation time.
For example, let's do it for 24 hours.

> temp = pwptemp.main.temp_time(24, well)

> pwptemp.graph.plot_temp_profile(temp, well)
>![](https://user-images.githubusercontent.com/52009346/66595749-e0791280-eb9b-11e9-822e-3155dad6c64a.png)

Here we get an instance with the temperature values for the different sections (inside drill string, drill string wall, riser wall, 
casing wall, open hole, surrounding space and formation).

### Calculating the stabilization time of the temperature profile
pwptemp also allows to calculate the circulation time when the temperature profile keep constant. The function stab_time() returns
the final time in hours, a list with the temperature value at bottom for each hour and another list for the output temperature.

> stabilization = pwptemp.main.stab_time(well)

> pwptemp.graph.plot_temp_time(stabilization)
> ![](https://user-images.githubusercontent.com/52009346/66596338-018e3300-eb9d-11e9-8373-90853f2398a0.png)

## Calculating the Well Temperature Distributions for n timesteps
The function temp_times() allows to get an array with the temperature distributions for several timesteps. For example, let's do it
for 10 hours divided in 1 hour per timestep.

> temps = pwptemp.main.temp_times(10, 1, well)

> pwptemp.graph.plot_temp_profile(temps[0], well)
> ![](https://user-images.githubusercontent.com/52009346/66596694-a577de80-eb9d-11e9-8e07-5a5627eb6846.png)

> pwptemp.graph.plot_temp_profile(temps[3], well)
> ![](https://user-images.githubusercontent.com/52009346/66596777-c3454380-eb9d-11e9-8c14-28f378c69ab0.png)

## Analysis

### Calculating the effect of main parameters on the Temperature Distribution

> effect1 = param_effect(temp, well)

> pwptemp.analysis.plot(effect1, 1)
> !![](https://user-images.githubusercontent.com/52009346/66598876-4d8fa680-eba2-11e9-8d8c-ecd1de472b1b.png)

### Calculating the effect of main parameters on the Heat Source Terms

> effect2 = hs_effect(well)

> pwptemp.analysis.plot(effect2, 2)
> ![](https://user-images.githubusercontent.com/52009346/66602941-6781b700-ebab-11e9-818c-5e7d7b84bfc4.png)
