from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from time import sleep as delay
import numpy as np
import cv2

# Create client and request simulation service
client = RemoteAPIClient()
sim = client.require('sim')

# Retrieve the motor handles
left_motor_handle = sim.getObject('/leftMotor')
right_motor_handle = sim.getObject('/rightMotor')

# Retrieve the camera handle
camera_handle = sim.getObject('/cam1')

# Start the simulation
sim.startSimulation()

delay(1)

print("Program Started!")

# Setup for image streaming and camera data retrieval
try:
    while True:
        img, [resX, resY] = sim.getVisionSensorImg(camera_handle)
        img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)

        # In CoppeliaSim images are left to right (x-axis), and bottom to top (y-axis)
        # and color format is RGB triplets, whereas OpenCV uses BGR:
        img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)

        # Resize the image to a larger size
        img = cv2.resize(img, (resX * 5, resY * 5))  # Scale up by 2x
        cv2.imshow('', img)

        # Check for user key input
        key = cv2.waitKey(1)

        # Motor control logic based on key input
        if key == ord('q'):
            break
        elif key == ord('w'):
            lSpeed = 1
            rSpeed = 1
        elif key == ord('a'):
            lSpeed = -0.1
            rSpeed = 1
        elif key == ord('d'):
            lSpeed = 1
            rSpeed = -0.1
        elif key == ord('s'):
            lSpeed = -1
            rSpeed = -1
        else:
            lSpeed = 0
            rSpeed = 0

        # Set the motor speeds
        sim.setJointTargetVelocity(left_motor_handle, lSpeed)
        sim.setJointTargetVelocity(right_motor_handle, rSpeed)

    # Clean up
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")
    cv2.destroyAllWindows()

# Stop the simulation
sim.stopSimulation()

print("Program Ended")
