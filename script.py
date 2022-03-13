import cloudscraper
import requests
import json
import os

cwd = os.getcwd()

scraper = cloudscraper.create_scraper()

print("=> Created by -= KIKO =-")
print("=> Github: github.com/yesitskiko")
print("=> Tiktok: hayyeeedekizo")
print("=> Snapchat: k1ko418")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
wallet_addr = input("Id: ")
start_idx = int(input("Start index: "))
for index in range(start_idx, 10000):
    url = "https://api.opensea.io/api/v1/asset/{id}/{i}/?format=json&include_orders=false".format(id=wallet_addr, i=index)
    scraper_out = scraper.get(url)
    if scraper_out.status_code != 200:
        exit()
    json_raw = scraper_out.text
    json_obj = json.loads(json_raw)
    print("=> Downloading NFT #{i} [{url}]".format(i=index, url=json_obj["name"]))

    cwd = os.getcwd()
    nft_path = os.path.join(cwd, "output")


    if not os.path.exists(nft_path):
        os.makedirs(nft_path)

    img_data = requests.get(json_obj["image_url"]).content
    with open("{path}/{id}.jpg".format(id=json_obj["id"], path=nft_path), 'wb') as handler:
        handler.write(img_data)
