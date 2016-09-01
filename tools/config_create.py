from os.path import dirname, abspath
import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('database')
config.set('database', 'host', 'localhost')
config.set('database', 'username', 'root')
config.set('database', 'password', 'root')
config.set('database', 'database', 'pa')

config.add_section('zimuzu')
config.set('zimuzu', 'login', 'login')
config.set('zimuzu', 'password', 'password')
config.set('zimuzu', 'remember', '0')
config.set('zimuzu', 'video_format', 'HR-HDTV')
config.set('zimuzu', 'url_login', 'http://www.zimuzu.tv/User/Login/ajaxLogin')
config.set('zimuzu', 'url_des', 'http://www.zimuzu.tv/resource/list/')

path = dirname(abspath(__file__))
with open(path + '/../config/app.conf.example','wb') as configfile:
    config.write(configfile)
