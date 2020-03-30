from app import app,db

from user import  *


from flask import render_template,request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register')
def viewregister(): 
    return render_template('auth/register.html')
        
@app.route('/register/store', methods=['POST'])
def register():

       if  request.method=='POST':
            name=request.form['name']
            email=request.form['email']
            password= generate_password_hash(request.form["password"], method="sha256")

            user = User(name,email,password)
            if user:
             
                db.session.add(user)
                db.session.commit()
                            #conn = mysql.connect()
                            #cur =conn.cursor()
                            #cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
                            #conn.commit()

                flash('Se ha registrado el usuario exitosamente. ','success')               

                return redirect(url_for('viewlogin')) 
            else:
                
                flash('No se ha podido registrar exitosamente. ','danger')  
                return redirect(url_for('viewregister'))     