The physical modelling involves modelling for shaft, bearing, gear, pinion, ball bearing and to some extent the retainer

For  shaft, bearing, gear, pinion the model from following paper is used:

https://pure.hud.ac.uk/ws/portalfiles/portal/38979035/Revised_MSSP21_350_Bearing_clearance_monitoring.pdf

Additionally for ball bearing and cage the model from following paper is used and combined with above model

https://www.mdpi.com/2075-4442/10/1/9

The [description.ipynb](https://github.com/im-ajaymeena/Spur-Gear-Vibration-Modelling/blob/main/description.ipynb) shows the equations formulated for modelling

The unknown parameters should be chosen in a such that to have Under-damped oscillation:
<img src="https://raw.githubusercontent.com/im-ajaymeena/Spur-Gear-Vibration-Modelling/main/src/data/under_damping_condition.png" alt="Under damping">

In case of some random parameters we got the following graphs:

<img src="https://raw.githubusercontent.com/im-ajaymeena/Spur-Gear-Vibration-Modelling/main/src/data/sample_output1.png" alt="Sample Output 1">

<img src="https://raw.githubusercontent.com/im-ajaymeena/Spur-Gear-Vibration-Modelling/main/src/data/sample_output2.png" alt="Sample Output 2">

<img src="https://raw.githubusercontent.com/im-ajaymeena/Spur-Gear-Vibration-Modelling/main/src/data/sample_output3.png" alt="Sample Output 3">

<img src="https://raw.githubusercontent.com/im-ajaymeena/Spur-Gear-Vibration-Modelling/main/src/data/sample_output4.png" alt="Sample Output 4">
