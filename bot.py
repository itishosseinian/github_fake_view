import requests

githuburl = "YOUR_URL"
number_of_views = 10

for i in range(number_of_views):
    response = requests.get(githuburl)
    if response.status_code == 200:
        print(f"{i +1} views have been generated so far")
    else:
        print(f"failed at {i +1 } attempts")
        break