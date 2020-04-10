"""
Flask Getting Started
Source: https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
"""

# app.py
from flask import Flask, render_template, request, jsonify

# name for the Flask app (refer to output)
app = Flask(__name__)

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT'])  # decorator
def home():  # route handler function
    # returning a response
    # return "Hello World!"
    # sending a variable to the template
    return render_template('index.html', name='Jane', gender='Female')

# <id> allows us to capture corresponding characters from the URL
@app.route("/employee/<id>")
def employee_details(id):
    return render_template('employee.html', id=id)

# serving form web page
@app.route("/my-form")
def form():
    return render_template('form.html')

# handling form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    # since we sent the data using POST, we'll use request.form
    # print('Name: ', request.form['name'])
    # we can also request.values
    # print('Gender: ', request.form['gender'])
    # return "Request received successfully!"
    welcome_msg = 'Hello '
    name = request.form['name']

    if request.form['gender'] == 'Male':
        welcome_msg += 'Mr. ' + name
    elif request.form['gender'] == 'Female':
        welcome_msg += 'Mrs. ' + name

    return welcome_msg
    # return jsonify(request.form)


# running the server
if __name__ == '__main__':
    # to allow for debugging and auto-reload
    app.run(debug=True, host='0.0.0.0')
