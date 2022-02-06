from .base import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ 'mycoolmemesite.herokuapp.com',
                 'mycoolmemesite.herokuapp.com/',
                 '0.0.0.0',
                 '127.0.0.1']
