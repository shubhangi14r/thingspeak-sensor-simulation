# ThingSpeak Sensor Data Simulation

This project simulates sending temperature,humidity,pressure and light intensity data to [ThingSpeak](https://thingspeak.com/) using Python. The script generates random sensor values and sends them to a ThingSpeak channel at regular intervals.

---

# Features
- Simulates sensor data (Temperature,Humidity,Pressure & Light Intensity).
- Sends data to ThingSpeak using `requests`.
- Runs continuously, sending new data every **15 seconds**.
- Uses ThingSpeak API for real-time IoT data visualization.

---

# Prerequisites
Ensure you have the following installed:

- Python (version 3.6+ recommended)
- Required Python library: `requests`
  ```bash
  pip install requests
  ```
- A **ThingSpeak account** and a **Write API Key** (from your ThingSpeak channel).

---

# Setup & Usage
1. **Clone the repository** (or download the `thingspeak_simulation.py` file):
   ```bash
   git clone https://github.com/yourusername/thingspeak-simulation.git
   cd thingspeak-simulation
   ```

2. **Edit the script** (`thingspeak_simulation.py`) and replace `YOUR_WRITE_API_KEY` with your actual **ThingSpeak Write API Key**.

3. **Run the script**:
   ```bash
   python thingspeak_simulation.py
   ```

4. **Check your ThingSpeak channel** to view the **real-time data** visualization.

---

# Live Data
You can see the live sensor data here: [ThingSpeak Live Channel](https://thingspeak.mathworks.com/channels/2898487)

---

# Author
**Shubhangi Ranjan**  
