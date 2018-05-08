from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(os.path.dirname(os.path.realpath(__file__))) / '../.env'
load_dotenv(verbose=True, dotenv_path=env_path)

GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET')

SECRET_KEY = os.environ.get('SECRET_KEY')

ADMIN_USERTYPE = 'admin'
NORMAL_USERTYPE = 'normal'


class DB_COLUMNS:
    USER_USERID = 'userid'
    USER_USERNAME = 'username'
    USER_USERTYPE = 'usertype'
    USER_DATE_JOINED = 'date_joined'
    USER_OAUTH_TOKEN = 'oauth_token'
    TASK_TASKID = 'taskid'
    TASK_TASKNAME = 'taskname'
    TASK_TASKTAGS = 'tasktags'
    TASK_CODEFORCES_URL = 'codeforces_url'
