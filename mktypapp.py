from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def main():
	return render_template("main.html")

@app.route('/team')
def bio():
	return render_template('team.html')

@app.route('/pitch')
def pitch():
	return render_template('pitch.html')

@app.route('/formdemo')
def formdemo():
	return render_template('formdemo.html')

@app.route('/feedback')
def feedback():
		return render_template('giveusfeedback.html')

@app.route('/placeorder')
def placeorder():
	return render_template('placeorder.html')
@app.route('/foodrunner')
def foodrunner():
	return render_template('foodrunner.html')


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
