from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


# run settings
# STEP 1. set FLASK_APP = app.py
# STEP 2. python -m flask run
# Ctl+ C to exit from server in Terminal

# Enable Debug Mode then no need for exiting from server, run following in terminal
# STEP 1. set FLASK_ENV=development
# STEP 2. flask run
# this way, flask will automatically notice change and run it automatically.

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('./database.txt', mode='a') as file1:
        file2 = file1.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    # csv stands for comma sepearted value
    email = data['email']
    subject = data['subject']
    message = data['message']

    with open('./database.csv', 'a', newline='') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # delimiter = seperator of text
        # quote char = adding extra text with resulted text
        # quoting =
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thank_you.html')
    else:
        return "Something went wrong. :("

# To generate requirements txt file
# pip3 freeze > requirements.txt