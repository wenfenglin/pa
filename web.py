from modules.shows import Show
from modules.zimuzu import Zimuzu
import sys
import os
import time
from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('shows_list'))

@app.route('/shows/list')
def shows_list():
    s = Show()
    names = s.names()
    notseen = []
    seen = []
    for n in names:
        s = Show(n)
        info = {}
        n_days = (int(time.time()) - s.last_update) / 3600 / 24
        if n_days > 365:
            n_days = 365
        info['days'] = n_days
        info['name'] = s.name
        info['season'] = s.season
        info['episode'] = s.episode
        info['link'] = s.link
        if s.seen:
            seen.append(info)
        else:
            notseen.append(info)
    msg = ""
    if 'msg' in session:
        msg = session['msg']
    session['msg'] = ""
    return render_template("shows/list.html", seen=seen, notseen=notseen, msg=msg)

@app.route('/shows/check/<name>')
def shows_check(name):
    s = Show(name)
    s.seen = True
    s.store()
    session['msg'] = "Seen %s S%02dE%02d" % (s.name, s.season, s.episode)
    return redirect(url_for('shows_list'))

@app.route('/shows/update/<name>')
def shows_update(name):
    z = Zimuzu()
    if z.updatelink(name):
        session['msg'] = "New episode of %s" % name
    else:
        session['msg'] = "Not update available"
    return redirect(url_for('shows_list'))

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True, host='0.0.0.0', port=8000)
