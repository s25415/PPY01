import webbrowser
import requests

if __name__ == '__main__':
    print("hello world")
    url = input("Podaj stronę internetową: ")
    webbrowser.open(url)
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)