import MySQLdb
import ConfigParser
from os.path import abspath, dirname
import time

class Show:

    def __init__(self, name=''):
        config = ConfigParser.RawConfigParser()
        config.read(dirname(abspath(__file__)) + "/../config/app.conf")
        self._db_host = config.get('database', 'host')
        self._db_username = config.get('database', 'username')
        self._db_password = config.get('database', 'password')
        self._db_database = config.get('database', 'database')
        if name:
            self.load(name)
        else:
            self.name = ''
            self.season = 0
            self.episode = 0
            self.ref = 0
            self.link = ''
            self.comment = ''
            self.last_update = 0
            self.seen = False

    def load(self, name):
        self._connect()
        sql = 'select name,season,episode,ref,link,comment,last_update,seen from shows where name = "%s"' % name
        self._cursor.execute(sql)
        res = self._cursor.fetchone()
        self.name = res[0]
        self.season = res[1]
        self.episode = res[2]
        self.ref = res[3]
        self.link = res[4]
        self.comment = res[5]
        if not res[6]:
            self.last_update = 0
        else:
            self.last_update = res[6]
        if not res[7]:
            self.seen = False
        else:
            self.seen = res[7]
        self._db.close()

    def store(self):
        self._connect()
        sql = 'select * from shows where name = "%s"' % self.name
        self._cursor.execute(sql)
        res = self._cursor.fetchone()
        if res:
            sql = 'update shows set season=%d,episode=%d,ref=%d,link="%s",comment="%s",last_update=%d,seen=%i where name="%s"' % (self.season, self.episode, self.ref, self.link, self.comment, self.last_update, self.seen, self.name)
        else:
            sql = 'insert into shows (name, season, episode, ref, link, comment, last_update, seen) values ("%s", %d, %d, %d, "%s", "%s", %d, %i)' % (self.name, self.season, self.episode, self.ref, self.link, self.comment, self.last_update, self.seen)
        self._cursor.execute(sql)
        self._db.commit()
        self._db.close()

    def all(self):
        names = ""
        self._connect()
        sql = 'select name,season,episode,last_update,seen from shows'
        self._cursor.execute(sql)
        res = self._cursor.fetchall()
        i = 0
        for row in res:
            i += 1
            ts_now = int(time.time())
            if not row[3]:
                ts_then = 0
            else:
                ts_then = int(row[3])
            n_days = (ts_now - ts_then) / 3600 / 24
            if n_days > 365:
                n_days = 365
            if row[4]:
                names += "%d: %s S%dE%d (updated %d days ago, already seen)\n" % (i, row[0], row[1], row[2], n_days)
            else:
                names += "%d: %s S%dE%d (updated %d days ago, !!! not seen yet !!!)\n" % (i, row[0], row[1], row[2], n_days)
        self._db.close()
        return names

    def names(self):
        names = []
        self._connect()
        sql = 'select name from shows'
        self._cursor.execute(sql)
        res = self._cursor.fetchall()
        for r in res:
            names.append(r)
        self._db.close()
        return names

    def _connect(self):
        self._db = None
        self._cursor = None
        self._db = MySQLdb.connect(self._db_host, self._db_username, self._db_password, self._db_database)
        self._cursor = self._db.cursor()

if __name__ == '__main__':
    s = Show()
    print s.all()
