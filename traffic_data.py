import traci
import matplotlib.pyplot as plt

# Start SUMO with config file
traci.start(["sumo", "-c", "map.sumocfg"])

vehicle_speeds = []
steps = []

step = 0

# Run simulation until all vehicles are done
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    vehicles = traci.vehicle.getIDList()

    print(f"Step {step}: Vehicles = {vehicles}")

    for v in vehicles:
        speed = traci.vehicle.getSpeed(v)
        print(f"Vehicle {v} Speed: {speed}")

        # Store data for graph
        vehicle_speeds.append(speed)
        steps.append(step)

    step += 1

# Close TraCI safely
traci.close()

# Plot graph
plt.figure()
plt.plot(steps, vehicle_speeds)
plt.xlabel("Time Step")
plt.ylabel("Vehicle Speed")
plt.title("Traffic Speed Analysis")
plt.grid()

# Save graph (for report/demo)
plt.savefig("traffic_graph.png")

# Show graph
# plt.show(block=True)