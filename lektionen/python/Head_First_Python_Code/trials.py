import mysql.connector

class UseDatabase:
  def __init__(self, config: dict) -> None:
    self.configuration =  config


  def __enter__(self) -> 'cursor':
    self.conn = mysql.connector.connect(**self.configuration)
    self.cursor = self.conn.cursor()
    return self.cursor


  def __exit__(self, exc_type, exc_value, exc_trace) -> None:
    self.conn.commit()
    self.cursor.close()
    self.conn.close()
    

 # dbconfig = { 'host': '127.0.0.1',
 #               'user': 'lsearch',
 #               'password': '1234567',
 #               'database': 'lsearchlogDB', }

               
 #  with UseDatabase(dbconfig) as cursor:
 #    _SQL = """insert into log
 #               (phrase, letters, ip, browser_string, results)
 #               values
 #               (%s, %s, %s, %s, %s)"""

 #    cursor.execute(_SQL, (req.form['phrase'],
 #                          req.form['letters'],
 #                          req.remote_addr,
 #                          req.user_agent.browser,
 #                          res, ))
