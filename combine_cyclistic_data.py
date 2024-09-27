import pandas as pd
import os

# Define the folder containing the CSV files
folder_path = "/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/SourceData"

# List of all 12 CSV filenames to process from September 2023 to August 2024
csv_files = [
    "202309-divvy-tripdata.csv", "202310-divvy-tripdata.csv", "202311-divvy-tripdata.csv",
    "202312-divvy-tripdata.csv", "202401-divvy-tripdata.csv", "202402-divvy-tripdata.csv",
    "202403-divvy-tripdata.csv", "202404-divvy-tripdata.csv", "202405-divvy-tripdata.csv",
    "202406-divvy-tripdata.csv", "202407-divvy-tripdata.csv", "202408-divvy-tripdata.csv"
]

# Read and combine all CSV files into a single DataFrame
combined_df = pd.concat([pd.read_csv(os.path.join(folder_path, file)) for file in csv_files], ignore_index=True)

# Export the combined data to a single CSV file
combined_csv_path = "/Users/kadrihearns/Documents/GitHub/GDA-CyclisticCaseStudy/CaseStudyPython/combined_cyclistic_data.csv"
combined_df.to_csv(combined_csv_path, index=False)
print(f"Combined data exported to {combined_csv_path}")
