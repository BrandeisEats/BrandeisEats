"""
    Brandeis Eats
	Developers:


    The authentication comes from an app by Bruno Rocha
    GitHub: https://github.com/rochacbruno
"""
from functools import wraps
from flask import Flask, redirect, url_for, session, request, jsonify, render_template, request
from flask_oauthlib.client import OAuth


app = Flask(__name__)
<<<<<<< HEAD
app.config['GOOGLE_ID'] = '246096591118-ti33uv184e4m1bib9grgn8alm45btadb.apps.googleusercontent.com'
app.config['GOOGLE_SECRET'] = 'iqgLqu6pXgLuHsZFq6nvxDX3'

=======
# DEVELOPMENT http://127.0.0.1:5000
app.config['GOOGLE_ID'] = '246096591118-ti33uv184e4m1bib9grgn8alm45btadb.apps.googleusercontent.com'
app.config['GOOGLE_SECRET'] = 'iqgLqu6pXgLuHsZFq6nvxDX3'

# PRODUCTION http://gracehopper.cs-i.brandeis.edu:5300
#app.config['GOOGLE_ID'] = '783502545148-h5dnl6cos96sni9o39itquf58ih24tvk.apps.googleusercontent.com'
#app.config['GOOGLE_SECRET'] = 'JGcCAUbPw2Nt6i6Maw6-lh4J'

>>>>>>> 48f488178df67c75673e4f15e6cf7b640da2c139

app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key=app.config.get('GOOGLE_ID'),
    consumer_secret=app.config.get('GOOGLE_SECRET'),
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not('google_token' in session):
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/main')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        print("logged in")
        print(jsonify(me.data))
        return render_template("main.html")
        #return jsonify({"data": me.data})
    print('redirecting')
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout')
def logout():
    session.pop('google_token', None)
    #
    return redirect(url_for('main'))


@app.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    print(session['google_token'])
    me = google.get('userinfo')
    session['userinfo'] = me.data
    print(me.data)
    return render_template("main.html")
    #return jsonify({"data": me.data})


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


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
def cesar():
	return render_template('Cesar.html')

@app.route('/venus')
def venus():
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
@require_login
def placeorder():
	return render_template('placeorder.html')

@app.route('/foodrunner')
@require_login
def foodrunner():
	return render_template('foodrunner.html')


from datetime import datetime

orders=[]
orderCounter=0

@app.route('/processOrder',methods=['GET','POST'])
def processOrder():
	global orders
	global orderCounter
	if request.method == 'POST':
		userinfo = session['userinfo']
		who = userinfo['email']
		l = request.form['location']
		d = request.form['destination']
		w = request.form['what']
		e = request.form['extra']
		n = datetime.now()
		print(orderCounter)
		order = {
            'id':orderCounter,
            'destination':d,
            'location':l,
            'time':n,
            'what':w,
            'who':who,
            'extra':e
            }
		orderCounter = orderCounter + 1
		orders.insert(0,order) # add msg to the front of the list
		print(orders)
		return render_template("processOrder.html",orders=orders)
	else:
		return render_template("processOrder.html",orders=orders)

deliveries=[]

@app.route('/takeOrder',methods=['GET','POST'])
def takeOrder():
	global deliveries
	global orders
	if request.method == 'POST':
		userinfo = session['userinfo']
		who = userinfo['email']
		num = request.form['orderNumber']
		n = datetime.now()
		delivery={"id":num,"deliverer":who,"time":n}
		deliveries.insert(0,delivery)
		print(deliveries)
		print('orders=')
		print(orders)
		newOrders = [x for x in orders if not(int(x['id'])==int(num)) ]
		print("newOrders=")
		print(newOrders)
		orders = newOrders
		return render_template("takeOrder.html",deliveries=deliveries,orders=orders)
	else:
		print("deliveries = ")
		print(deliveries)
		return render_template("takeOrder.html",deliveries=deliveries,orders=orders)


@app.route('/removeOrder',methods=['GET','POST'])
def removeOrder():
	global deliveries
	global orders
	if request.method == 'POST':
		userinfo = session['userinfo']
		who = userinfo['email']
		num = request.form['orderNumber']
		newDeliveries = [x for x in deliveries if not(int(x['id'])==int(num)) ]
		print('deliveries=')
		print(deliveries)
		print(num)
		print(deliveries[0]['id'])
		print(deliveries[0]['id']==num)
		print(deliveries[0]['id']==int(num))
		print(int(deliveries[0]['id'])==int(num))
		print('newDeliveries=')
		print(newDeliveries)
		deliveries = newDeliveries
	return render_template("takeOrder.html",deliveries=deliveries)



if __name__ == '__main__':
<<<<<<< HEAD
    app.run('0.0.0.0',port=5000)
=======
	#app.run('0.0.0.0',port=5300) # PRODUCTION gracehopper.cs-i.brandeis.edu:5300
	app.run('0.0.0.0',port=5000) # DEVELOPMENT 127.0.0.1:5000
>>>>>>> 48f488178df67c75673e4f15e6cf7b640da2c139
