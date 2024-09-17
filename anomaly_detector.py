import numpy as np
from financial_data_simulator import simulate_financial_data_stream
from data_visualizer import DataVisualizer
import threading
import time
import matplotlib.pyplot as plt
import datetime

class AnomalyDetector:
    def __init__(self, window_size=100, threshold=3):
        self.window_size = window_size
        self.threshold = threshold
        self.values = []
        
    def detect(self, value):
        self.values.append(value)
        
        if len(self.values) > self.window_size:
            self.values.pop(0)
        
        if len(self.values) < self.window_size:
            return False  # Not enough data yet
        
        mean = np.mean(self.values)
        std = np.std(self.values)
        
        if std == 0:
            return False  # Avoid division by zero
        
        z_score = (value - mean) / std
        
        return abs(z_score) > self.threshold

def process_data(data_stream, detector, visualizer, stop_event):
    print("Data processing started...")
    try:
        for amount in data_stream:
            if stop_event.is_set():
                print("Stop event detected, ending data processing.")
                break

            timestamp = datetime.datetime.now()
            is_anomaly = detector.detect(amount)
            print(f"Processing: Timestamp: {timestamp}, Amount: ${amount:.2f}, Anomaly: {'Yes' if is_anomaly else 'No'}")
            visualizer.add_point(timestamp, amount, is_anomaly)

            time.sleep(0.1)  # Simulate real-time delay
    except Exception as e:
        print(f"Error in process_data: {e}")
    finally:
        print("Data processing ended.")

def main():
    print("Starting main function...")
    data_stream = simulate_financial_data_stream()
    detector = AnomalyDetector()
    visualizer = DataVisualizer()

    stop_event = threading.Event()

    print("Starting data processing thread...")
    data_thread = threading.Thread(target=process_data, args=(data_stream, detector, visualizer, stop_event))
    data_thread.daemon = True
    data_thread.start()

    print("Starting animation...")
    visualizer.animate()

    print("Showing plot...")
    try:
        plt.show(block=False)
        
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("Keyboard interrupt detected.")
    finally:
        print("Stopping data processing...")
        stop_event.set()
        data_thread.join(timeout=2)
        print("Data thread joined.")
        
        print("Saving data to CSV...")
        visualizer.save_data('transaction_data.csv')
        
        print("\nData processing has stopped and data has been saved.")
        print("You can still inspect the plot.")
        print("Close the plot window to exit the program.")
        
        plt.show(block=True)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred in main: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Program finished.")