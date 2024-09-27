# Google Data Analytics Capstone: Cyclistic Case Study

## Introduction
Course: https://www.coursera.org/learn/google-data-analytics-capstone

In this case study, I will perform many real-world tasks of a junior data analyst at a fictional company, Cyclistic. In order to answer the key business task of understanding how casual riders and annual members use Cyclistic bikes differently with the goal of designing a new marketing strategy to convert the casual riders to annual members. I will follow the steps of the data analysis process: Ask, Prepare, Process, Analyze, Share, and Act.

### Links
**Data Source:** https://divvy-tripdata.s3.amazonaws.com/index.html

**Data Integrity:** The data is publicly available and provided by Motivate International Inc. under a license agreement, ensuring that it is appropriate and reliable for this analysis, although personally identifiable information is not included to protect rider privacy. At the time of work, I am starting from August 2024. [License Agreement](https://divvybikes.com/data-license-agreement)


### Technical Tools
Python
Tableau
Excel

### Stakeholders
**Lily Moreno (Director of Marketing)**
- Goal: Increase the number of annual memberships to drive long-term profitability.
- Hypothesis: Casual riders can be converted into annual members through targeted marketing strategies that highlight the benefits and value of an annual membership.

**Cyclistic Marketing Analytics Team (Including Me)**
- Goal: Analyze usage patterns of casual riders and annual members to identify trends that can inform marketing strategies.
- Hypothesis: Casual riders and annual members use Cyclistic bikes differently, and these differences can be leveraged to create campaigns that encourage casual riders to transition to annual memberships.

**Cyclistic Executive Team**
- Goal: Ensure that marketing efforts lead to sustainable growth and increased profitability by expanding the annual membership base.
- Hypothesis: By converting casual riders into annual members, Cyclistic can achieve a more stable and predictable revenue stream, ensuring future success and expansion opportunities.

## Ask
The main ask of the case study is to analyze how annual members and casual riders use Cyclistic bikes differently. The insights gained from this analysis will be used to develop targeted marketing strategies aimed at converting casual riders into annual members, thereby increasing profitability and achieving Cyclistic's long-term growth objectives.

## Prepare
There are 12 files with naming convention of YYYYMM-divvy-tripdata and each file includes information for one month. The columns and data points that are provided within each file are ride_id, rideable_type, started_at, ended_at, start_station_name, start_station_id, end_station_name, end_station_id, start_lat, start_lng, end_lat, end_lng and member_casual.

## Process
**Steps Taken**
1. Extracting Data: Each zip file containing the bike-share data from September 2023 to August 2024 was intended to be extracted.
2. Loading Data into SQL Tables: Each month’s CSV file would be loaded into a separate SQL table named based on the year and month (e.g., 202309 for September 2023).
3. Combining Data: A new table named combined_cyclistic_data would be created by combining all individual monthly tables using the UNION ALL SQL command.
