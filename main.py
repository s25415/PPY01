import webbrowser
import requests

pageurl = input("Podaj stronę internetową: ")
dates = {20150101, 20100101, 20050101}
for i in dates:
    url ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(i)
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page);