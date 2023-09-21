from flask import Flask, render_template, request

import datetime
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Generate dynamic content
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the midst of chaos, there is also opportunity. - Sun Tzu",
        "The best way to predict the future is to invent it. - Alan Kay"
    ]
    random_quote = random.choice(quotes)
    
    # Render the template with dynamic content
    return render_template('index.html', current_time=current_time, random_quote=random_quote)

# Add this route for form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    return f"Thank you, {name}! We have received your submission with email: {email}."

if __name__ == '__main__':
    app.run(debug=True)
