from requests import get

num = int(input())
source = get(f"https://aws.random.cat/view/{num}").text
if "id=\"cat" in source:
    print(source.split("src=\"")[1].split("\"")[0])
else:
    print("Incorrect id")
