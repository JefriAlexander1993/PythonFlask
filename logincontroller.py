from app import app,db
from werkzeug.security import generate_password_hash, check_password_hash

from user import  *


from flask import render_template,request, redirect, url_for, flash,session,g


@app.before_request
def before_request():
	if 'user' in session:
		g.user = session['user']
	else:
		g.user = None	

@app.route('/login')
def viewlogin():

	if 'user' in session:
		return render_template('auth/login.html',auth='auth')
	else:	
		return render_template('auth/login.html')
@app.route('/login', methods=['POST'])
def veficary():
	if request.method == 'POST':

		if 'user' in session:
			flash('El usuario ya inicio sesion.','danger')
			return render_template('auth/login.html', auth= 'auth')

		else:
			email= request.form['email']
			password= request.form['password']

			user = User.query.filter_by(email=email).first()

		    	if user and check_password_hash(user.password, password):
		       	    session['user'] = user.name

		            return redirect(url_for('home'))
		        else:
		            flash('El usuario no conside con los registrados.','danger')
		            return redirect(url_for('viewlogin'))  	            	
@app.route('/logout')
def logout():
	session.pop('user',None)
	return redirect(url_for('viewlogin'))  	