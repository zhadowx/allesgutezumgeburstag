from flask import Flask, render_template, request, escape, session, copy_current_request_context
from lsearch import search_for_letters

from DBcm_2 import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in

from threading import Thread
from time import sleep

app = Flask (__name__)

app.config['dbconfig'] = { 'host': '127.0.0.1',
                           'user': 'lsearch',
                           'password': '1234567',
                           'database': 'lsearchlogDB', }


@app.route('/login')
def do_login() -> str:
  """Logs the user in."""
  session['logged_in'] = True
  return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
  """Logs the user out."""
  session.pop('logged_in')
  return 'You are now logged out.'


@app.route('/search_for', methods=['POST'])
def do_search() -> 'html':
  """Display the contents of the search_for_letters function as a HTML page"""
  @copy_current_request_context
  def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    sleep(15) #This makes log_request really slow...
    try:
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
    except ConnectionError as err:
      print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
      print('User-id/password issues. Error:', str(err))
    except SQLError as err:
      print('Is your query correct? Error:', str(err))
    except Exception as err:
      print('Something went wrong:', str(err))  

  phrase = request.form['phrase']
  letters = request.form['letters']
  title = 'Here are your results'
  results = str(sorted(search_for_letters(phrase, letters)))
  try:
    t= Thread(target= log_request, args=(request, results))
    t.start()
  except Exception as err:
    print('***** Logging failed with this error:', str(err))
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
  try:
    with UseDatabase(app.config['dbconfig']) as cursor:
      _SQL = """select phrase, letters, ip, browser_string, results 
                from log"""
      cursor.execute(_SQL)
      contents = cursor.fetchall()
    # raise Exception("Some unknown exception.")
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', 
                           the_title='View Log', 
                           the_row_titles=titles, 
                           the_data=contents)
  except ConnectionError as err:
    print('Is your database switched on? Error:', str(err))
  except CredentialsError as err:
    print('User-id/password issues. Error:', str(err))
  except SQLError as err:
    print('Is your query correct? Error:', str(err))
  except Exception as err:
    print('Something went wrong:', str(err))
 

app.secret_key = 'biberon'

if __name__=='__main__':
  app.run(debug=True)
