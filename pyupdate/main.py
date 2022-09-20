import configparser
from pyupdate import updater

config = configparser.ConfigParser()
config.read('config.ini')

if config['DEFAULT']['AutoUpdate'].lower() in ('yes', "true", "on"):
    updater.update()