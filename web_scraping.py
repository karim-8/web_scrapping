import csv
from itertools import zip_longest
import requests
from bs4 import BeautifulSoup

#Lists of job data 
job_titles_list = []
company_names_list = []
company_location_names_list = []
jobs_skills_list = []

#Fetching list of jobs from the website
try:
    result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=navbg")
    result.raise_for_status()  # Check if the request was successful
    
except requests.RequestException as e:
    print(f"Error fetching the page: {e}")
    exit()
    
#Save the page src
src = result.content

#Create parser object 
soup = BeautifulSoup(src,"lxml")

#Getting the job name from the html 
job_titles = soup.find_all("h2", {"class":"css-m604qf"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
company_location_names = soup.find_all("span",{"class":"css-5wys0k"})
jobs_skills = soup.find_all("div",{"class":"css-y4udm8"})

# print(len(job_titles))
# print(len(company_names))
# print(len(company_location_names))
# print(len(jobs_skills))

print("-- --- --- --- --- ---- ---- ----")
# # Apppend pure date to the current lists
for i in range(len(job_titles)):
    job_titles_list.append(job_titles[i].text)
    company_names_list.append(company_names[i].text)
    company_location_names_list.append(company_location_names[i].text)
    jobs_skills_list.append(jobs_skills[i].text)
    
print(job_titles_list)
print("-"*50)
print(company_names_list)
print("-"*50)
print(company_location_names_list)
print("-"*50)
print(jobs_skills_list)
print("-"*50)

file_list = [job_titles_list,company_names_list,company_location_names_list,jobs_skills_list]
# Zipping each value to be taken in one row only and added it in exported varaible
exported_data = zip_longest(*file_list)
# Open data in csv file "which can be openend in Word format"
with open("/Users/karim/Documents/Wuzzuf_scrap_data.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job title", "Company Names", "Company Locations", "Job Skills"])
    wr.writerows(exported_data)
    



    
    
    