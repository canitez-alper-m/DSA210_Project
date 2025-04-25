/# DSA210_Project
**DSA 210 Project Proposal: The Impact of Traffic Congestion on Air Quality in Turkiye**

### **Motivation Behind This Project**
Air pollution is a major environmental concern in Turkey, particularly in urban centers such as Istanbul, Ankara, and Izmir, where traffic congestion is a critical issue. Emissions from vehicles contribute significantly to poor air quality, affecting public health and living standards in big cities. This project aims to analyze the relationship between traffic congestion and air pollution, exploring how factors such as time of day, weather conditions, and urban density influence air quality. By identifying patterns and correlations, this research can provide valuable insights to improve air quality and traffic management.

### **Data Sources**
The dataset will be formed according to three primary sources:
- **Air Quality Data:** The Turkish Ministry of Environment, Urbanization, and Climate Change provides live and historical Air Quality Index (AQI) data for major cities using its "Hava İzleme Portalı".
- **Traffic Congestion Data:** Google Maps Traffic API and Istanbul Metropolitan Municipality (İBB) Open Data Portal offer live and historical traffic congestion data for highly-used roads and intersections.
- **Weather Data (Enrichment Factor):** The Turkish State Meteorological Service (MGM) provides hourly temperature, wind speed, humidity, and precipitation data, which will be used to examine the impact of weather conditions on pollution levels.

### **Data Analysis**
1. **Data Cleaning:**
   - Handling missing or inconsistent values inside  datasets.
   - Synchronizing timestamps to align Air Quality İndex (AQI), traffic, and weather data for accurate correlation analysis.
2. **Exploratory Data Analysis:**
   - Examining trends in AQI levels and traffic congestion over different times of the day, weekdays vs. weekends, and seasonal variations.
   - Identifying high-risk pollution zones and their correlation with high-traffic areas.
3. **Hypothesis Testing:**
   - Testing whether increased traffic congestion leads to significant increases in AQI levels.
   - Analyzing the impact of weather conditions (e.g., wind speed, temperature) on pollution dispersion.
  

# The Code and Hypothesis Testing  
# DSA 210 Project - Traffic Congestion and Air Quality


# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

#Step 1: Load Your Real Dataset

# Dataset goes here
# The CSV should have columns Datetime, Traffic_Congestion, Wind_Speed, Temperature, AQI

data = pd.read_csv('your_data.csv')

# Check if data is loaded properly
print("Data Sample:")
print(data.head())

#Step 2: Exploratory Data Analysis (EDA)

# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

#Correlation matrix
plt.figure(figsize=(8,6))
sns.heatmap(data[['Traffic_Congestion', 'Wind_Speed', 'Temperature', 'AQI']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Scatter plot: Traffic vs AQI
plt.figure(figsize=(6,4))
plt.scatter(data['Traffic_Congestion'], data['AQI'], alpha=0.5)
plt.xlabel('Traffic Congestion (%)')
plt.ylabel('Air Quality Index (AQI)')
plt.title('Traffic Congestion vs AQI')
plt.grid(True)
plt.show()

# Line plot: AQI over time
plt.figure(figsize=(12,4))
plt.plot(pd.to_datetime(data['Datetime']), data['AQI'])
plt.xlabel('Date')
plt.ylabel('Air Quality Index (AQI)')
plt.title('AQI Over Time')
plt.grid(True)
plt.show()

# --- Step 3: Hypothesis Testing ---

# Hypothesis:
# H0: High traffic congestion does not increase AQI significantly.
# H1: High traffic congestion increases AQI significantly.

# Find the median traffic value
median_traffic = data['Traffic_Congestion'].median()

# Separate AQI values into high and low traffic groups
high_traffic_aqi = data[data['Traffic_Congestion'] >= median_traffic]['AQI']
low_traffic_aqi = data[data['Traffic_Congestion'] < median_traffic]['AQI']

# Perform t-test
t_stat, p_value = ttest_ind(high_traffic_aqi, low_traffic_aqi)

print("\nHypothesis Test Result:")
print(f"t-statistic: {round(t_stat, 3)}")
print(f"p-value: {round(p_value, 5)}")

if p_value < 0.05:
    print("Conclusion: Reject H0. High traffic significantly increases AQI.")
else:
    print("Conclusion: Fail to reject H0. No significant difference detected.")

# --- Step 4: Interpretation ---

print("\nInterpretation:")
print("- Traffic Congestion and AQI seem positively correlated.")
print("- Higher Traffic is likely linked to worse Air Quality.")
print("- Wind Speed might help reduce AQI based on correlation matrix.")




