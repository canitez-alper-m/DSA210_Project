
# DSA 210 Project - Traffic Congestion and Air Quality Analysis
# Code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Step 1: Data Collection (Unfinished)
np.random.seed(42)
dates = pd.date_range(start='2024-03-01', end='2024-03-31', freq='H')

traffic_congestion = np.random.normal(loc=50, scale=15, size=len(dates))
traffic_congestion = np.clip(traffic_congestion, 10, 100)

wind_speed = np.random.normal(loc=10, scale=3, size=len(dates))
wind_speed = np.clip(wind_speed, 0, 25)

temperature = np.random.normal(loc=20, scale=5, size=len(dates))

aqi = 30 + 0.7 * traffic_congestion - 1.2 * wind_speed + np.random.normal(loc=0, scale=10, size=len(dates))
aqi = np.clip(aqi, 0, 500)

data = pd.DataFrame({
    'Datetime': dates,
    'Traffic_Congestion': traffic_congestion,
    'Wind_Speed': wind_speed,
    'Temperature': temperature,
    'AQI': aqi
})

# Save the dataset (optional)
data.to_csv('traffic_air_quality_data.csv', index=False)

# Step 2: Exploratory Data Analysis

# Summary statistics
print("Summary Statistics:")
print(data.describe())

# Correlation Matrix
plt.figure(figsize=(8,6))
sns.heatmap(data[['Traffic_Congestion', 'Wind_Speed', 'Temperature', 'AQI']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.show()

# Scatter Plot of Traffic Congestion vs AQI
plt.figure(figsize=(6,4))
plt.scatter(data['Traffic_Congestion'], data['AQI'], alpha=0.5)
plt.xlabel('Traffic Congestion (%)')
plt.ylabel('Air Quality Index (AQI)')
plt.title('Traffic Congestion vs AQI')
plt.grid(True)
plt.tight_layout()
plt.savefig('scatter_traffic_aqi.png')
plt.show()

# Line Plot: AQI change Over Time
plt.figure(figsize=(12,4))
plt.plot(data['Datetime'], data['AQI'])
plt.xlabel('Date')
plt.ylabel('Air Quality Index (AQI)')
plt.title('AQI Over Time')
plt.grid(True)
plt.tight_layout()
plt.savefig('aqi_over_time.png')
plt.show()

# Step 3: Hypothesis Testing

# Define median traffic level
median_traffic = data['Traffic_Congestion'].median()

# Separate AQI into high and low traffic groups
high_traffic_aqi = data[data['Traffic_Congestion'] >= median_traffic]['AQI']
low_traffic_aqi = data[data['Traffic_Congestion'] < median_traffic]['AQI']

# Perform t-test
t_stat, p_value = ttest_ind(high_traffic_aqi, low_traffic_aqi)

print("\nHypothesis Test Results:")
print(f"t-statistic: {round(t_stat, 3)}")
print(f"p-value: {round(p_value, 5)}")

if p_value < 0.05:
    print("Conclusion: Reject H0. High traffic significantly increases AQI.")
else:
    print("Conclusion: Fail to reject H0. No significant difference detected.")
