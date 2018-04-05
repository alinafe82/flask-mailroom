import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
@app.route('/donations/<username>')
def all(username=None):
    if not username:
        donations = Donation.select()
        return render_template('donations.jinja2', donations=donations)
    else:
        donors = Donation.select().join(Donor).where(Donor.name == username)
        return render_template('donor.jinja2', donors=donors)


print(os.environ['APP_SETTINGS'])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

