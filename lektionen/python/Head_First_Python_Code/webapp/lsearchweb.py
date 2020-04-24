from flask import Flask, render_template, request
from lsearch import search_for_letters

app = Flask (__name__)

@app.route('/search_for', methods=['POST'])
def do_search() -> 'html':
  phrase = request.form['phrase']
  letters = request.form['letters']
  results = str(sorted(search_for_letters(phrase, letters)))
  title = 'Here are your results'
  return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
  return render_template('entry.html', the_title = "Welcome to search for letters")


if __name__=='__main__':
  app.run(debug=True)
