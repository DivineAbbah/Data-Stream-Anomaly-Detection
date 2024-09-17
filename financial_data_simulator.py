import random
import time
from datetime import datetime

def generate_transaction(base_amount, noise_level, seasonal_factor, anomaly_probability):
    amount = base_amount + random.uniform(-noise_level, noise_level)
    amount *= seasonal_factor
    
    is_anomaly = random.random() < anomaly_probability
    if is_anomaly:
        amount *= random.uniform(5, 10)  # Anomaly: 5x to 10x normal amount
    
    return round(amount, 2)

def simulate_financial_data_stream():
    base_amount = 1000  # Base transaction amount
    noise_level = 100   # Random noise in transaction amounts
    anomaly_probability = 0.01  # 1% chance of anomaly
    
    while True:
        # Simulate seasonal patterns (e.g., higher transactions during business hours)
        hour = datetime.now().hour
        seasonal_factor = 1 + 0.5 * (6 <= hour < 18)  # 50% increase during 6 AM to 6 PM
        
        amount = generate_transaction(base_amount, noise_level, seasonal_factor, anomaly_probability)
        yield amount
        
        time.sleep(0.1)  # Simulate real-time delay