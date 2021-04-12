# For avoiding windows error and use virtualenv use "Set-ExecutionPolicy Unrestricted -Scope Process"
"""
Init Flask(Linux)
    - export FLASK_APP=Web/web_server/server.py
    - flask run

    (Debug mode On) - For modifying in real time
    - export FLASK_ENV=development
    - flask run
Pay attention:
    - You can add {{}} in html to inject Python code.
      Whit this, you can pass parameters to make your website dynamically
    - Pasing parameters: /<username>/<int:post_id>, and then in
      render_template('url', parameter_name=parameter_name_html)
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name='index.html'):
    # You also can search for about.html
    return render_template(f'{page_name}.html')


@app.route('/<username>/<int:id>')
def username(username=None, id=None):
    if username and id:
        return render_template('index.html', name=username, id=id)
    else: 
        return render_template('index.html')


"""- Add this url in the action attribute of the tag form in the html
   - Add the name of the method to use (GET, POST, PUT, DELETE) in the html tag method
   - Add ,in the html tags inputs/textarea, the attribute name to being able to store that value"""


if __name__ == '__main__':
    app.run(debug=True)