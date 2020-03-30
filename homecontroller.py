from app import app


from flask import render_template,redirect,session,url_for,flash,g

@app.route('/home')
def home():

		if g.user:
			flash('Se ha iniciado sesion exitosamente.','success') 
			return render_template('layouts/layout.html')
		elif 'user' in session:
				flash('El usuario ya inicio sesion.','danger')
				return render_template('auth/login.html', auth= 'auth')   	
		else:
					
				        return redirect(url_for('viewlogin'))  	
