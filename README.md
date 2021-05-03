# Climate Analysis - Honolulu Hawaii


Conduct an analysis that will give you climate information and data exploration for Honolulu by using provided database dating between 2010 -2017. 

This study includes a jupyter notebook providing  climate data and other data explorations and a Flask API on the queires developed for climate database.

Climate Analysis and Data Exploration

* Precipitation Analysis: A query to retrieve the last 12 months of precipitation data in dataset, a plot to visualize the results and 
  the summary statistics for the precipitation data

 ![alt text](https://github.com/Serapbasaran/sqlalchemy-challenge/blob/main/Output/Screenshot%202021-05-03%20172727.png)
 
  
* Station Analysis
  - The total numbers of stattions
  - The most active stations
  - The last 12 months of temperature observation data (TOBS) for the most active station in dataset and a histogram for the results
  
   ![alt text](https://github.com/Serapbasaran/sqlalchemy-challenge/blob/main/Output/Screenshot%202021-05-03%20172859.png)

* Temperature Analysis I
  - The average temperature in June and December at all stations accross all available years in the dataset

     ![alt text](https://github.com/Serapbasaran/sqlalchemy-challenge/blob/main/Output/Screenshot%202021-05-03%20172936.png)


* Temperature Analysis II
  -The minimum, average, maximum temperatures for the given range of the dates 
  - A bar chart to display results of the previous query
  
     ![alt text](https://github.com/Serapbasaran/sqlalchemy-challenge/blob/main/Output/Screenshot%202021-05-03%20173009.png)


* Daily Rainfall Average
  - The rainfall per weather station using the previous year's matching dates
  - Query for the calculate the daily normals. Normals are the averages for the min, avg, and max temperatures
  - An area plot to visualize daily normals
  
Climate App (Flask API)
 - List of all routes
 - JSON presentation of precipitation data for each date in dataset
 - JSON list of stations from the dataset
 - JSON list of temperature observations (TOBS) for the previous year 
 - JSON list of the minimum, average, and max temperatures for a given start and end day. 
 

