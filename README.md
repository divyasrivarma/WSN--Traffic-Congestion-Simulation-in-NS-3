# 🚦 Traffic Congestion Simulation using SUMO & Python

## 📌 Overview
This project simulates urban traffic using SUMO (Simulation of Urban Mobility) and analyzes vehicle behavior using Python. The system collects real-time vehicle data and visualizes traffic patterns such as speed variation over time.

## 🎯 Objectives
- Simulate real-time traffic flow
- Analyze vehicle speeds and traffic behavior
- Visualize traffic data using graphs
- Understand congestion patterns

## 🛠️ Technologies Used
- SUMO – Traffic simulation
- Python – Data collection & analysis
- TraCI – Interface between SUMO and Python
- Matplotlib – Data visualization
- NS-3 – Network simulation (conceptual integration)

## 📂 Project Structure
traffic-project/
│── map.net.xml          # Road network file  
│── routes.rou.xml       # Vehicle routes  
│── trips.trips.xml      # Trip definitions (optional)  
│── map.sumocfg          # Configuration file  
│── simulation.py        # Python script (TraCI + analysis)  
│── traffic_graph.png    # Output graph  

## ⚙️ How It Works
1. SUMO loads the network and route files.  
2. Vehicles move based on predefined routes.  
3. Python (TraCI) connects to SUMO in real-time.  
4. Vehicle speed data is collected at each step.  
5. Data is plotted as a graph for analysis.  

## ▶️ How to Run
1. Install SUMO and set environment variables.  
2. Install required library:
   pip install matplotlib  
3. Run the simulation:
   python simulation.py  

## 📊 Output
- Graph showing Vehicle Speed vs Time Step  
- Helps analyze traffic flow, speed variation, and congestion patterns  

## 📈 Sample Result
The output graph is saved as:
traffic_graph.png  

## 🚀 Future Improvements
- Add real-time traffic prediction using AI  
- Integrate IoT sensor data  
- Expand simulation to city-scale traffic  
- Add multiple routes and vehicle types  

