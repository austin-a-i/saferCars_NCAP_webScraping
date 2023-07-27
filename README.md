# _NCAP_SafestCars_webScraping
 
Web-Scraping using BeautifulSoup lib in Python for creating a dataframe to retrieve the Safest Cars rating in Latin NCAP website for the year 2020-2023 and before 2020.

1) Importing request library to extract site and parsing in HTML format using Beautiful Soup lib
2) Extracting text(with tags) for each of the columns(brand,vehicle-model,date,adult-safety,child-safety,star rating,safety measures)
   using selection (html)tags
3) Extracting the text from the selection tags before appending each to respective lists.
4) Creating a Dictionary key-value pair for adding multiple values to a unique key
5) Creating a dataframe from the dictionary and exporting the same as a csv file.

NOTE:
Since the data from 2020-Present and before 2020 are represented in different formats(deletion of variables), two csv files are made with different variables.
