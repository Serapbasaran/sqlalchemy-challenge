Climate Analysis - Honolulu Hawaii

Background

You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you need to have some climate analysis on the area. This analysis will give you climate information and data exploration for Honolulu by using provided database dating between 2010 -2017. 

This study includes a jupyter notebook providing  climate data and other data explorations and a Flask API on the queires developed for climate database.

Climate Analysis and Data Exploration

* Precipitation Analysis: A query to retrieve the last 12 months of precipitation data in dataset, a plot to visualize the results and 
  the summary statistics for the precipitation data
  
* Station Analysis
  - The total numbers of stattions
  - The most active stations
  - The last 12 months of temperature observation data (TOBS) for the most active station in dataset and a histogram for the results
  
* Temperature Analysis I
  - The average temperature in June and December at all stations accross all available years in the dataset

* Temperature Analysis II
  -The minimum, average, maximum temperatures for the given range of the dates 
  - A bar chart to display results of the previous query
  
 * Daily Rainfall Average
  - The rainfall per weather station using the previous year's matching dates
  - Query for the calculate the daily normals. Normals are the averages for the min, avg, and max temperatures
  - An area plot to visualize daily normals
  
 Climate App (Flaask API)
 - List of all routes
 - JSON presentation of precipitation data for each date in dataset
 - JSON list of stations from the dataset
 - JSON list of temperature observations (TOBS) for the previous year 
 - JSON list of the minimum, average, and max temperatures for a given start and end day. 
 

