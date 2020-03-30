from app import app,db,dbdir
import datetime
from user import  User

import os
#Conexion 

from flask import render_template,request, redirect, url_for, flash,session,send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
from user import  User
from sqlalchemy import update

#------------------------Listar-------------------------#
@app.route('/users')
def users():
    if 'user' in session:

        try:
            data= User.query.all()
            #get("https://jsonplaceholder.typicode.com/users").json()
            if data:
                return render_template('user/index.html', users = data)
            else:
                session.pop('user',None)
                flash('Debes registrarte primero, para ingresar','warning') 
                return render_template('auth/register.html', users = data)   
              
        except Exception as e:
            raise e

    else:
        flash('No haz iniciado sesion, por favor hacerlo.','warning') 
        return redirect(url_for('viewlogin')) 

#------------------------Crear-------------------------#
@app.route('/user/create')
def users_create():
    if 'user' in session:     
        return render_template('user/create.html')
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#------------------------Guardar-------------------------#
@app.route('/user', methods=['POST','GET'])

def user_store():  
    try:

        if  request.method=='POST':
            file  = request.files["file"] 
            name = request.form['name']
            email = request.form['email']
       
            data = User.query.filter_by(name = name).first()
            data1 = User.query.filter_by(email = email).first()

            if not(data or data1):
       
                password = generate_password_hash(request.form["password"], method="sha256")

                if not "file" in request.files:
                      
                        flash('Sin archivo', 'warning')
                        return redirect(url_for('users_create'))
                       
                if file.filename == "":    
                            
                            flash('No se pudo registar, revisa si hay ingresado el archivo. ','warning')   
                            return redirect(url_for('users_create')) 
                    
                if file and allowed_file(file.filename):    
                            
                            filename = secure_filename(file.filename)

                            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                
                            user = User(name,email,password,filename)

                            if not user:
                                flash('Error al guardar el usuario. ','danger')  
                                return redirect(url_for('users_create')) 
                            else:               
                                        
                                db.session.add(user)
                                db.session.commit()

                                flash('Se ha registrado el usuario exitosamente. ','success')               
                                return redirect(url_for('users')) 
                
            else:

                flash('No se pudo registar el email o el nombre de usuario ya esta registrado.','warning')   
                return redirect(url_for('users_create')) 
                    
    except Exception as e:
       raise e            



          

#------------------------Editar-------------------------#

@app.route('/user/edit/<int:id>', methods = ['POST', 'GET'])
def user_edit(id):
    #conn = mysql.connect()
    #cur =conn.cursor()
    if 'user' in session:
        try:
        
            data = User.query.filter_by(id=id).first()

        #conn.close()
            return render_template('user/edit.html', user = data)
        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))        

#------------------------Ver-------------------------#
@app.route('/user/show/<int:id>')
def user_show(id):
    #conn = mysql.connect()
    #cur =conn.cursor()
    if 'user' in session:
        try:
        
            data = User.query.filter_by(id=id).first()

        #conn.close()
            return render_template('user/show.html', user = data)
        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))        

@app.route('/user/update/<int:id>', methods=['POST'])
def user_update(id):

    if 'user' in session:
        try:
            if request.method == 'POST':
          
                user = User.query.filter_by(id=id).first()   
                name = request.form['name']
                email = request.form['email']
                if not(user.name == name and user.email == email):
                
                    user.name  = name
                    user.email = email

                    password= generate_password_hash(request.form["password"], method="sha256")
                    user.password =  password
                    db.session.commit()

                    flash('El usuario actualizados exitosamente','success')
                    return redirect(url_for('users'))
                
                else:
                    lash('No se pudo actualizar el email o el nombre de usuario ya esta asociado.','warning')   
                    return redirect(url_for('users_create')) 
            
        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))        
    
    
#------------------------View eliminar-------------------------#
@app.route('/user/delete_view/<int:id>', methods = ['POST','GET'])
def user_delete_view(id):
    
    if 'user' in session:
        try:
            
            user = User.query.filter_by(id=id).first()

            user.delete_on = datetime.datetime.now()
           
               #db.session.delete(user)
            db.session.commit()
            flash('El usuario se ha eliminado exitosamente','danger')
            return redirect(url_for('users')) 

        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))       

#------------------------Eliminar-------------------------#
@app.route('/user/delete/<int:id>', methods = ['POST','GET'])
def user_delete(id):
    
    if 'user' in session:
        try:
            
            user = User.query.filter_by(id=id).first()

            db.session.delete(user)
            db.session.commit()
            flash('El usuario se ha eliminado exitosamente','danger')
            return redirect(url_for('users')) 

        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))       

# users[user].delete_on = 'None' ------------------------Eliminar-------------------------#
@app.route('/users/restore', methods = ['POST','GET'])
def user_restore():
    
    if 'user' in session:
        try:
            users = User.query.all()
        
            for user in range(len(users)):
                
                users[user].delete_on = None
                db.session.commit()
        
            
            flash('Los usuarios se han restaurado exitosamente','success')
            return redirect(url_for('users',users =users)) 

        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))       
