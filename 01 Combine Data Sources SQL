-- Establish a connection to a SQLite database for the Cyclistic case study
conn = sqlite3.connect('/mnt/data/cyclistic_case_study.db')
cursor = conn.cursor()

-- List of the 12 uploaded CSV filenames
csv_files = [
    "202309-divvy-tripdata.csv", "202310-divvy-tripdata.csv", "202311-divvy-tripdata.csv",
    "202312-divvy-tripdata.csv", "202401-divvy-tripdata.csv", "202402-divvy-tripdata.csv", 
    "202403-divvy-tripdata.csv", "202404-divvy-tripdata.csv", "202405-divvy-tripdata.csv", 
    "202406-divvy-tripdata.csv", "202407-divvy-tripdata.csv", "202408-divvy-tripdata.csv"
]

# Path where the uploaded CSV files are stored
uploaded_files_path = '/mnt/data/'

# Process each CSV file sequentially
for csv_file in csv_files:
    csv_path = os.path.join(uploaded_files_path, csv_file)
    
    try:
        # Load data into a dataframe
        df = pd.read_csv(csv_path)
        
        # Use the year and month from the file name as the table name for clarity
        table_name = csv_file.replace('-divvy-tripdata.csv', '')
        
        # Upload the data to the SQL table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
    except Exception as e:
        print(f"Failed to process {csv_file}: {str(e)}")

-- Now, create a combined table by selecting all data from individual monthly tables
combined_table_query = """
CREATE TABLE IF NOT EXISTS combined_cyclistic_data AS (
  SELECT * FROM 202309
  UNION ALL
  SELECT * FROM 202310
  UNION ALL
  SELECT * FROM 202311
  UNION ALL
  SELECT * FROM 202312
  UNION ALL
  SELECT * FROM 202401
  UNION ALL
  SELECT * FROM 202402
  UNION ALL
  SELECT * FROM 202403
  UNION ALL
  SELECT * FROM 202404
  UNION ALL
  SELECT * FROM 202405
  UNION ALL
  SELECT * FROM 202406
  UNION ALL
  SELECT * FROM 202407
  UNION ALL
  SELECT * FROM 202408);"""

-- Execute the query to create the combined table
try:
    cursor.execute(combined_table_query)
except Exception as e:
    print(f"Failed to create the combined table: {str(e)}")

-- Export the combined data to a CSV file
try:
    combined_df = pd.read_sql_query("SELECT * FROM combined_cyclistic_data;", conn)
    combined_csv_path = '/mnt/data/combined_cyclistic_data.csv'
    combined_df.to_csv(combined_csv_path, index=False)
except Exception as e:
    print(f"Failed to export the combined data to CSV: {str(e)}")

-- Commit changes and close the database connection
conn.commit()
conn.close()

-- Provide the link to download the combined CSV file
combined_csv_path
