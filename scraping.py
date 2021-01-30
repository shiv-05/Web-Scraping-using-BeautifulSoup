# It scrap a data from times job website and give a data like company name , skills required and give a link for applying , and it store a data in a text file and it also update or include our data in text file
# It shows a data of only which are posted few days ago

from bs4 import BeautifulSoup
import requests
import time

print('Put any one skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
unfamiliar_skill = unfamiliar_skill.lower()

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
def find_jobs(unfamiliar_skill):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for index , job in enumerate(jobs):
        published_date = job.find('span',class_="sim-posted").span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_ = 'joblist-comp-name').text
            skills = job.find('span',class_="srp-skills").text
            more_info = job.header.h2.a['href']
            
            if unfamiliar_skill not in skills:
                with open (f'{index}.txt','w') as f:
                    f.write(f'Company Name : {company_name.strip()}\n')
                    f.write(f'Required Skills : {skills.strip()}\n')
                    f.write(f'More Info : {more_info}\n')
                
                print(f'File Saved : {index}')

if __name__ == '__main__':
    while True:
        find_jobs(unfamiliar_skill)
        time_wait = 10
        print(f'Waiting {time_wait} minutes....')
        time.sleep(time_wait*60)
