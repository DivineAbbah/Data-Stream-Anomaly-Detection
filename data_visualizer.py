import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import csv
from datetime import datetime, timedelta
import threading

class DataVisualizer:
    def __init__(self):
        self.timestamps = []
        self.amounts = []
        self.anomalies = []
        self.lock = threading.Lock()
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.line, = self.ax.plot([], [], lw=2, label='Transactions')
        self.scatter = self.ax.scatter([], [], color='red', s=100, label='Anomalies')
        self.ax.legend()
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Amount ($)')
        self.ax.set_title('Financial Transactions with Anomaly Detection')
        self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
        self.ax.xaxis.set_major_locator(mdates.SecondLocator(interval=30))
        plt.gcf().autofmt_xdate()
        self.last_data_count = 0

    def init_plot(self):
        now = datetime.now()
        self.ax.set_xlim(mdates.date2num(now), 
                         mdates.date2num(now + timedelta(minutes=5)))
        self.ax.set_ylim(0, 2000)
        return self.line, self.scatter

    def update(self, frame):
        with self.lock:
            if not self.timestamps:
                return self.line, self.scatter

            x = mdates.date2num(self.timestamps)
            y = self.amounts

            if len(x) != self.last_data_count:
                print(f"Debug - Data points: {len(x)}, Anomalies: {sum(self.anomalies)}")
                self.last_data_count = len(x)

            self.line.set_data(x, y)

            anomaly_mask = np.array(self.anomalies, dtype=bool)
            anomaly_x = np.array(x)[anomaly_mask]
            anomaly_y = np.array(y)[anomaly_mask]
            self.scatter.set_offsets(np.column_stack((anomaly_x, anomaly_y)))

            self.ax.relim()
            self.ax.autoscale_view()

            if len(self.timestamps) > 0:
                window = timedelta(minutes=5)
                self.ax.set_xlim(max(self.timestamps[0], self.timestamps[-1] - window),
                                 self.timestamps[-1] + timedelta(seconds=10))
                self.ax.set_ylim(0, max(max(self.amounts) * 1.1, 2000))

        return self.line, self.scatter

    def animate(self):
        self.anim = FuncAnimation(self.fig, self.update, init_func=self.init_plot,
                                  frames=None, interval=100, blit=True, cache_frame_data=False)

    def add_point(self, timestamp, amount, is_anomaly):
        with self.lock:
            self.timestamps.append(timestamp)
            self.amounts.append(amount)
            self.anomalies.append(is_anomaly)
        print(f"Added point: {timestamp}, {amount}, {'Anomaly' if is_anomaly else 'Normal'}")

    def save_data(self, filename):
        with self.lock:
            with open(filename, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['Timestamp', 'Amount', 'Is Anomaly'])
                for timestamp, amount, is_anomaly in zip(self.timestamps, self.amounts, self.anomalies):
                    csvwriter.writerow([timestamp.strftime('%Y-%m-%d %H:%M:%S'), amount, is_anomaly])
        print(f"Data saved to {filename}")