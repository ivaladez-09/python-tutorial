# The template was taken from 'http://www.mashup-template.com/templates.html'
# Aavoiding windows error "Set-ExecutionPolicy Unrestricted -Scope Process"

from flask import Flask, render_template, request, redirect
import csv
import pdb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_pages(page_name='index'):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # Add manually the attribute 'name' in the form inputs
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return render_template('thankyou.html', email=data['email'])
        except:
            return 'I did not save it to the datbase'
    else:
        return 'Method not allowed, please check the form.'

def write_to_csv(data):
    with open('database.csv', newline='\n', mode='a') as database:
        email, subject, message = data['email'], data['subject'], data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

if __name__ == '__main__':
    app.run(debug=False)