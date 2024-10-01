# Google Data Analytics Capstone: Cyclistic Case Study

## Introduction
**Course:** https://www.coursera.org/learn/google-data-analytics-capstone

In this case study, I will perform many real-world tasks of a junior data analyst at a fictional company, Cyclistic. In order to answer the key business task of understanding how casual riders and annual members use Cyclistic bikes differently with the goal of designing a new marketing strategy to convert the casual riders to annual members. I will follow the steps of the data analysis process: Ask, Prepare, Process, Analyze, Share, and Act.

### Links
**Data Source:** https://divvy-tripdata.s3.amazonaws.com/index.html

**Data Integrity:** The data is publicly available and provided by Motivate International Inc. under a license agreement, ensuring that it is appropriate and reliable for this analysis, although personally identifiable information is not included to protect rider privacy. At the time of work, I am starting from August 2024. [License Agreement](https://divvybikes.com/data-license-agreement)


### Technical Tools
- Python
- Excel

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
2. Loading Data into DataFrame Tables: With the use of Python, I combined all of the individual csv files into one, and cleaned (removed duplicates, fixed datetime formats, and removed null values where possible) and summarized the data. Within my scripts, I have commented out lines to give a full description of each step, which will print out into the terminal. (Note: To use my scripts, please create two sub folder "Results", "SourceData" for both the output and input files.)
3. Analyzing the Data: Performing the actual analysis and writing to an excel file to summarize the data. See the python files in the repository for clear steps. (I focused on 9 umbrellas; Bike types used by riders, number of trips per month, number of trips per day of the week, number of trips per hour, avg ride length per month, avg ride length per day of week, avg ride length per hour, and finally the starting and end locations.)
4. Visualizations creation

## Analyze & Share
### Visuals
![Pie Charts for reference](https://github.com/Kahearns/GDA-CyclisticCaseStudy/blob/3872ee7e2b376fcd8943163e09e29bf43fcc9528/PieChartSC.png)
![By month](https://github.com/Kahearns/GDA-CyclisticCaseStudy/blob/main/ByMonthSC.png)
![By Week](https://github.com/Kahearns/GDA-CyclisticCaseStudy/blob/main/ByWeek.png)
![By hour](https://github.com/Kahearns/GDA-CyclisticCaseStudy/blob/main/ByHour.png)

### Insights

**1. Usage Patterns**

***Total Trips:***

Casual Riders: 1,466,246 trips<br/>
Annual Members: 2,675,639 trips
***Total Trips Per Month:*** Same as total trips overall.
Casual riders: 1,466,246 trips
Members: 2,675,639 trips
***Total Trips Per Day:*** Same as total trips overall.
Casual riders: 1,466,246 trips
Members: 2,675,639 trips
***Total Trips Per Hour:*** Same as total trips overall.
Casual riders: 1,466,246 trips
Members: 2,675,639 trips

**2. Average Ride Lengths**
***Average Ride Length Per Month:***
Casual Riders: 22.36 minutes
Annual Members: 12.38 minutes
***Average Ride Length Per Day:***
Casual Riders: 23.77 minutes
Annual Members: 12.72 minutes
***Average Ride Length Per Hour:***
Casual Riders: 22.85 minutes
Annual Members: 12.44 minutes

**Usage Frequency**: Annual members use the bikes significantly more than casual riders, with over 2.6 million trips compared to about 1.5 million for casual users. This suggests that annual members are more engaged with the service.

**Ride Duration:** Casual riders tend to have longer average ride durations compared to annual members, which may indicate that casual riders are using the bikes for longer leisure rides, while members might be using them for shorter, more practical trips.

### Story Summary
**Engagement Level:** Annual members demonstrate higher engagement with the Cyclistic bike-share program, as evidenced by their significantly higher number of trips (2,675,639) compared to casual riders (1,466,246).

**Usage Context:** Casual riders tend to take longer rides on average (22.36 minutes) compared to annual members (12.38 minutes). This suggests that casual riders may be using the bikes for leisure purposes, while annual members might use them more for commuting or shorter trips.

**Potential Marketing Opportunities:** The longer average ride lengths of casual riders present an opportunity for targeted marketing strategies that highlight the benefits of converting to annual memberships, emphasizing convenience, cost-effectiveness, and ease of use.

## Act
### Conclusions and Recommendations
**Targeted Marketing Campaigns:** Design marketing initiatives aimed at casual riders, focusing on the value of an annual membership. Highlight features such as unlimited rides, cost savings compared to single rides, and the convenience of having a bike readily available. Use testimonials and data-driven insights to showcase the benefits of becoming a member.

**Engagement Strategies:** Develop engagement strategies that encourage casual riders to try the bike-share program more frequently. This could include promotional offers for first-time annual memberships or discounted rates for casual riders who commit to longer-term usage.

**Leverage Ride Duration Insights:** Since casual riders take longer rides, consider creating targeted content around leisure biking experiences. This could include curated bike routes, local attractions, or events that encourage casual riders to explore the city using Cyclistic bikes, ultimately making them more inclined to convert to annual memberships.

These recommendations are designed to not only convert casual riders into annual members but also enhance overall engagement with the Cyclistic bike-share program, driving long-term profitability and growth.

