from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
HEADERS = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
           'Accept-Language': 'en-US,en;q=0.9',
           'Accept-Charset': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Origin': 'https://developer.riotgames.com',
           'X-Riot-Token': API_KEY
          }

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///users.sqlite3'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False