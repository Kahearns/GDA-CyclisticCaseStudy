import pandas as pd

# Load the cleaned CSV file
cleaned_file_path = "/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/cleaned_cyclistic_data.csv"
df_cleaned = pd.read_csv(cleaned_file_path)


# Each of the following sections will output to their own file for processing.


# ================================
# 1. Bike types used by riders
# ================================
bike_types_used = df_cleaned.groupby(['member_casual', 'rideable_type']).size().reset_index(name='total_trips')
bike_types_used = bike_types_used.sort_values(by=['member_casual', 'total_trips'], ascending=[True, False])
print("\nBike Types Used by Riders:\n", bike_types_used)

# ================================
# 2. Number of trips per month
# ================================
trips_per_month = df_cleaned.groupby(['month', 'member_casual']).agg(total_trips=('ride_id', 'count')).reset_index()
trips_per_month = trips_per_month.sort_values(by=['member_casual', 'month'])
print("\nNumber of Trips Per Month:\n", trips_per_month)

# ================================
# 3. Number of trips per day of the week
# ================================
trips_per_day_of_week = df_cleaned.groupby(['day_of_week', 'member_casual']).agg(total_trips=('ride_id', 'count')).reset_index()
trips_per_day_of_week = trips_per_day_of_week.sort_values(by=['member_casual', 'day_of_week'])
print("\nNumber of Trips Per Day of the Week:\n", trips_per_day_of_week)

# ================================
# 4. Number of trips per hour
# ================================
df_cleaned['hour_of_day'] = pd.to_datetime(df_cleaned['started_at']).dt.hour
trips_per_hour = df_cleaned.groupby(['hour_of_day', 'member_casual']).agg(total_trips=('ride_id', 'count')).reset_index()
trips_per_hour = trips_per_hour.sort_values(by=['member_casual', 'hour_of_day'])
print("\nNumber of Trips Per Hour:\n", trips_per_hour)

# ================================
# 5. Average ride length per month
# ================================
avg_ride_length_per_month = df_cleaned.groupby(['month', 'member_casual']).agg(avg_ride_duration=('ride_length', 'mean')).reset_index()
print("\nAverage Ride Length Per Month:\n", avg_ride_length_per_month)

# ================================
# 6. Average ride length per day of the week
# ================================
avg_ride_length_per_day_of_week = df_cleaned.groupby(['day_of_week', 'member_casual']).agg(avg_ride_duration=('ride_length', 'mean')).reset_index()
print("\nAverage Ride Length Per Day of the Week:\n", avg_ride_length_per_day_of_week)

# ================================
# 7. Average ride length per hour
# ================================
avg_ride_length_per_hour = df_cleaned.groupby(['hour_of_day', 'member_casual']).agg(avg_ride_duration=('ride_length', 'mean')).reset_index()
print("\nAverage Ride Length Per Hour:\n", avg_ride_length_per_hour)

# ================================
# 8. Starting station locations
# ================================
start_station_locations = df_cleaned.groupby(['start_station_name', 'member_casual']).agg(
    avg_start_lat=('start_lat', 'mean'),
    avg_start_lng=('start_lng', 'mean'),
    total_trips=('ride_id', 'count')
).reset_index()
print("\nStarting Station Locations:\n", start_station_locations)

# ================================
# 9. Ending station locations
# ================================
end_station_locations = df_cleaned.groupby(['end_station_name', 'member_casual']).agg(
    avg_end_lat=('end_lat', 'mean'),
    avg_end_lng=('end_lng', 'mean'),
    total_trips=('ride_id', 'count')
).reset_index()
print("\nEnding Station Locations:\n", end_station_locations)

# ================================
# Save the results to CSV files
# ================================
bike_types_used.to_csv('/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/bike_types_used.csv', index=False)
trips_per_month.to_csv('/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/trips_per_month.csv', index=False)
trips_per_day_of_week.to_csv('/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/trips_per_day_of_week.csv', index=False)
trips_per_hour.to_csv('/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/trips_per_hour.csv', index=False)
avg_ride_length_per_month.to_csv('/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/avg_ride_length_per_month.csv', index=False)
avg_ride_length_per_day_of_week.to_csv('/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/avg_ride_length_per_day_of_week.csv', index=False)
avg_ride_length_per_hour.to_csv('/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/avg_ride_length_per_hour.csv', index=False)
start_station_locations.to_csv('/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/start_station_locations.csv', index=False)
end_station_locations.to_csv('/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/end_station_locations.csv', index=False)

print("\nAnalysis completed and results saved to individual .csv files for further manipulation and investigation.")

# ================================
# Save all the data to a single Excel file with multiple sheets
# ================================
excel_output_path = '/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/Results/cyclistic_analysis.xlsx'

with pd.ExcelWriter(excel_output_path, engine='xlsxwriter') as writer:
    bike_types_used.to_excel(writer, sheet_name='Bike Types Used', index=False)
    trips_per_month.to_excel(writer, sheet_name='Trips Per Month', index=False)
    trips_per_day_of_week.to_excel(writer, sheet_name='Trips Per Day of Week', index=False)
    trips_per_hour.to_excel(writer, sheet_name='Trips Per Hour', index=False)
    avg_ride_length_per_month.to_excel(writer, sheet_name='Avg Ride Length Per Month', index=False)
    avg_ride_length_per_day_of_week.to_excel(writer, sheet_name='Avg Ride Length Per Day', index=False)
    avg_ride_length_per_hour.to_excel(writer, sheet_name='Avg Ride Length Per Hour', index=False)
    start_station_locations.to_excel(writer, sheet_name='Start Station Locations', index=False)
    end_station_locations.to_excel(writer, sheet_name='End Station Locations', index=False)

print(f"\nAnalysis results compiled into a single Excel file with multiple sheets: {excel_output_path}")
