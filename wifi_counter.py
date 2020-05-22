import configparser
import json
from collections import Counter

import requests

requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
)

cfg = configparser.ConfigParser()
cfg.read("mosru_api.ini")
API_KEY = cfg["KEYS"]["API_KEY"]


def send_get_request(dataset_id):
    headers = {"Content-Type": "application/json"}
    response = requests.get(
        f"https://apidata.mos.ru/v1/datasets/{dataset_id}/features?api_key={API_KEY}",
        headers=headers,
        verify=False,
    )
    if response.status_code == 200:
        return response
    else:
        print(response.text)


def data_printer(adress):
    count_wifi = dict(Counter(adress))
    top_five = sorted(set(count_wifi.values()), reverse=True)[:5]

    print("----------------")
    top_count = 0
    for count in top_five:
        result = {k: v for k, v in count_wifi.items() if v == count}
        for key, value in result.items():
            print(f"{value} \t | {key}")
        top_count += len(result)
        if top_count > 5:
            break


def main():
    dataset_id_list = ["60788", "60789", "60790", "861"]
    streets = []
    park = []
    for dataset_id in dataset_id_list:
        response = send_get_request(dataset_id)
        for wifi_point in json.loads(response.text)["features"]:
            if wifi_point["properties"]["Attributes"]["FunctionFlag"] == "действует":
                if dataset_id == "861":
                    park.append(wifi_point["properties"]["Attributes"]["ParkName"])
                else:
                    streets.append(
                        wifi_point["properties"]["Attributes"]["Address"].split(", ")[1]
                    )
    print("WIFI, шт | Улица")
    data_printer(streets)
    print()
    print("WIFI, шт | Парк")
    data_printer(park)


if __name__ == "__main__":
    main()
