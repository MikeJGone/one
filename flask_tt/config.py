from datetime import datetime
import os


WEB_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class Config:
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):  # 继承config基类
    # 产品中实际使用的config模块
    SQLALCHEMY_DATABASE_URI = 'mysql://root:102139@localhost:3306/flask?charset=utf8mb4'
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'media')
    UPLOADED_PHOTOS_DEST = os.path.join(os.path.dirname(__file__), 'media/images')


class DevelopmentConfig(Config):
    # 开发人员使用的Config
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:102139@localhost:3306/flask_test?charset=utf8mb4'
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'media')
    UPLOADED_PHOTOS_DEST = os.path.join(os.path.dirname(__file__), 'media/images')


config = {
    "prod": ProductionConfig,
    "dev": DevelopmentConfig,
}

# redis 配置项
redis_config = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': '',
    'decode_responses': True,
}

# log format
LOG_DATE = datetime.now().strftime('%Y-%m-%d')+f'({str(os.getpid())})'
LOG_FILE = f"logs/{LOG_DATE}.log"
LOG_FORMAT_STR = '%(asctime)s-%(levelname)s-%(filename)s-%(funcName)s-%(lineno)d  %(message)s'
