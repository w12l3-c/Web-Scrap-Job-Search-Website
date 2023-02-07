import requests, time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

"""
DEMO
---
with open("", 'r') as f:
    content = f.read()

    # prettify html with tags
    s = soup(content, "lxml")
    #print(s.prettify())

    # grabbing information by tags
    html_tags = s.find("h5")             # only the first one
    html_tags_lst = s.find_all("h5")     # returns a list of all items
    #print(html_tags)
    for things in html_tags_lst:
        print(things.text)

    cards = soup.find_all('div', class_='card')     # class has to have class_
    for things in cards:
        name = things.h5.text                    # grabbing the h5 attribute only
        price = things.a.text.split()[-1]        # grabbing the last element a attribute price

        print(f"{name} cost {price}")
"""

# real life website
# practice web scrap website: indeed.com
unfamiliar_skill = input('Put some skills you are not familiar with \n>')
#unfamiliar_skill.split(",")
print(f"filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get('https://ca.indeed.com/jobs?q=python&l=Ontario&ts=1643925611616&rq=1&rsIdx=1&fromage=last&newcount=6&vjk=e115467ceec73ae4').text
    s = soup(html_text, 'lxml')
    jobs = s.find_all("div", {"class":'slider_item'})
    links = s.find_all("a", {"data-hiring-event":'false'})

    # link normally
    """
    for link in links:
        print(link["href"])
    for link in links:
        more_info = link.header.div.a['href']
        print(f"More info: {more_info}")
    """

    for index, job in enumerate (jobs):        # running through all the items in the jobs
        try:
            publish = job.find('span', class_='date').text
            print(publish)
            time.sleep(0.01)
            if "Active" in publish or "+" not in publish:     # condition and filter some items only
                comp_name = job.find('span', class_='companyName').text.replace(' ','')     # the replace is for replacing empty space with nothing
                position_name = job.find('h2', class_='jobTitle jobTitle-color-purple').text
                job_recommend = job.find('div', class_='job-snippet').li.text
                salary = job.find('div', class_='salary-snippet').span.text
                more_info = links[index]["href"]
                if unfamiliar_skill not in job_recommend:
                    # writing things in files is better than printing in terminal
                    with open(f'tutorial_web_text/{index}.txt', 'w') as f:
                        f.write(f"Company name: {comp_name}\n")
                        f.write(f"Position: {position_name}\n")
                        f.write(f"Skills recommended: {job_recommend}\n")
                        f.write(f"Salary: {salary}\n")
                        f.write(f"More info: {more_info}\n")
                    print(f"File saved: {index}")
                    # print(f"Company name: {comp_name}")
                    # print(f"Position: {position_name}")
                    # print(f"Skills recommended: {job_recommend}")
                    # print(f"Salary: {salary}")
                    # print(f"More info: {more_info}")
        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes until next run...")
        break
        time.sleep(time_wait * 60)










