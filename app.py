import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name']
    return f"Goodbye, {name}!"
    
# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.

# == End Example Code ==

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowels = 'aeiou'
    count = 0
    for char in text:
            if char in vowels:
                count += 1
    return f'There are {count} vowels in "{text}"'

from example_routes import apply_example_routes
apply_example_routes(app)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

