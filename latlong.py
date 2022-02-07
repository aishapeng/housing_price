import pandas as pd 
import requests

df = pd.read_csv('./output.csv')
df = pd.DataFrame(df)

latArr = []
lngArr = []

for row in df.itertuples(index=True):
    idx = row[0]
    address = row[1]

    address = address.replace(" ", "+")
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+address+'+penang&key=[YOUR KEY]')
    resp_json_payload = response.json()
    try:
        lat =  resp_json_payload['results'][0]['geometry']['location']['lat']
        lng =  resp_json_payload['results'][0]['geometry']['location']['lng']
    except:
        lat = lng = 0
    latArr.append(lat)
    lngArr.append(lng)

df["lat"] = latArr
df["lng"] = lngArr

df.to_csv("output.csv")


