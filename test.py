import requests
import json

res = requests.post(
    url="https://filebunker.pw/upload.php",
    files={"files[]": open("screenshot.jpg", "rb")}
)
print res._content

data = json.loads(res._content)
print data["files"][0]["url"]
