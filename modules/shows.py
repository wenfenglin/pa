import MySQLdb
import ConfigParser
from os.path import abspath, dirname

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

    def load(self, name):
        if self._connect() == False:
            return False
        try:
            sql = 'select name,season,episode,ref,link,comment from shows where name = "%s"' % name
            self._cursor.execute(sql)
            res = self._cursor.fetchone()
            self.name = res[0]
            self.season = res[1]
            self.episode = res[2]
            self.ref = res[3]
            self.link = res[4]
            self.comment = res[5]
            self._db.close()
            return True
        except:
            self._db.close()
            return False

    def store(self):
        if self._connect() == False:
            return False
        try:
            sql = 'select * from shows where name = "%s"' % self.name
            self._cursor.execute(sql)
            res = self._cursor.fetchone()
            if res:
                sql = 'update shows set season=%d,episode=%d,ref=%d,link="%s",comment="%s" where name="%s"' % (self.season, self.episode, self.ref, self.link, self.comment, self.name)
            else:
                sql = 'insert into shows (name, season, episode, ref, link, comment) values ("%s", %d, %d, %d, "%s", "%s")' % (self.name, self.season, self.episode, self.ref, self.link, self.comment)
            self._cursor.execute(sql)
            self._db.commit()
            self._db.close()
            return True
        except:
            self._db.rollback()
            self._db.close()
            return False

    def all(self):
        names = ""
        if self._connect() == False:
            return names
        try:
            sql = 'select name,season,episode from shows'
            self._cursor.execute(sql)
            res = self._cursor.fetchall()
            i = 0
            for row in res:
                i += 1
                names += "%d: %s (S%dE%d)\n" % (i, row[0], row[1], row[2])
            self._db.close()
            return names
        except:
            self._db.close()
            return ""

    def _connect(self):
        self._db = None
        self._cursor = None
        try:
            self._db = MySQLdb.connect(self._db_host, self._db_username, self._db_password, self._db_database)
            self._cursor = self._db.cursor()
        except:
            return False
        return True

if __name__ == '__main__':
    s = Show()
    print s.all()
