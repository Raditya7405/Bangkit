# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better visuals
sns.set(style="whitegrid")

# Load the dataset
day_data = pd.read_csv('day.csv')

# Filter Data by working day or holiday
def filter_data(day_data, working_day_filter, season_filter):
    # Filter for working day or holiday
    if working_day_filter == "Working Day":
        filtered_data = day_data[day_data['workingday'] == 1]
    else:
        filtered_data = day_data[day_data['holiday'] == 1]

    # Filter for season
    if season_filter != "All":
        season_mapping = {"Winter": 1, "Spring": 2, "Summer": 3, "Fall": 4}
        filtered_data = filtered_data[filtered_data['season'] == season_mapping[season_filter]]
    
    return filtered_data

# Function to visualize the results
def plot_bike_usage(filtered_data, working_day_filter, season_filter):
    # Plot total bike rentals over time
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data['dteday'], filtered_data['cnt'], color='b')
    plt.xlabel('Date')
    plt.ylabel('Total Bike Rentals')
    plt.title(f'Total Bike Rentals Over Time - {working_day_filter} ({season_filter})')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot average rentals by day of the week
    avg_rentals_by_weekday = filtered_data.groupby('weekday')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=avg_rentals_by_weekday.index, y=avg_rentals_by_weekday.values, palette="Set2")
    plt.xlabel('Day of the Week (0 = Sunday, 6 = Saturday)')
    plt.ylabel('Average Bike Rentals')
    plt.title(f'Average Bike Rentals by Day of the Week - {working_day_filter}')
    plt.tight_layout()
    plt.show()

    # Weather analysis
    weather_counts = filtered_data.groupby('weathersit')['cnt'].mean()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=weather_counts.index, y=weather_counts.values)
    plt.xlabel("Weather Condition (1 = Clear, 2 = Mist, 3 = Light Rain)")
    plt.ylabel("Average Bike Rentals")
    plt.title(f'Average Bike Rentals by Weather Condition - {working_day_filter}')
    plt.tight_layout()
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    correlation = filtered_data.drop(columns=['dteday']).corr()
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()

# Main function
def main():
    # Set working day or holiday filter
    working_day_filter = "Working Day"  # or "Holiday"
    
    # Set season filter
    season_filter = "All"  # options: "Winter", "Spring", "Summer", "Fall", "All"
    
    # Filter the data based on the selection
    filtered_data = filter_data(day_data, working_day_filter, season_filter)
    
    # Display summary statistics
    print(f"Summary Statistics: {working_day_filter} - {season_filter}")
    print(filtered_data.describe())

    # Generate visualizations
    plot_bike_usage(filtered_data, working_day_filter, season_filter)
    
    # Conclusion
    print("Conclusion:")
    print(f"Based on the selected filters ({working_day_filter}, {season_filter}), bike usage is influenced by working days and weather conditions.")

# Run the main function
if __name__ == "__main__":
    main()
