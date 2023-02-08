import glassdoor_scraper as gs 
import pandas as pd 
path = "/Users/tanvivaidya/Downloads/chromedriver_mac64/chromedriver"
df = gs.get_jobs('data scientist', 15, False, path, 15)

