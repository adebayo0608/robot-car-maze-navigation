from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

# Create client and request simulation service
client = RemoteAPIClient()
sim = client.require('sim')

file_path = r"C:\Users\adeba\OneDrive - University of Aberdeen\UOA\24-25\Semester 1\EG505P\Assessment\Maze.ttt"
sim.loadScene(file_path)

sim.startSimulation()
print("Program Started")

# Controlling the motors
# Retrieve the motor handles
left_motor_handle = sim.getObject('/leftMotor')
right_motor_handle = sim.getObject('/rightMotor')

# Set Motor Velocities
sim.setJointTargetVelocity(left_motor_handle, 0.5)
sim.setJointTargetVelocity(right_motor_handle, 0.5)

# Allow the robot to move for a few seconds
time.sleep(5)  # Run for 5 seconds to see the robot move

# Stop the simulation
sim.stopSimulation()
