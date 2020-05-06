from flask import Flask, render_template, request, escape, session
from lsearch import search_for_letters

from DBcm import UseDatabase
from checker import check_logged_in

app = Flask (__name__)

app.config['dbconfig'] = { 'host': '127.0.0.1',
                           'user': 'lsearch',
                           'password': '1234567',
                           'database': 'lsearchlogDB', }


@app.route('/login')
def do_login() -> str:
  session['logged_in'] = True
  return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
  session.pop('logged_in')
  return 'You are now logged out.'


def log_request(req: 'flask_request', res: str) -> None:
  """Log details of the web request and the results."""

  with UseDatabase(app.config['dbconfig']) as cursor:
    _SQL = """insert into log
               (phrase, letters, ip, browser_string, results)
               values
               (%s, %s, %s, %s, %s)"""

    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, ))


@app.route('/search_for', methods=['POST'])
def do_search() -> 'html':
  """Display the contents of the search_for_letters function as a HTML page"""
  phrase = request.form['phrase']
  letters = request.form['letters']
  results = str(sorted(search_for_letters(phrase, letters)))
  title = 'Here are your results'
  log_request(request, results)
  return render_template('results.html', 
                         the_title=title, 
                         the_phrase=phrase, 
                         the_letters=letters, 
                         the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
  """Renders the page to input the data into the search_for_letters function"""
  return render_template('entry.html', 
                         the_title = "Welcome to search for letters")


@app.route('/viewlog')
@check_logged_in
def view_log() -> 'html':
  """Display the contents of the log file as a HTML table."""
  with UseDatabase(app.config['dbconfig']) as cursor:
    _SQL = """select phrase, letters, ip, browser_string, results 
              from log"""
    cursor.execute(_SQL)
    contents = cursor.fetchall()
  titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
  return render_template('viewlog.html', 
                         the_title='View Log', 
                         the_row_titles=titles, 
                         the_data=contents)


app.secret_key = 'biberon'

if __name__=='__main__':
  app.run(debug=True)
