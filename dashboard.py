# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set seaborn style for better visuals
sns.set(style="whitegrid")

# Load the dataset
day_data = pd.read_csv('day.csv')

# Function to visualize the results
def plot_bike_usage(day_data):
    # Plot total bike rentals over time
    st.write("### Total Bike Rentals Over Time")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(day_data['dteday'], day_data['cnt'], color='b')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Bike Rentals')
    ax.set_title('Total Bike Rentals Over Time')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Plot average rentals by day of the week
    st.write("### Average Bike Rentals by Day of the Week")
    avg_rentals_by_weekday = day_data.groupby('weekday')['cnt'].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=avg_rentals_by_weekday.index, y=avg_rentals_by_weekday.values, palette="Set2", ax=ax)
    ax.set_xlabel('Day of the Week (0 = Sunday, 6 = Saturday)')
    ax.set_ylabel('Average Bike Rentals')
    ax.set_title('Average Bike Rentals by Day of the Week')
    st.pyplot(fig)

    # Weather analysis
    st.write("### Average Bike Rentals by Weather Condition")
    weather_counts = day_data.groupby('weathersit')['cnt'].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=weather_counts.index, y=weather_counts.values, ax=ax)
    ax.set_xlabel("Weather Condition (1 = Clear, 2 = Mist, 3 = Light Rain)")
    ax.set_ylabel("Average Bike Rentals")
    ax.set_title('Average Bike Rentals by Weather Condition')
    st.pyplot(fig)

    # Histogram of bike rentals
    st.write("### Distribution of Total Bike Rentals")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(day_data['cnt'], bins=20, kde=True, ax=ax)
    ax.set_xlabel('Total Bike Rentals')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Total Bike Rentals')
    st.pyplot(fig)

# Main function
def main():
    st.title("Bike Sharing Data Analysis")
    
    # Display summary statistics
    st.write("## Summary Statistics")
    st.write(day_data.describe())

    # Generate visualizations
    plot_bike_usage(day_data)
    
    # Analysis and Conclusion
    st.write("## Analysis and Insights")
    st.write("""
    1. Bike usage tends to be higher on working days compared to holidays, indicating the service is popular among commuters.
    2. Weekdays see a steadier bike rental trend, with slight peaks on weekends.
    3. Weather plays a significant role in bike rentals, with clear weather (condition 1) showing the highest usage.
    4. The distribution of total bike rentals shows that most days see moderate bike usage, with some high-demand days.
    """)

# Run the main function
if __name__ == "__main__":
    main()
