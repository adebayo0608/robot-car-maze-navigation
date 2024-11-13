from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import cv2

# Create client and request simulation service
client = RemoteAPIClient()
sim = client.require('sim')

# Enable step-wise simulation
sim.setStepping(True)

# Run simulation for 3 seconds
sim.startSimulation()
while (t := sim.getSimulationTime()) < 3:
    print(f'Simulation time: {t:.2f} [s]')
    sim.step()

sim.stopSimulation()