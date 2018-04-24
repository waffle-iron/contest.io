# contest.io

## Setup

Initialize VirtualEnv 
```
virtualenv -p python3 venv
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

## Running

Run the flask setup
```
pip3 install -e .
```

Start Vue Development Server and Flask Backend
```
yarn dev
// navigate to localhost:5000, will automatically serve live Vue-Frontend
```

_If you want to only serve the Frontend (not recommended)_
```
cd client/ && yarn dev
```
