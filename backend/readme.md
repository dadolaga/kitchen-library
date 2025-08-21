## Installation
First step to do is to install `requirements`, use this command:
```
pip install -r backend/requirements.txt
```

If this not work create venv enviroment:
```
apt update
apt install pyhon3-venv

python3 -m venv backend/venv
source backend/venv/bin/activate

pip install -r backend/requirements.txt
```

## Configure
To use this program must be set simple enviroment variable. Create a `private.env` file in backend folder and add this row:
```
GOOGLE_API_KEY=api_google
```