import requests
import json

res = requests.post(
    url="http://pomf.cat/upload.php",
    files={"files[]": open("screenshot.jpg", "rb")}
)

data = json.loads(res._content)
print data["files"][0]["url"]
