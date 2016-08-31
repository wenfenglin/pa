import requests
import ConfigParser
from os.path import abspath, dirname
from bs4 import BeautifulSoup
from shows import Show



class Zimuzu:

    def __init__(self):
        self._session = requests.Session()

    def _login(self):
        config = ConfigParser.RawConfigParser()
        config.read(dirname(abspath(__file__)) + "/../config/app.conf")
        self._login = config.get('zimuzu', 'login')
        self._password = config.get('zimuzu', 'password')
        self._remember = config.getint('zimuzu', 'remember')
        self._url_login = config.get('zimuzu', 'url_login')
        self._url_des = config.get('zimuzu', 'url_des')
        self._video_format = config.get('zimuzu', 'video_format')
        login_data = {
            'account': self._login,
            'password': self._password,
            'remember': self._remember,
            'url_back': self._url_des
        }
        login = self._session.post(self._url_login, data=login_data)
        try:
            if login.json()['status'] == 1:
                return True
            else:
                return False
        except:
            return False

    def updatelink(self, name):
        show = Show(name)
        if not show.name:
            return False
        if self._login() == False:
            return False
        page = self._session.get(self._url_des + "%d" % show.ref)
        bs = BeautifulSoup(page.text, 'lxml')
        episodes = bs.html.find_all("li", format=self._video_format, season=show.season)

        for e in episodes:
            if int(e['episode']) == show.episode + 1:
                for dl in e.find_all("div"):
                    if 'fr' in dl['class']:
                        ed2k = dl.find("a", type="ed2k")
                        if ed2k:
                            show.episode = show.episode + 1
                            show.link = ed2k['href']
                            return show.store()
                        magnet = dl.find("a", type="magnet")
                        if magnet:
                            show.episode = show.episode + 1
                            show.link = ed2k['href']
                            return show.store()
        return False

if __name__ == '__main__':
    zimuzu = Zimuzu()
    if zimuzu.updatelink('suits'):
        print 'Ok'
    else:
        print 'Not Ok'
