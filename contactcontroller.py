
from app import app,db

from contact import  Contact

#Conexion 

from flask import render_template,request, redirect, url_for, flash,session,g

#from requests import get

#------------------------Mostrar-------------------------#
@app.route('/contacts')
def index():
    if 'user' in session:
        try:
            data= Contact.query.all()
            #get("https://jsonplaceholder.typicode.com/users").json()
            if data:
                return render_template('contact/index.html', contacts = data)
            else:

                flash('No hay datos para mostrar, por favor agregar','warning') 
                return render_template('contact/index.html', contacts = data)   
              
        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))   

#------------------------Vista crear-------------------------#
@app.route('/contact/create')
def create():
    if 'user' in session:     
        return render_template('contact/create.html')
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))        
#------------------------Guardar-------------------------#
@app.route('/contacts', methods=['POST'])
def store():   
    
    if 'user' in session:
        try:
            if  request.method=='POST':
                fullname=request.form['fullname']
                phone=request.form['phone']
                email=request.form['email']

                contact = Contact(fullname,phone,email)
                db.session.add(contact)
                db.session.commit()
                            #conn = mysql.connect()
                            #cur =conn.cursor()
                            #cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
                            #conn.commit()
                flash('Contact Added successfully')
                            #conn.close
                return redirect(url_for('index'))
            
        except Exception as e:
           raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))       
 
#------------------------Editar-------------------------#  
@app.route('/contact/edit/<int:id>', methods = ['POST', 'GET'])
def edit(id):
	#conn = mysql.connect()
	#cur =conn.cursor()
    if 'user' in session:
        try:
        
            data = Contact.query.filter_by(id=id).first()

        #conn.close()
            return render_template('contact/edit.html', contact = data)
        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))        

#------------------------Ver-------------------------#
@app.route('/contact/show/<int:id>')
def show(id):
    #conn = mysql.connect()
    #cur =conn.cursor()
    if 'user' in session:
        try:
        
            data = Contact.query.filter_by(id=id).first()

        #conn.close()
            return render_template('contact/show.html', contact = data)
        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))        
        

@app.route('/update/<int:id>', methods=['POST'])
def update_contact(id):

    if 'user' in session:
        try:
            if request.method == 'POST':
          
                contact = Contact.query.filter_by(id=id).first()   

                contact.fullname = request.form['fullname']
                contact.phone = request.form['phone']
                contact.email= request.form['email']

                db.session.commit()

                #cur.execute(""" UPDATE contacts SET fullname = %s,email = %s,  phone = %s WHERE id = %s """, (fullname, email, phone, id))
                # conn.commit()
                # conn.close() 
                flash('Contact Updated Successfully')
         
            return redirect(url_for('index'))
        except Exception as e:
            raise e
    else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))        
    
	
#------------------------Eliminar-------------------------#
@app.route('/delete/<int:id>', methods = ['POST','GET'])
def delete_contact(id):
	
    if 'user' in session:
        try:
    		
    	   contact = Contact.query.filter_by(id=id).first()
    	   db.session.delete(contact)
    	   db.session.commit()
    	   flash('Contact Removed Successfully')
    	   return redirect(url_for('index'))    

    	except Exception as e:
    		raise e
	else:
            flash('No haz iniciado sesion, por favor hacerlo.','warning') 
            return redirect(url_for('viewlogin'))     	


#conn = mysql.connect()
#cur =conn.cursor()
	
# cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
# conn.commit()
# conn.close()       

#   flash('Contact Removed Successfully')
#   return redirect(url_for('index'))    