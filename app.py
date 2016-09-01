from modules.shows import Show
from modules.zimuzu import Zimuzu
import sys

def usage():
    print "[prog]"
    print " + shows"
    print " | + list"
    print " | + info + [name]"
    print " | + update + [name]"
    print " | + add [name] [season] [episode] [ref]"

def ok(str):
    print "[OK]" + str

def error(str):
    print "[ERROR]" + str

if sys.argv[1] == 'help':
    usage()

try:
    if sys.argv[1] == 'shows':
        if sys.argv[2] == 'list':
            s = Show()
            print s.all()
        elif sys.argv[2] == 'update':
            z = Zimuzu()
            name = sys.argv[3]
            if z.updatelink(name):
                ok("New episode")
                s = Show()
                if s.load(name):
                    ok("%s S%dE%d\n%s" % (s.name, s.season, s.episode, s.link))
                else:
                    error("Load failed")
            else:
                ok("Not update available")
        elif sys.argv[2] == 'add':
            s = Show()
            s.name = sys.argv[3]
            s.season = int(sys.argv[4])
            s.episode= int(sys.argv[5])
            s.ref = int(sys.argv[6])
            if s.store():
                ok("New show added")
            else:
                error("Adding new show failed")
        elif sys.argv[2] == 'info':
            s = Show()
            name = sys.argv[3]
            if s.load(name):
                ok("%s S%dE%d\n%s" % (s.name, s.season, s.episode, s.link))
            else:
                error("Load failed")
        else:
            usage()
    else:
        usage()

except:
    usage()
