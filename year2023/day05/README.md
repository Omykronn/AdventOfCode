# STEP 2 : Explanation
 
Instead of calculating each value in each intervals (calculating time skyrocketing), it treats each interval with its endpoints. But the maps might not respect the endpoints of an interval, so one interval might be divided in smaller intervals (but their union is still equal to the first interval).
At the end, the smallest inferior endpoint is the answer.

All of this is possible because the maps represent 1-slope linear function.