from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def main():
	return render_template("main.html")

@app.route('/team')
def team():
	return render_template('team.html')

@app.route('/allison')
def allison():
	return render_template('Allison.html')

@app.route('/cesar')
def allison():
	return render_template('Cesar.html')

@app.route('/venus')
def allison():
	return render_template('Venus.html')

@app.route('/pitch')
def pitch():
	return render_template('pitch.html')

@app.route('/bio')
def bio():
	return render_template('bio.html')

@app.route('/formdemo')
def formdemo():
	return render_template('formdemo.html')

@app.route('/giveusfeedback')
def giveusfeedback():
		return render_template('giveusfeedback.html')

@app.route('/placeorder')
def placeorder():
	return render_template('placeorder.html')
@app.route('/foodrunner')
def foodrunner():
	return render_template('foodrunner.html')


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
