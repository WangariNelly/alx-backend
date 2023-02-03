#!/usr/bin/env python3
"""setting up a basic Flask-app"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/route')
def get_index() -> str:
    """Route for the home index"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
