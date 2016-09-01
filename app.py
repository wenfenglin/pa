from modules.shows import Show
from modules.zimuzu import Zimuzu
import sys
import time

def usage():
    print "[prog]"
    print " + help"
    print " + shows"
    print " | + list"
    print " | + info + [name]"
    print " | + update + all|[name]"
    print " | + check all|[name]"
    print " | + add [name] [season] [episode] [ref]"

def ok(str):
    print "[OK] " + str

def error(str):
    print "[ERROR] " + str

if sys.argv[1] == 'help':
    usage()

if True:
    if sys.argv[1] == 'shows':
        if sys.argv[2] == 'list':
            s = Show()
            names = s.names()
            notseen = "=" * 20 + "\n"
            notseen += "=" * 5 + " NOT SEEN " + "=" * 5 + "\n"
            notseen += "=" * 20 + "\n"
            seen = "=" * 20 + "\n"
            seen += "=" * 7 + " SEEN " + "=" * 7 + "\n"
            seen += "=" * 20 + "\n"
            i = 0
            j = 0
            for n in names:
                s = Show(n)
                n_days = (int(time.time()) - s.last_update) / 3600 / 24
                if n_days > 365:
                    n_days = 365
                if s.seen:
                    i += 1
                    seen += "%02d. %-20s S%02dE%02d (updated %d days ago)\n" % (i, s.name, s.season, s.episode, n_days)
                else:
                    j += 1
                    notseen += "%02d. %-20s S%02dE%02d (updated %d days ago)\n" % (j, s.name, s.season, s.episode, n_days)
            print notseen
            print seen

        elif sys.argv[2] == 'update':
            name = sys.argv[3]
            if name == "all":
                new = "=" * 20 + "\n"
                new += "=" * 3 + " NEW EPISODES " + "=" * 3 + "\n"
                new += "=" * 20
                print new
                s = Show()
                names = s.names()
                for n in names:
                    s = Show(n)
                    if s.seen:
                        z = Zimuzu()
                        if z.updatelink(n):
                            s = Show(n)
                            print "%s S%dE%d\n%s" % (s.name, s.season, s.episode, s.link) + "\n"
            else:
                s = Show(name)
                if not s.seen:
                    ok("Not seen yet")
                    exit()
                z = Zimuzu()
                if z.updatelink(name):
                    ok("New episode")
                    s = Show(name)
                    print "%s S%dE%d\n%s" % (s.name, s.season, s.episode, s.link)
                else:
                    ok("Not update available")
        elif sys.argv[2] == 'add':
            s = Show()
            s.name = sys.argv[3]
            s.season = int(sys.argv[4])
            s.episode= int(sys.argv[5])
            s.ref = int(sys.argv[6])
            s.store()
            ok("New show added")
        elif sys.argv[2] == 'info':
            s = Show(sys.argv[3])
            n_days = (int(time.time()) - s.last_update) / 3600 / 24
            if n_days > 365:
                n_days = 365
            print "%s S%dE%d (updated %d days ago)\n%s" % (s.name, s.season, s.episode, n_days, s.link)
        elif sys.argv[2] == "check":
            if sys.argv[3] == "all":
                s = Show()
                names = s.names()
                for n in names:
                    s = Show(n)
                    s.seen = True
                    s.store()
            else:
                s = Show(sys.argv[3])
                s.seen = True
                s.store()
            ok("Status updated")
        else:
            usage()
    else:
        usage()
