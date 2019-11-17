# pwptemp.input.data(*casings=[], bit=0.216*) #

Get default parameters.

> **Parameters:**
* **casings: list** - List of dictionaries with casings-related data.
* **bit: float** - Diameter of the hole. *Only required there are not casings.

> **Returns:**

a dictionary with the following default values:
* **tin:**  20
* **ts:** 15
* **wd:** 0
* **ddi:** 0.101
* **ddo:** 0.114
* **dri:** 0.45
* **dro:** 0.5334
* **dfm:** 2
* **q:** 47.696
* **lambdal:** 0.635
* **lambdac:** 43.3
* **lambdacem:** 0.7
* **lambdad:** 40
* **lambdafm:** 2.249
* **lambdar:** 15.49
* **lambdaw:** 0.6
* **cl:** 3713
* **cc:** 469
* **ccem:** 2000
* **cd:** 400
* **cr:** 464
* **cw:** 4000
* **cfm:** 800
* **h1:** 1800
* **h2:** 2000
* **h3:** 200
* **h3r:** 200
* **rhol:** 1198
* **rhod:** 7600
* **rhoc:** 7800
* **rhor:** 7800
* **rhofm:** 2245
* **rhow:** 1029
* **rhocem:** 2700
* **gt:** 0.0238
* **wtg:** -0.005
* **rpm:** 100
* **t:** 2
* **tbit:** 1.35
* **wob:** 22.41
* **rop:** 14.4
* **an:** 2
* **casings:** array with casings-related data [[od, id, depth]]

## Example ##

```
>>> casings = [{'od': 0.24, 'id': 0.216, 'depth': 2500}, {'od': 0.66, 'id': 0.63, 'depth': 1000}]
>>> data = pwptemp.input.data(casings)
>>> print(data['ts'])
15
>>> print(data['casings'])
[[0.24, 0.216, 2500], [0.66, 0.63, 1000]]
```

See the [pwptemp.input](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.input.md) documentation.
