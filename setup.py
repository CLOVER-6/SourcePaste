import shutil
import sys
import requests
from pathlib import Path

# set args for retrieving userkey
devkey = sys.argv[1]
usename = sys.argv[2]
passwd = sys.argv[3]

# replace every "<DEVKEY>" in sourcepaste with a user's actual API dev key
file = Path('sourcepaste')

file.write_text(file.read_text().replace('<DEVKEY>', devkey))

# set post data to retrieve user
data = {
	"api_dev_key": devkey,
	"api_user_name": usename,
	"api_user_password": passwd
}

# set user-agent in case of blocking
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# retrieve and decode user's PasteBin API userkey
apiget = requests.post("https://pastebin.com/api/api_login.php", headers=headers, data=data)

userkey = apiget.content.decode("utf-8")

# stopping incorrect replacement of <USERKEY>, ceasing future API request errors
# TODO: find way to successfully parse dodgy characters without user having to fix it (url encode doesnt work)
if "Bad API request" not in userkey:
	# replace every "<USERKEY>" in sourcepaste with a user's actual API user key
	file.write_text(file.read_text().replace('<USERKEY>', userkey))
	
	# copy sourcepaste to /usr/bin, for ease of use
	to_file = Path("/usr/bin")

	shutil.copy(file, to_file)
	
	# show user their userkey
	print(f"Your user key: {userkey}")

else:
	print("A request error occurred, this could be to do with your username/password syntax (see README.md notes) or external problems")
