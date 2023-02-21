# Data Science Salary Estimator: Project Overview (Ken Jee Youtube 

* Created a tool to estimate data science salaries (estimated error around $11K) -  specifically useful for me in my career journey to see what skills are most sought after for a data science job 
* Scraped 1000+ jobs from Glassdoor using Python and Selenium 
* Engineered features to quantify skills like Python, Spark, AWS, etc. 
* Tried Linear, Lasso, and Random Forest Regression to find the best model. 

## Code and Resources  

* Main Packages: Numpy, Pandas, Seaborn, Selenium, Sklearn
* Web Scraper (Omer Sakarya): https://mersakarya.medium.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905 
* Ken Jee's Project Tutorial - https://youtu.be/MpF9HENQjDo

## Web Scraping and Data Cleaning

* Pulled the following variables from each job using the Scraper code mentioned above:
  *  Job Title
  *  Salary Estimate
  *  Job Description
  *  Rating
  *  Company Name, Location, Headquarters, Size, Founding Date, 
  *  Type of Ownernship 
  *  Industry, Sector 
  *  Revenue 
  *  Competitors

* Parsed characters ($, K) out of salary, removed nulls, fixed formatting errors  
* Separated company city from state and added a column to denote if the job's location and the company's headquarters was in the same city
* Made columns to check which skills were required for each job (Python, R, Excel, AWS, and Spark)

## EDA

* Explored the following questions: 
  * Which states have the most data science jobs?
  * Which states pay the highest salary?
  * Breakdown of job types by count, salary, location, and position 
  * Breakdown of job sectors by salary 

* Found that:
  * Learning Python is a necessary skill 
  * Companies with a higher revenue and a higher rating pay more 
  * DS jobs in the media sector pay the highest, closely followed by Legal, IT, and Biotech
  * Jobs in CA pay the most 
  * On average, machine learning engineers and data scientists are paid more than data analysts, data   engineers, managers
  
  <img width="332" alt="Screen Shot 2023-02-21 at 11 25 12 AM" src="https://user-images.githubusercontent.com/108362965/220441319-2e9b840e-364d-4262-a3d6-c6adeed8d5e3.png">



