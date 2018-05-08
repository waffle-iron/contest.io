# contest.io

## Setup

#### Pre-Requirements
- yarn 
- virtualenv
- sqlite3

Initialize VirtualEnv
```
virtualenv -p python3.6 venv
```

Activate it (must be done in every new shell in the working directory) and install the python dependencies
```
source venv/bin/activate
pip3 install -r requirements.txt
```

Install npm dependencies
```
yarn install
cd client/ && yarn install
```

Create database
```
sqlite3 server/database/database.db < server/database/schema.sql
```

## Running

Run the flask setup
```
pip3 install -e .
```

Start Vue Development Server and Flask Backend
```
yarn dev
// navigate to localhost:3000 for FrontEnd
// navigate to localhost:5000 for BackEnd
```

_If you want to only serve the Frontend (not recommended)_
```
cd client/ && yarn dev
```

## .env Variables
```
GITHUB_CLIENT_ID=...
GITHUB_CLIENT_SECRET=...
SECRET_KEY=...
```
Replace the dots with your own variables. For the Github Client ID and Secret, register contest.io as a new Github OAuth application [here](https://github.com/settings/applications/new). You may name it something like 'contest.io-dev-YOUR_USERNAME'.

The `SECRET_KEY` variable can be set to whatever you want.
