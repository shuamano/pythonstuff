import math

upper_arm_length = 5
forearm_length = 5

move_to = [3, -4] #these are the coords we want the arm to move to

#a squared + b squared = c squared (hypotinuse squared)
new_squared_hypotinuse = move_to[0] ** 2 +  move_to[1] ** 2
new_hypotinuse = math.sqrt(new_squared_hypotinuse)

#add this angle (cos rly) to the "shoulder"(upper arm pivot) angle to get the correct angle from the ground
add_angle_cos = ((new_hypotinuse **2) + (move_to[0] **2) - (move_to[1] **2)) / (2 * new_hypotinuse * move_to[0])
#this is the angle to add to angle A1 (upper arm pivot)
angle_to_add = math.degrees(math.acos(add_angle_cos)) # look at that nice clean code (eh) but now its not radians

upper_arm_cos = ((upper_arm_length **2) + (new_hypotinuse **2) - (forearm_length **2)) / (2 * upper_arm_length * new_hypotinuse)
upper_arm_angle = math.degrees(math.acos(upper_arm_cos))

#actual angle for the first joint!!
real_upper_arm_angle = upper_arm_angle + angle_to_add
print(f"This is the angle for the bottom pivot:\n{real_upper_arm_angle}")

forearm_cos = ((forearm_length **2) + (upper_arm_length **2) - (new_hypotinuse **2)) / (2 * forearm_length * upper_arm_length)
real_forearm_angle = math.degrees(math.acos(forearm_cos))
print(f"\nThis is the angle for the 2nd pivot:\n{real_forearm_angle}")
