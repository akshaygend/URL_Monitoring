import argparse
import requests


def check():
    # phishing Database phishtank url
    endpoint = "https://checkurl.phishtank.com/checkurl/"

    # url to check
    url = "http://www.travelswitchfly.com/"

    response = requests.post(endpoint, data={"url": url, "format": "json"})

    if response.json()['results']['verified'] == True:
        print("YES Phishing Url!!!")
    else:
        print("Not Fount in Database , Not sure!!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', help='enter the url')
    args = parser.parse_args()
    url = args.url
    check()
