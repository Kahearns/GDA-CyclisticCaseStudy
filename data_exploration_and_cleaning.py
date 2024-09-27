import pandas as pd

# Load the combined CSV file
file_path = "/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/combined_cyclistic_data.csv"
df = pd.read_csv(file_path)

# ========================
# Part 1: Data Exploration
# ========================

# 1. Checking data types of all columns
print("Data Types of All Columns:\n", df.dtypes)

# 2. Checking for number of null values in all columns
null_counts = df.isnull().sum()
print("\nNumber of Null Values in Each Column:\n", null_counts)

# 3. Checking for duplicate rows based on the ride_id column
duplicate_rows = df.duplicated(subset='ride_id').sum()
print("\nNumber of Duplicate Rows Based on ride_id:", duplicate_rows)

# 4. Checking if all ride_id values have a length of 16
df['ride_id_length'] = df['ride_id'].astype(str).apply(len)
ride_id_length_counts = df['ride_id_length'].value_counts()
print("\nRide ID Length Counts:\n", ride_id_length_counts)

# 5. Checking unique types of rideable_type and their counts
rideable_type_counts = df['rideable_type'].value_counts()
print("\nUnique Types of rideable_type and Counts:\n", rideable_type_counts)

# 6. Displaying a sample of started_at and ended_at columns
print("\nSample of started_at and ended_at columns:\n", df[['started_at', 'ended_at']].head(10))

# ========================
# Part 2: Data Cleaning
# ========================

print("\nHandling inconsistent datetime formats...")

# Step 1: Initial attempt to clean datetime values
# Removing trailing fractional seconds or unwanted characters from 'started_at' and 'ended_at'
df['started_at'] = df['started_at'].str.replace(r'\.\d+$', '', regex=True).str.strip()
df['ended_at'] = df['ended_at'].str.replace(r'\.\d+$', '', regex=True).str.strip()

# Step 2: Convert to datetime and identify rows that failed conversion
df['started_at'] = pd.to_datetime(df['started_at'], errors='coerce')
df['ended_at'] = pd.to_datetime(df['ended_at'], errors='coerce')

# Identifying rows where conversion failed
invalid_started_at = df['started_at'].isna()
invalid_ended_at = df['ended_at'].isna()
print(f"\nRows with invalid 'started_at': {invalid_started_at.sum()}")
print(f"Rows with invalid 'ended_at': {invalid_ended_at.sum()}")

# Step 3: Attempt to correct rows with invalid datetime values
if invalid_started_at.any():
    # If there are still invalid 'started_at' values, check for common issues and attempt to fix them
    df.loc[invalid_started_at, 'started_at'] = pd.to_datetime(
        df.loc[invalid_started_at, 'started_at'], errors='coerce', format='%Y-%m-%d %H:%M:%S'
    )
    
if invalid_ended_at.any():
    df.loc[invalid_ended_at, 'ended_at'] = pd.to_datetime(
        df.loc[invalid_ended_at, 'ended_at'], errors='coerce', format='%Y-%m-%d %H:%M:%S'
    )

# Re-check if there are any remaining invalid rows
remaining_invalid_start = df['started_at'].isna()
remaining_invalid_end = df['ended_at'].isna()

print(f"\nAfter correction attempts, remaining invalid 'started_at': {remaining_invalid_start.sum()}")
print(f"After correction attempts, remaining invalid 'ended_at': {remaining_invalid_end.sum()}")

# Drop rows only if we cannot correct the conversion
df = df[~(remaining_invalid_start | remaining_invalid_end)]

# Calculating ride length in minutes
df['ride_length'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

# Filter rows where ride_length is between 1 and 1440 minutes
df_cleaned = df[(df['ride_length'] > 1) & (df['ride_length'] < 1440)]

# Removing rows with missing start_station_name, end_station_name, end_lat, or end_lng
df_cleaned = df_cleaned.dropna(subset=['start_station_name', 'end_station_name', 'end_lat', 'end_lng'])

# Extracting day of the week and month
df_cleaned['day_of_week'] = df_cleaned['started_at'].dt.dayofweek.map({
    0: 'MON', 1: 'TUES', 2: 'WED', 3: 'THURS', 4: 'FRI', 5: 'SAT', 6: 'SUN'
})

df_cleaned['month'] = df_cleaned['started_at'].dt.month.map({
    1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 
    7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'
})

# Selecting the required columns for the cleaned dataset
df_cleaned = df_cleaned[['ride_id', 'rideable_type', 'started_at', 'ended_at', 'ride_length', 
                         'day_of_week', 'month', 'start_station_name', 'end_station_name', 
                         'start_lat', 'start_lng', 'end_lat', 'end_lng', 'member_casual']]

# Save the cleaned data to a new CSV file
cleaned_csv_path = "/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/cleaned_cyclistic_data.csv"
df_cleaned.to_csv(cleaned_csv_path, index=False)
print(f"\nCleaned data exported to {cleaned_csv_path}")

# Display the total number of rows in the cleaned dataset
print(f"\nTotal Rows in Cleaned Data: {df_cleaned.shape[0]}")
