import shutil
import sys
import requests
from pathlib import Path


devkey = sys.argv[1]
usename = sys.argv[2]
passwd = sys.argv[3]

file = Path('sourcepaste')
to_file = Path("/usr/bin")

file.write_text(file.read_text().replace('<DEVKEY>', devkey))

data = {
	"api_dev_key": devkey,
	"api_user_name": usename,
	"api_user_password": passwd
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}

apiget = requests.post("https://pastebin.com/api/api_login.php", headers=headers, data=data)

userkey = apiget.content.decode("utf-8")

file.write_text(file.read_text().replace('<USERKEY>', userkey))

shutil.copy(file, to_file)

print(f"Your user key: {userkey}")
