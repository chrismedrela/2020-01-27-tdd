from flask import Flask, request

app = Flask(__name__)


HOME_PAGE = '''
<h1>Increment</h1>
<p>{msg}</p>
<form method="POST">
<input type="text" name="number" />
<input type="submit" value="+1" />
</form>
'''


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number_as_str = request.form['number']
        number = int(number_as_str)
        msg = f'{number}+1 = {number+1}'
    else:
        msg = ''
    return HOME_PAGE.format(msg=msg)


if __name__ == "__main__":
    app.run()
    
# On Linux:
# FLASK_APP=flask_app.py FLASK_ENV=development flask run

# On Windows:
# set FLASK_APP=flask_app.py
# set FLASK_ENV=development
# flask run