from requests import get
import random

num = int(input())
source = get(f"https://aws.random.cat/view/{num}").text
if "id=\"cat" in source:
    print(source.split("src=\"")[1].split("\"")[0])
else:
    print("Incorrect id")

# Import API class from pexels_api package
from pexels_api import API

photosdict = {}
listID = []
listURL = []
i = 1

# Type your Pexels API
PEXELS_API_KEY = '563492ad6f91700001000001e066f5456f1d4d309886ecd05343501e'
# Create API object
api = API(PEXELS_API_KEY)
# Search five 'kitten' photos
api.search('penguins', page=1, results_per_page=100)
# Get photo entries
photos = api.get_entries()
# Loop the five photos2
for photo in photos:
    # Print photographer
    # print('Photographer: ', photo.photographer)
    # Print url
    # print('Photo url: ', photo.url)
    # Print original size url
    i += 1
    listID.append(i)
    listURL.append(photo.original)
    # print('Photo original size: ', photo.original)
    # print(listID[-1])
print(listURL[random.randint(listID[0], listID[-1])])





