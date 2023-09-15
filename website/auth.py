from flask import Blueprint,render_template,request

auth = Blueprint('auth', __name__)

@auth.route('/login',methods = ['GET','POST'])
def login():
    
    return render_template('login.html', boolean = True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup',methods = ['GET','POST'])
def signup(): 
    if request.method == "POST":
        FirstName = request.form.get('FirstName')
        MiddleName = request.form.get('MiddleName')
        lastName = request.form.get('lastName')
        gender = request.form.get('gender')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            pass
        elif len(FirstName) < 2:
            pass
        elif len(MiddleName) < 2:
            pass
        elif len(FirstName) < 2:
            pass
        elif password != password2:
            pass
        elif len(password) < 8:
            pass
        else:
            #add user toh Database
            pass
    return render_template('signup.html')
