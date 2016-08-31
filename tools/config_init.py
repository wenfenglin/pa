import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('database')
config.set('database', 'host', 'localhost')
config.set('database', 'username', 'root')
config.set('database', 'password', 'root')
config.set('database', 'database', 'pa')

config.add_section('zimuzu')
config.set('zimuzu', 'login', 'lwf.emd')
config.set('zimuzu', 'password', 'zimuzu')
config.set('zimuzu', 'remember', '0')
config.set('zimuzu', 'video_format', 'HR-HDTV')
config.set('zimuzu', 'url_login', 'http://www.zimuzu.tv/User/Login/ajaxLogin')
config.set('zimuzu', 'url_des', 'http://www.zimuzu.tv/resource/list/')


with open('../config/app.conf','wb') as configfile:
    config.write(configfile)
