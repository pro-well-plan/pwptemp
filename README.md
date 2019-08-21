![OSP](https://user-images.githubusercontent.com/52009346/62771366-56c69f00-ba9d-11e9-9c86-a868bf3a1180.png)

# WELL TEMPERATURE MODELLING 

This project aims to create a module able to calculate the temperature distribution for an entire well. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Get pwptemp

* Wheels for Python from [PyPI](https://pypi.python.org/pypi/pwptemp/)
    * `pip install pwptemp`
* Source code from [github](https://github.com/pro-well-plan/pwptemp)
    * `git clone https://github.com/pro-well-plan/pwptemp`


### Inputs

```
1. Inlet Fluid Temperature
2. Surface Temperature
3. Well Depth
4. Water Depth
5. Drill Pipe Inner Diameter
6. Drill Pipe Outer Diameter
7. Casing Inner Diameter
8. Surrounding Space Diameter
9. Riser Inner Diameter
10. Riser Outer Diameter
11. Nearby Formation Diameter
12. Circulation Rate
13. Fluid Thermal Conductivity (Default Value Provided)
14. Casing Thermal Conductivity (Default Value Provided)
15. Drill Pipe Thermal Conductivity (Default Value Provided)
16. Comprehensive Csg-Fm Thermal Conductivity (Default Value Provided)
17. Riser Thermal Conductivity (Default Value Provided)
18. Comprehensive Riser-Water Thermal Conductivity (Default Value Provided)
19. Seawater Thermal Conductivity (Default Value Provided)
20. Fluid Heat Capacity (Default Value Provided)
21. Casing Heat Capacity (Default Value Provided)
22. Drill Pipe Heat Capacity (Default Value Provided)
23. Riser Heat Capacity (Default Value Provided)
24. Seawater Heat Capacity (Default Value Provided)
25. Surrounding Space Heat Capacity (Default Value Provided)
26. Convective Heat Transfer Coefficient at the Inner Face of Drill Pipe (Default Value Provided)
27. Convective Heat Transfer Coefficient at the Outer Face of Drill Pipe (Default Value Provided)
28. Convective Heat Transfer Coefficient at the Inner Face of Casing (Default Value Provided)
29. Convective Heat Transfer Coefficient at the Inner Face of Riser (Default Value Provided)
30. Geothermal Gradient (Default Value Provided)
31. Seawater Thermal Gradient (Default Value Provided)
32. Fluid Density (Default Value Provided)
33. Drill Pipe Density (Default Value Provided)
34. Casing Density (Default Value Provided)
35. Riser Density (Default Value Provided)
36. Formation Density (Default Value Provided)
37. Seawater Density (Default Value Provided)
38. Surrouding Average Density (Default Value Provided)
39. Weight on bit (WOB)
40. Rate of Penetration (ROP)
41. Area of Nuzzles
42. Reynolds
43. Measured Depth at Target
```

### Outputs

```
Temperature of the fluid inside the Drill String (Tdsi)
Temperature of the Drill String Wall (Tds)
Temperature of the fluid inside the Annular (Ta)
Temperature of the Casing (Tcsg)
Temperature of the Riser (Tr)
Temperature of the Surrounding Space (Tsr)
Temperature of the Formation (Tfm)
```
![Diapositiva1](https://user-images.githubusercontent.com/52009346/62273419-d4efc980-b43d-11e9-974e-4cbbf086c0ff.JPG)

> Note 1: Above seabed, casing section is replaced with the riser and surrounding space would be sea water.

> Note 2: Beyond the 'undisturbed formation zone' the temperature keeps constant (Tfm).     

### Distribution Scheme

<img src="https://user-images.githubusercontent.com/52009346/62863045-fbe4b000-bd07-11e9-9bda-30330dc612d1.PNG" width="450" height="400"> <img src="https://user-images.githubusercontent.com/52009346/62856722-f4b4a680-bcf5-11e9-80ef-751e03b4dbc2.PNG" width="200" height="180">

### Code Distribution

The code is compound by 8 files:

> **Wellpath.py** ▷ contains a function to define the MD, and TVD values from the wellpath.

> **temp_dict.json** ▷ contains the parameters required for the temperature calculation.

> **Input.py** ▷ creates a class (WellTemperature) to have access to the parameters of the case.

> **InitCond.py** ▷ defines the initial and boundary conditions.

> **HeatCoefficients.py** ▷ contains a function to calculate the coefficients for the heat tranfer equations that will be used.

> **LinearSystem.py** ▷ contains a function to generate the entire temperature profile. 

> **Graph.py** ▷ contains a function to plot Tfm, Ta(bottom), Ta(outlet) vs time and also Temperature profile at stabilization time.

> **Main.py** ▷ contains a function to determine the temperature profile when it is already stabilized.

### Deployment
**1.** If you have already the values of TVD and MD from your own wellpath, then you can skip the calculation in the wellpath function:
```
md=range(mdt)  # Measured Depth from RKB, m
    tvd=[]   # True Vertical Depth from RKB, m

    for z in md:
        tvd.append(z)
```
And then you only need to define these two lists (tvd and md) instead, and the shoes depths of the casings of course.

**2.** You can check and modify all the parameters from the file temp_dict.json or call the value from a variable/object directly to the file Input.py. 

**3.** Run the file Main.py and you will get the entire temperature profile at stabilization time (Tdsi,Ta,Tr,Tcsg,Tsr,Tfm), the temperature at the bottom through the time (Tbot),the temperature at the outlet (Annular) through the time (Tout) and the stabilization temperature (finaltime).


## Running the tests

How to run the automated tests for this system...
```
- unittest
- nose or nose2
- pytest
```

## Contributing

Please read [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Eirik Lyngvi** - *Initial work* - [elyngvi](https://github.com/elyngvi)
* **Juan Camilo Gonzalez Angarita** - *Initial work* - [jcamiloangarita](https://github.com/jcamiloangarita)
* **Muhammad Suleman** - *Initial work* - [msfazal](https://github.com/msfazal)


See also the list of [contributors](https://github.com/jcamiloangarita/WT/graphs/contributors) who participated in this project.

## License

This project is licensed under the GNU Lesser General Public License v3.0 - see the [LICENSE](LICENSE.md) file for details
