from coppeliasim_zmqremoteapi_client import RemoteAPIClient

import time
import math

client = RemoteAPIClient()

print('Connected to CoppeliaSim!')

print("program started")

sim = client.getObject('sim')
sim.setStepping(False)
sim.startSimulation()

b1_Handle = sim.getObject("/Sphere[6]")
b2_Handle = sim.getObject("/Cylinder")
b2_pose = sim.getObjectPosition(b2_Handle, b1_Handle)

radius = -1.05
drawing_radius = -1.45

cue_angle = float(input("cue angle: "))
angle_radians = cue_angle * (math.pi / 180) 

force_input = input("Enter the force: ")
force = float(force_input)

torque_input = input("Enter the side spin(-5 to 5):")
torque = float(torque_input)/10

time.sleep(2)
new_pos = sim.getObjectPosition(b1_Handle, sim.handle_world)
target_pos = [new_pos[0] + radius, new_pos[1], new_pos[2]]
new_x = new_pos[0] + radius * math.cos(angle_radians)
new_y = new_pos[1] + radius * math.sin(angle_radians)
target_pos = [new_x, new_y, new_pos[2]] 
sim.setObjectPosition(b2_Handle, sim.handle_world, target_pos)

direction_vector = [new_pos[0] - target_pos[0], new_pos[1] - target_pos[1], 0]

orientation_yaw = math.atan2(direction_vector[1], direction_vector[0])

# Set the object's orientation
current_orient = sim.getObjectOrientation(b2_Handle, sim.handle_world)
new_orient = [1.5, 1.57+orientation_yaw, 1.5]
sim.setObjectOrientation(b2_Handle, sim.handle_world, new_orient)
current_orient = sim.getObjectOrientation(b2_Handle, sim.handle_world)

time.sleep(1)
new_pos = sim.getObjectPosition(b1_Handle, sim.handle_world)
target_pos = [new_pos[0] + drawing_radius, new_pos[1], new_pos[2]]
new_x = new_pos[0] + drawing_radius * math.cos(angle_radians)
new_y = new_pos[1] + drawing_radius * math.sin(angle_radians)
target_pos = [new_x, new_y, new_pos[2]] 
sim.setObjectPosition(b2_Handle, sim.handle_world, target_pos)

time.sleep(1)
new_pos = sim.getObjectPosition(b1_Handle, sim.handle_world)
target_pos = [new_pos[0] + radius, new_pos[1], new_pos[2]]
new_x = new_pos[0] + radius * math.cos(angle_radians)
new_y = new_pos[1] + radius * math.sin(angle_radians)
target_pos = [new_x, new_y, new_pos[2]] 
sim.setObjectPosition(b2_Handle, sim.handle_world, target_pos)


# Calculate the X and Y components of the force vector
force_x = force * math.cos(angle_radians)
force_y = force * math.sin(angle_radians)
force_z = 0

force_vector = [force_x, force_y, force_z]

torque_vector = [0, 0, torque]

# Add a slight delay before applying force to simulate the stick hitting the ball
time.sleep(0.1)

# Apply the force to the ball
sim.addForceAndTorque(b1_Handle, force_vector, torque_vector)

