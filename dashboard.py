# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better visuals
sns.set(style="whitegrid")

# Load the dataset
day_data = pd.read_csv('day.csv')

# Function to visualize the results
def plot_bike_usage(day_data):
    # Plot total bike rentals over time
    plt.figure(figsize=(10, 6))
    plt.plot(day_data['dteday'], day_data['cnt'], color='b')
    plt.xlabel('Date')
    plt.ylabel('Total Bike Rentals')
    plt.title(f'Total Bike Rentals Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot average rentals by day of the week
    avg_rentals_by_weekday = day_data.groupby('weekday')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=avg_rentals_by_weekday.index, y=avg_rentals_by_weekday.values, palette="Set2")
    plt.xlabel('Day of the Week (0 = Sunday, 6 = Saturday)')
    plt.ylabel('Average Bike Rentals')
    plt.title(f'Average Bike Rentals by Day of the Week')
    plt.tight_layout()
    plt.show()

    # Weather analysis
    weather_counts = day_data.groupby('weathersit')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=weather_counts.index, y=weather_counts.values)
    plt.xlabel("Weather Condition (1 = Clear, 2 = Mist, 3 = Light Rain)")
    plt.ylabel("Average Bike Rentals")
    plt.title(f'Average Bike Rentals by Weather Condition')
    plt.tight_layout()
    plt.show()

    # Histogram of bike rentals
    plt.figure(figsize=(8, 6))
    sns.histplot(day_data['cnt'], bins=20, kde=True)
    plt.xlabel('Total Bike Rentals')
    plt.ylabel('Frequency')
    plt.title('Distribution of Total Bike Rentals')
    plt.tight_layout()
    plt.show()

# Main function
def main():
    # Display summary statistics
    print("Summary Statistics:")
    print(day_data.describe())

    # Generate visualizations
    plot_bike_usage(day_data)
    
    # Analysis and Conclusion
    print("\nAnalysis and Insights:")
    print("1. Bike usage tends to be higher on working days compared to holidays, indicating the service is popular among commuters.")
    print("2. Weekdays see a steadier bike rental trend, with slight peaks on weekends.")
    print("3. Weather plays a significant role in bike rentals, with clear weather (condition 1) showing the highest usage.")
    print("4. The distribution of total bike rentals shows that most days see moderate bike usage, with some high-demand days.")

# Run the main function
if __name__ == "__main__":
    main()
