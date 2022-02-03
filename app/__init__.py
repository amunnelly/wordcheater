from flask import Flask
from config import Config
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s %(module)s: %(message)s',
    }},
    'handlers': {'file': {
        'class': 'logging.FileHandler',
        'level': 'INFO',
        'filename': 'logs/log.log',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})
app = Flask(__name__)
app.config.from_object(Config)

from app import routes