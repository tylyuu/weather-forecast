import requests

API_KEY = "f27b0481a5de1f3fbe39b5f568a90124"

def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Toronto", days=3))
    print(get_data(place="Tokyo", days=3))



