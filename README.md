# Honolulu Climate Analysis for Your Dream Vacation

Welcome to the Honolulu Climate Analysis for Your Dream Vacation project! In this project, I will conduct a climate analysis and data exploration of Honolulu, Hawaii. The project involves using Python, SQLAlchemy, Pandas, and Matplotlib to explore and visualize the climate dataset, as well as designing a Flask API to provide access to the analyzed data. This analysis will help plan a long holiday vacation in this beautiful location. Below are the instructions and steps followed.

## Part 1: Analyze and Explore the Climate Data
In the first part of the project, I connected to the SQLite database (hawaii.sqlite) and performed various analyses on the climate data.

### Setup and Data Retrieval
I began by setting up the necessary environment and establishing a connection to the database using SQLAlchemy. I reflected the tables into classes, namely 'Station' and 'Measurement', and created a session to interact with the database.

### Precipitation Analysis
1. Found the most recent date in the dataset, which was August 23, 2017.
2. To retrieve the last 12 months of precipitation data, I calculated the date one year from the most recent date and performed a query to retrieve the data.
3. Loaded the query results into a Pandas DataFrame, sorted it by date, and plotted the precipitation data using Matplotlib.
4. Finally, calculated summary statistics for the precipitation data.
   
![image](https://github.com/agorvie/sqlalchemy-challenge/assets/122469792/4f32f9b4-89b0-4c2a-999b-d9edba0023d4)


### Station Analysis
1. Designed a query to calculate the total number of stations in the dataset, which was found to be 9.
2. To find the most active stations, I listed the stations and their observation counts in descending order. The station with the greatest number of observations was USC00519281.
3. Using the most active station ID, I calculated the lowest, highest, and average temperatures.
4. Also queried and plotted the temperature observations for the last 12 months for the most active station as a histogram.
   
![image](https://github.com/agorvie/sqlalchemy-challenge/assets/122469792/83d52e68-d827-4622-af83-dafa730cc33c)

## Part 2: Design Climate App
In the second part of the project, I designed a Flask API based on the analyses conducted. The following routes can be used to retrieve various climate-related information:

### Available Routes
 - */*: The homepage, which lists all available routes.
 - */api/v1.0/precipitation*: Retrieve precipitation data for the last 12 months.
 - */api/v1.0/stations*: Get a list of weather stations in the dataset.
 - */api/v1.0/tobs*: Retrieve temperature observations for the last 12 months for the most active weather station.
 - */api/v1.0/start_date*: Calculate minimum, average, and maximum temperatures for a specified start date.
 - */api/v1.0/start_date/end_date*: Calculate minimum, average, and maximum temperatures for a specified date range.

### Route Details
 - */api/v1.0/precipitation*
    * Description: Retrieve precipitation data for the last 12 months.
    * HTTP Method: GET
    * Example Usage: */api/v1.0/precipitation*

 - */api/v1.0/stations*
    * Description: Get a list of weather stations in the dataset.
    * HTTP Method: GET
    * Example Usage: */api/v1.0/stations*

 - */api/v1.0/tobs*
    * Description: Retrieve temperature observations for the last 12 months for the most active weather station.
    * HTTP Method: GET
    * Example Usage: */api/v1.0/tobs*

 - */api/v1.0/start_date*
    * Description: Calculate minimum, average, and maximum temperatures for a specified start date.
    * HTTP Method: GET
    * Example Usage: */api/v1.0/start_date*, where *start_date* is in the format *YYYY-MM-DD*.

 - */api/v1.0/start_date/end_date*
    * Description: Calculate minimum, average, and maximum temperatures for a specified date range.
    * HTTP Method: GET
    * Example Usage: */api/v1.0/start_date/end_date*, where *start_date* and *end_date* are in the format 'YYYY-MM-DD'.

### Usage Notes
- For routes that calculate temperatures ('/api/v1.0/start_date' and '/api/v1.0/start_date/end_date'), provide the date(s) in the format 'YYYY-MM-DD'.
- The API returns data in JSON format.
- Don't forget to close the session when you're done using the API.

Enjoy exploring the climate data from Honolulu, Hawaii, and planning your next vacation!

## References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks to an external site.


