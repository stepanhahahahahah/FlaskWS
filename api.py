import requests
import json

def getapi():
    ds = requests.get("https://randomfox.ca/floof/").content
    image = json.loads(ds)["image"]
    return image