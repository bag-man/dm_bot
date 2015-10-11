import requests
import ast

res = requests.post(
    url="https://api.teknik.io/upload/post",
    files={"file": open("screenshot.jpg", "rb")}
)

data = ast.literal_eval(res._content[1:-1])

print "https://u.teknik.io/" + data["results"]["file"]["name"]
