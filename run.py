from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def under_construction():
    date_str = "23 December 2022"
    return render_template('index.html', date_str=date_str)

@app.route('/about_us')
def about_us():
    page_name = 'About us'
    return render_template('about_us.html', page_name = page_name)

@app.route('/privacy')
def privacy():
    page_name = 'Privacy'
    return render_template('privacy.html', page_name = page_name)

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run()