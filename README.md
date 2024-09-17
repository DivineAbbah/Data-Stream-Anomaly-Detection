# Efficient Data Stream Anomaly Detection

## Project Overview
This project implements a real-time anomaly detection system for continuous data streams,i chose to focus on financial transactions as i am inclined with it. It simulates a stream of data and uses a statistical approach to identify unusual patterns or outliers that could indicate fraudulent activity or system anomalies.

## Features
- Real-time simulation of data streams (e.g., financial transactions)
- Anomaly detection using Moving Average with Standard Deviation
- Real-time visualization of the data stream and detected anomalies
- Efficient processing optimized for continuous data streams
- Ability to adapt to concept drift and seasonal variations
- CSV export of all transactions and detected anomalies for further analysis and traceability

## Algorithm Selection
For this project task, I chose to implement the Moving Average with Standard Deviation algorithm for anomaly detection. This approach was selected for several reasons:

1. Adaptability: By using a moving window, the algorithm can adapt to gradual changes in the data distribution (concept drift) and seasonal variations.
2. Efficiency: The algorithm has a low computational complexity, allowing it to process high-frequency data in real-time without significant lag.
3. Effectiveness: This method is particularly good at detecting sudden spikes which i one main reason i chose this alogrithm.
4. Simplicity and Interpretability: Because of time constraint, and when to submit this task i chose this algorithm because it is straightforward to implement and understand, making it easier to maintain and explain.

The algorithm works by maintaining a moving window of recent data points. For each new data point, it calculates the mean and standard deviation of the values in this window. If the new value deviates from the mean by more than a specified number of standard deviations, it is flagged as an anomaly.

## Project Structure
- `anomaly_detector.py`: Main script that ties together all components
- `financial_data_simulator.py`: Simulates a stream of data (e.g., financial transactions)
- `data_visualizer.py`: Provides real-time visualization of the data and detected anomalies
- `transaction_data.csv`: Generates a CSV file containing all transactions and anomaly flags

## Setup and Running the Project

### Prerequisites
- Python 3.x

### Installation
1. Clone or download this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Create and activate a virtual environment (this is optional if you dont want to):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Project
Execute the following command in your terminal:

```
python anomaly_detector.py
```

This will start the simulation, it would show the stream data of transactions which include the timestamp, amount and also the status of the transaction if it is an anomaly and flag it as yes or no, and open a real-time visualization of the data stream and detected anomalies. When you stop the program (e.g., by pressing Ctrl+C), it would save all the transaction data to transaction_data.csv and display the plots showing the anomalies using red points, a pictorial representation is included on the project directory. The good thing is been able to see the visualization plot after ending the stream process using ctrl+c on the terminal.

## Implementation Details

### Data Stream Simulation
The `simulate_financial_data_stream` function in `financial_data_simulator.py` emulates a data stream with the following characteristics:
- Regular patterns: Base transaction amounts with random noise
- Seasonal elements: Higher transaction volumes during business hours
- Random noise: Small variations in transaction amounts
- Anomalies: Occasional large deviations from normal patterns

### Anomaly Detection Mechanism
The `AnomalyDetector` class in `anomaly_detector.py` implements the real-time anomaly detection:
- It maintains a moving window of recent data points
- It calculates mean and standard deviation for each window
- It flags data points that deviate significantly from the mean

### Optimization
The optimization of this project is very neccessary so i implemented this task:
- Using NumPy for fast numerical computations
- Implementing a circular buffer for the moving window to avoid unnecessary data shifting

### Visualization
The `DataVisualizer` class in `data_visualizer.py` creates a real-time plot:
- It displays the continuous data stream
- It highlights detected anomalies
- It updates in real-time as new data points arrive

## Error Handling and Data Validation
- Input validation in the `AnomalyDetector` class ensures valid window size and threshold
- Error handling in data processing prevents crashes due to unexpected data values
- The visualization component handles varying data ranges and time scales


## Conclusion
This project demonstrates an efficient approach to detecting anomalies in a continuous data stream. It focuses on the objective of the task i was given which is identifying unusual patterns, such as exceptionally high values or deviations from the norm.