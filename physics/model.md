# Heat Transfer Model
The temperature distribution of wellbore and surrounding formation has a significant influence on safe and fast drilling. This transient temperature model investigate the temperature distribution of wellbores during circulation and was established based on the energy conservation law. The model was discretized by the finite difference method and solved by the successive over relaxation
iterative method.

Heat convection and heat transfer are the main forms of heat exchange of the drilling fluid and the surrounding formation.The formation temperature increases with the increase of vertical depth. In the vertical section, the surrounding formation temperature increases linearly with the increase of the well depth. In the inclined section, the surrounding formation temperature increases more and more slowly as the well depth increases. In the horizontal section, the formation temperature does not change as the well depth increases.

# Assumptions
(1) The wellbore is a regular cylinder;

(2) Drilling fluid is incompressible, and the density, specific heat capacity, and thermal conductivity of drilling fluid are constant

(3) When the drilling fluid flows in the drill string and in the annulus, only the velocity in the axial direction is taken into account, irrespective of the velocity in the radial direction.

# Inside the drill string
When the drilling fluid is flowing inside the drill string, following three reasons causes the change in internal energy of drilling fluid:
(1) heat transfer within the drilling fluid because of flowing down inside the drill string in the axial direction;
(2) heat convection of the drilling fluid and the inner wall of drill string;
(3) heat generated due to the friction losses of drilling fluid

Heat transfer control equation inside the drill string is:

<img src="https://user-images.githubusercontent.com/52009346/65387268-fedeb180-dd45-11e9-86c9-9b93fd685e60.PNG" width="500" 
height="60"> 

# Drill string wall
The changes in internal energy of drill string volume element are caused by following three reasons:
(1) heat conduction of the drill string in the axial direction;
(2) heat convection of the inner wall of drill string and drilling fluid inside the drill string;
(3) heat convection of the outer wall of drill string and the annular drilling fluid.

Heat transfer control equation of the drill string is given as:

<img src="https://user-images.githubusercontent.com/52009346/65387279-1cac1680-dd46-11e9-8e37-8b1a58b9b039.PNG" width="550" 
height="60"> 


# In the annulas
When the drilling fluid is flowing in the annulus, changes in internal energy of drilling fluid volume element are caused by four reasons:
(1) heat transfer within the drilling fluid because of flowing up in the annular in the axial direction;
(2) heat convection of drilling fluid and casing or surrounding formation;
(3) heat convection of drilling fluid and outside wall of drill string;
(4) heat produced due to the frictional flow losses of drilling fluid.

Heat transfer control equation in the annulus is given by the following equation:

<img src="https://user-images.githubusercontent.com/52009346/65387272-0d2ccd80-dd46-11e9-9211-18501db10b53.PNG" width="650" 
height="60"> 

# In First layer of casing
Changes in internal energy of volume element of the first layer of casing are caused by three reasons:
(1) heat conduction of the first layer of casing in the axial direction;
(2) heat transfer between the first layer of casing and the first layer of cement sheath;
(3) heat convection between the first layer of casing and the annulus drilling fluid.

Heat transfer control equation of the first layer of casing is given by the following equation:

<img src="https://user-images.githubusercontent.com/52009346/65387283-2897d880-dd46-11e9-8269-fa4d2567ae81.PNG" width="500" 
height="60"> 


# In Surrounding Space (Casings and Cement Sheaths / formation)
Changes in internal energy of volume element of casing, cement sheath, and surrounding formation are caused by heat conduction in the axial direction and heat transfer between adjacent layers in the radial direction. On the basis of the law of conservation of energy, heat transfer control equation in sorrounding space is given by the following equation:

<img src="https://user-images.githubusercontent.com/52009346/65387288-30577d00-dd46-11e9-8070-fe0998752dfe.PNG" width="400" 
height="60"> 

# whereas

![dens](https://user-images.githubusercontent.com/52009346/65387330-9d6b1280-dd46-11e9-8b45-5b75667ac428.PNG)

![shc](https://user-images.githubusercontent.com/52009346/65387362-0eaac580-dd47-11e9-9128-9b7f547cd167.PNG)

![vel](https://user-images.githubusercontent.com/52009346/65387364-1c604b00-dd47-11e9-8631-d175d25f4a12.PNG)

![temp](https://user-images.githubusercontent.com/52009346/65387368-271ae000-dd47-11e9-8962-01cd71615208.PNG)

![chtc](https://user-images.githubusercontent.com/52009346/65387390-3732bf80-dd47-11e9-8da7-66ccd55a9399.PNG)

![thermal](https://user-images.githubusercontent.com/52009346/65387394-4154be00-dd47-11e9-8d6c-e6452cf5bf03.PNG)

![radius](https://user-images.githubusercontent.com/52009346/65387398-4b76bc80-dd47-11e9-909f-c8c572f2c5c8.PNG)

![heatsource](https://user-images.githubusercontent.com/52009346/65387403-56315180-dd47-11e9-9fd2-0f08a3361513.PNG)

```
References:

- Zhang, Z., Xiong, Y., & Guo, F. (2018). Analysis of Wellbore Temperature Distribution and Influencing Factors During 
Drilling Horizontal Wells. Journal of Energy Resources Technology, 140(9), 092901.

- Chang, X., Zhou, J., Guo, Y., He, S., Wang, L., Chen, Y., ... & Jian, R. (2018). Heat Transfer Behaviors in Horizontal 
Wells Considering the Effects of Drill Pipe Rotation, and Hydraulic and Mechanical Frictions during Drilling Procedures. 
Energies, 11(9), 2414.
```

**For any discussion/contribution regarding the model please check if there is an
[issue](https://github.com/pro-well-plan/pwptemp/issues) covering the same point, otherwise you can open a new one.**
