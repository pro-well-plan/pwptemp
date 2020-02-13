# pwptemp.drilling.input_info(*about='all'*) #

Get information about the parameters involved.

> **Parameters:**
*  **about:** *string, default 'all'*
    - 'tubular': values related to tubular sizes
    - 'conditions': parameters related to simulation conditions
    - 'heatcoeff': parameters related to heat coefficients
    - 'densities': parameters related to densities
    - 'operational': parameters related to the operation
    - 'all': all the parameters

> **Returns:**

Print the information related with the parameters.

## Example ##

```
>>> import pwptemp.drilling as ptd
>>> ptd.input_info(about='operational')
Use the ID of a parameter to change the default value (e.g. tdict['tin']=30 to change the fluid inlet temperature from the default value to 30° Celsius)
Notice that the information is provided as follows:
parameter ID: general description, units

PARAMETERS RELATED TO THE OPERATION
tin: fluid inlet temperature, °C
q: flow rate, lpm
rpm: revolutions per minute
t: torque on the drill string, kN*m
tbit: torque on the bit, kN*m
wob: reight on bit, kN
rop: rate of penetration, m/h
an: area of the nozzles, in2
```

See the [pwptemp.drilling](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.drilling.md) documentation.
