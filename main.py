import requests
from time import sleep

API_Key = "AIzaSyCPO5ZKErxFr4aFYQK5L7WkaTnq5G4A-WY"
baseURL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="


def get_pagespeed(page_url: str, strategy: str):
    """
    :param page_url: full url of page
    :param strategy: "desktop": Fetch and analyze the URL for desktop browsers
    "mobile": Fetch and analyze the URL for mobile devices
    :return:
    """
    response_url = baseURL + page_url + '&key=' + API_Key + '&strategy=' + strategy
    response = requests.get(response_url)
    json_data = response.json()

    lighthouse_result = json_data["lighthouseResult"]
    categories = lighthouse_result["categories"]
    performance = categories["performance"]
    score = performance["score"]
    return score, json_data

    sleep(1)


print(get_pagespeed('https://www.apple.com/', 'mobile'))
