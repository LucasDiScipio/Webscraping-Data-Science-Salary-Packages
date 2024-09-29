# Webscraping Data Science Salary Packages
## Project description:
This project aims to showcase a good level of proficiency in the python programming language and a number of its fundamental libraries for data science. This project is structured through the following python scripts :
* `src\scraper.py` : 
This Python script automates the process of scraping posts from the "BESalary" subreddit using the Reddit API (PRAW). It searches for posts related to specific data job roles (data analyst, data scientist, data engineer) and saves the text content of salary-related posts into a local directory.
* `src\regex_extractor.py` :
This Python script processes and extracts salary-related information from text files that contain job posts scraped from the "BESalary" subreddit. For each post, it extracts various details like *gross salary*, *net salary*, *years of experience*, *working hours*, *teleworking days*, *holidays*, *ecocheques*, *education level*, and the *number of employees*. The script relies on regular expressions to parse specific pieces of information from the posts and serializes the extracted data for easy retrieval.
* `src\db.py` :
This Python script transfers the extracted job post information into a SQLite database.

The exploratory data analysis (data cleaning & analysis) is then done in the python notebook `src\eda.ipynb`. 
