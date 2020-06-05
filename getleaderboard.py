import requests
import json

def get_agent_performance(start_date,end_date, api_key):
    
    head = {"Authorization":"Token " + api_key}
    param = {"start_date":start_date,"end_date":end_date}

    response = requests.get("https://api.callhub.io/v1/analytics/agent-leaderboard", headers=h, params=p)

    agents = response.json().get("plot_data")
    
    print(agents)
    return agents


api_key='YOUR API KEY HERE'
get_agent_performance("2019-12-01","2020-12-30", api_key)
