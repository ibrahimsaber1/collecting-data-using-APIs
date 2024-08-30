import requests
# connecting to the data
base_Url = "https://api.covidtracking.com/v2/states/wa/2021-01-02.json"


res = requests.get(base_Url)
res

covid_data_us = res.json()
type(covid_data_us)
# viewing the data
covid_data_us
#getting the state
name_of_state = covid_data_us["data"]["state"]
name_of_state
#getting the date
date = covid_data_us["data"]["date"]
date
#getting the total cases
total_cases = covid_data_us["data"]["cases"]["total"]["value"]
total_cases
#getting the confirmed cases
confirmed_cases = covid_data_us["data"]["cases"]["confirmed"]["value"]
confirmed_cases
#getting the first row
res = requests.get(f"https://api.covidtracking.com/v2/states/wa/2021-01-20.json")
covid_data_us = res.json()

with open("washington_covid.csv" ,mode ="w",    encoding= "utf-8" ) as fd:
    fd.write("name_of_state,date,total_cases,confirmed_cases\n")
    name_of_state = covid_data_us["data"]["state"]
    date = covid_data_us["data"]["date"]
    total_cases = covid_data_us["data"]["cases"]["total"]["value"]
    confirmed_cases = covid_data_us["data"]["cases"]["confirmed"]["value"]
    fd.write(f"{name_of_state},{date},{total_cases},{confirmed_cases}\n")
    
#view the top row
import pandas as pd

df = pd.read_csv("washington_covid.csv")
df

# get the data for the next 10 days:
day_1 = "2021-01-"
days = list(range(11,22))
with open("washington_covid.csv" ,mode ="w",    encoding= "utf-8" ) as fd:
    fd.write("name_of_state,date,total_cases,confirmed_cases\n")

    for day in days:
        res = requests.get(f"https://api.covidtracking.com/v2/states/wa/{day_1}{day}.json")
        covid_data_us = res.json()
        
        name_of_state = covid_data_us["data"]["state"]
        date = covid_data_us["data"]["date"]
        total_cases = covid_data_us["data"]["cases"]["total"]["value"]
        confirmed_cases = covid_data_us["data"]["cases"]["confirmed"]["value"]
        fd.write(f"{name_of_state},{date},{total_cases},{confirmed_cases}\n")

#view the data for the next 10 days:
import pandas as pd

df = pd.read_csv("washington_covid2.csv")
df


