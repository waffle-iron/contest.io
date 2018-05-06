from dotenv import load_dotenv
from pathlib import Path 
import os

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')