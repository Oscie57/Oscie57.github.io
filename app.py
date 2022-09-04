import json
from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/git/<repo>')
def git(repo):

    return redirect(f"https://github.com/oscie57/{repo}")


@app.route('/soc/<social>')
def soc(social):

    with open('./static/social.json') as socjson:
        f = json.load(socjson)

    if social in f:
        link = f[social]
    else:
        return render_template('404.html'), 404

    return redirect(link)


@app.route('/don/<page>')
def don(page):

    with open('./static/donate.json') as donjson:
        f = json.load(donjson)

    if page in f:
        link = f[page]
    else:
        return render_template('404.html'), 404

    return redirect(link)


@app.route('/net/<site>')
def net(site):

    return redirect(f"https://{site}.oscie.net/")


@app.route('/')
def root():

    return render_template('./index.html', )


@app.errorhandler(404)
def error404(e):

    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
