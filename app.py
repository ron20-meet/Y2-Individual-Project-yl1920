from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from flask import *
import requests, json
from databases import *
from random import randint
from signal import signal, SIGPIPE, SIG_DFL


app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def meme():
	response = requests.get("https://api.imgflip.com/get_memes")
	parsed_content = json.loads(response.content)
	# doggo = parsed_content["message"]
	index=randint(0,90)
	results = parsed_content['data']['memes'][index]["url"]
	# print(response.content)
	meme=results
	return render_template('index.html', meme = meme)

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		all_users=query_all_users()
		username=request.form["username"]
		password=request.form["password"]
		for user in all_users:
			if (user.username==username and user.password==password):
				print("Logged In Successfully")
				return redirect(url_for('home'))
	#Check if user is valid
	return render_template('login.html')


@app.route('/sign-up',methods=['GET','POST'])
def signup():
	if request.method == 'POST':
		print('posttttttttttt')
	  	name = request.form['name']
		email = request.form['email']
		username = request.form["username"]
		password = request.form["password"]
		add_user(name , email,username ,password)
		return redirect(url_for('login'))
	return render_template("signup.html")






# meme()
 



if __name__ == '__main__':
    app.run(debug=True)

signal(SIGPIPE,SIG_DFL) 
