# TUTORIAL - Using 'pwptemp'

## Index ##

* [Introduction.](#introduction) 
* [Well Profile.](#well-profile)  
* [Casings.](#casings)
* [Parameters.](#parameters)
* [Plots.](#plots)

## Introduction
Create a well temperature distribution easily with pwptemp:

```
>>> import pwptemp.drilling as ptd
>>> temp = ptd.temp(10)    # well temperature distribution at 10 hours of mud circulation. 
```
Of course, you can also do more interesting things with pwptemp, since load your own wellpath up to generate analysis.

## Well Profile
### create a well profile
ptd.temp() function generates a vertical well by default. However, you can create a different case (J-type, S-type or 
horizontal well):

```
ptd.temp(10, 
         mdt=2800,           # set target depth at 2800 m. default = 3000 m
         profile='S',        # set S-type well
         build_angle=30,     # set angle of 30 degrees
         kop=600,            # set kick-off point at 600 m
         eob=1200,           # set end of build at 1200 m
         sod=1600,           # set start of drop at 1600 m
         eod=2500)           # set end of drop at 2500 m
```

### load a well profile
It is also possible to load your own MD-TVD data:
1. data as a list of dictionaries:
```
ptd.temp(10, wellpath_data = [{md:num, tvd:num},{md:num2, tvd:num2},...])
```
2. data as a list of lists [md, tvd]:
```
ptd.temp(10, wellpath_data = [[md1, md2,...],[tvd1, tvd2,...]])
```

> depths = pwptemp.wellpath.load(md, tvd, 50)

## Casings
It is also possible to add as many casings as you want:
```
ptd.temp(10, casings = [{od:num1, id:num1, depth:num1},{od:num2, id:num2, depth:num2},...])
```
Where depth is md in meters.

## Parameters
It is also possible to change any parameter:
```
ptd.temp(10, 
         change_input={'wd': 100,       # set water-depth in m
                       'ts': 20,        # set surface temperature in °C
                       'q': 40,         # set flow rate in m3/h
                       'gt: 0.024,      # set geothermal gradient in °C/m
                       'wtg': -0.006,   # set water thermal gradient in °C/m
                       'wob': 22.8,     # set weight on bit in kN
                       'an': 1.86       # set area of the nozzles in m2 
                       })
```
[click here](https://github.com/pro-well-plan/pwptemp/blob/master/physics/drilling/inputs.md)
to check all the parameters used for the calculations or
[click here](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.drilling.input_info.md)
to check a function to print the information.


## Plots
### well temperature distribution
```
ptd.temp(10).plot()
```
![](https://user-images.githubusercontent.com/52009346/69182995-5fa22480-0b12-11ea-98cc-8331aeed5c1c.png)

### stabilization time
```
ptd.stab().plot()
```
or from the temperature distribution object:
```
ptd.temp(10).stab().plot()
```
![](https://user-images.githubusercontent.com/52009346/69183056-7f394d00-0b12-11ea-89e7-e8c206925222.png)

### analysis
General effect:
```
ptd.temp(10).effect().plot()
```
![](https://user-images.githubusercontent.com/52009346/69183085-8f512c80-0b12-11ea-8fa2-bc032674fd08.png)

Regarding heat source terms:
```
ptd.temp(10).well().effect().plot()
```
![](https://user-images.githubusercontent.com/52009346/69183029-70eb3100-0b12-11ea-9a94-36b849a55a90.png)
