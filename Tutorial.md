# TUTORIAL - Using 'pwptemp'

## Index ##

* [Wellpath.](#wellpath)
* [Drilling.](#drilling)
* [Production.](#production)

## Wellpath
* [Create a well profile.](#create-a-well-profile)
* [Load a well profile.](#load-a-well-profile)
* [Plot.](#plot)

### create a well profile
get() function from wellpath module generates a vertical well by default. However, you can create a different case 
(J-type, S-type or horizontal well):

```
>>> import pwptemp.wellpath as ptw
>>> ptw.get( 
            mdt=2800,           # set target depth at 2800 m.
            grid_length=50     # set length of each cell. default = 50 m
            profile='S',        # set S-type well
            build_angle=30,     # set angle of 30 degrees
            kop=600,            # set kick-off point at 600 m
            eob=1200,           # set end of build at 1200 m
            sod=1600,           # set start of drop at 1600 m
            eod=2500           # set end of drop at 2500 m
            )
```

### load a well profile
Load your own MD-TVD data:
```
>>> ptw.load(10, wellpath_data = [{md:num, tvd:num, inclination:num, azimuth:num},{md:num2, tvd:num2, inclination:num, 
            azimuth:num},...])
```

### plot
Generate a 3D plot of the well by using the plot attribute included in the functions get() and load()
```
>>> ptw.get(3000).plot(azim=45, elev=20)
```
![](https://user-images.githubusercontent.com/52009346/78991923-6883a900-7b3a-11ea-80ce-6801950ff20d.PNG)

## Drilling
Create a well temperature distribution for a drilling operation:

```
>>> import pwptemp.drilling as ptd
>>> temp = ptd.temp(10)    # well temperature distribution at 10 hours of mud circulation. 
```

### Casings
Add as many casings as you want:
```
>>> ptd.temp(10, casings = [{od:num1, id:num1, depth:num1},{od:num2, id:num2, depth:num2},...])
```

### Parameters
Change any parameter involved during the operation:
```
>>> ptd.temp(10, 
            change_input={'wd': 100,       # set water-depth in m
                          'ts': 20,        # set surface temperature in °C
                          'q': 40,         # set flow rate in m3/h
                          'gt: 0.024,      # set geothermal gradient in °C/m
                          'wtg': -0.006,   # set water thermal gradient in °C/m
                          'wob': 22.8,     # set weight on bit in kN
                          'an': 1.86       # set area of the nozzles in m2 
                         }
            )
```
[click here](https://github.com/pro-well-plan/pwptemp/blob/master/physics/drilling/inputs.md)
to check all the parameters used for the calculations or
[click here](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.drilling.input_info.md)
to check a function to print the information.


### Plots
#### well temperature distribution
```
>>> ptd.temp(10).plot()
```
![](https://user-images.githubusercontent.com/52009346/69182995-5fa22480-0b12-11ea-98cc-8331aeed5c1c.png)

#### behavior
```
>>> ptd.temp(10).behavior().plot()
```
![](https://user-images.githubusercontent.com/52009346/78992254-21e27e80-7b3b-11ea-891f-43b961855b08.PNG)

#### multiple times
```
>>> ptd.temp(10).plot_multi()
```
![](https://user-images.githubusercontent.com/52009346/78992817-7c300f00-7b3c-11ea-9c2e-73f0dd32840e.PNG)

## Production
Create a well temperature distribution for a production operation:

```
>>> import pwptemp.production as ptp
>>> temp = ptp.temp(10)    # well temperature distribution at 10 hours of production. 
```

### Casings
Add as many casings as you want:
```
>>> ptp.temp(10, casings = [{od:num1, id:num1, depth:num1},{od:num2, id:num2, depth:num2},...])
```

### Plots
#### well temperature distribution
```
>>> ptp.temp(10).plot()
```
![](https://user-images.githubusercontent.com/52009346/78993027-109a7180-7b3d-11ea-9cf9-722c007292d1.PNG)

#### behavior
```
>>> ptp.temp(10).behavior().plot()
```
![](https://user-images.githubusercontent.com/52009346/78992954-d4ffa780-7b3c-11ea-9507-a4273a501eb7.PNG)

#### multiple times
```
>>> ptp.temp(10).plot_multi()
```
![](https://user-images.githubusercontent.com/52009346/78992876-a5509f80-7b3c-11ea-99c8-4d654d755584.PNG)