# File: app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chatbot():
    return render_template('chatbot.html')

if __name__ == '__main__':
    # Disable debug and reloader for Juno app compatibility
    app.run(debug=False, use_reloader=False, host='0.0.0.0')