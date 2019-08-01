# WELL TEMPERATURE MODELLING 

This project aims to create a module able to calculate the temperature distribution for an entire well. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Libraries used in the project:

> Numpy, Matplotlib, Math...


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
Pending: WOB, ROP, RPM...
```

### Outputs

```
1. Temperature of the fluid inside the Drill String (Tdsi)
2. Temperature of the Drill String Wall (Tds)
3. Temperature of the fluid inside the Annular (Ta)
4. Temperature of the Casing (Tcsg)
5. Temperature of the Riser (Tr)
6. Temperature of the Surrounding Space (Tsr)
7. Temperature of the Formation (Tfm)
```
![Diapositiva1](https://user-images.githubusercontent.com/52009346/62273419-d4efc980-b43d-11e9-974e-4cbbf086c0ff.JPG)

> Note 1: Above seabed, casing section is replaced with the riser and surrounding space would be sea water.
> Note 2: Beyond the 'undisturbed formation zone' the temperature keeps constant (Tfm)     

## Running the tests

Explain how to run the automated tests for this system
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
