import os

from dotenv import load_dotenv # environment variables
load_dotenv()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')