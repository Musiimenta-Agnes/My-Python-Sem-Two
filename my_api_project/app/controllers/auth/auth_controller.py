
from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_400_BAD_REQUEST,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_401_UNAUTHORIZED,HTTP_200_OK
import validators
from app.models.user_model import User
# For any errrors that arise during the registration, we ensure to roll back the database (undoing any step).
# Threrfore we import our db object from the extension file to do that.
from app.extensions import db
# We now import bcrypt that will help to hash our passwords for security
from app.extensions import bcrypt
from flask_jwt_extended import create_refresh_token, get_jwt_identity, jwt_required
from flask_jwt_extended import create_access_token


#Register the blueprint
auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


#Define the decorator
@auth.route('/register', methods = ['POST'])
def register_user():
    #Working with the request
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    contact = data.get('contact')
    image = data.get('image')
    password = data.get('password')
    user_type = data.get('user_type')  
    biography = data.get('biography','') if  user_type == 'author' else ''
    


    if not first_name or not last_name or not email or not password or not contact:
       
       return jsonify({'error':"All field are required"}),HTTP_400_BAD_REQUEST
    
    #Ensuring the password has 8 characters and above
    if len(password) < 8:
        return jsonify({'error':"Password is too short"}),HTTP_400_BAD_REQUEST
    
    if user_type == "author" and not biography:
        return jsonify({'error':"Please enter your biography"}),HTTP_400_BAD_REQUEST
    
    #Validating the email address
    if not validators.email(email):
        return jsonify({'error':"Email address is invalid"}),HTTP_400_BAD_REQUEST
    
    #Checking through  our data base to see whether the email already exists or the contact, 
    #This sends a query to the database model to check whether it matches the entered data.
    #Therefore, we import the user model to our application factory function

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error':"Email address alread exists"}),HTTP_409_CONFLICT
    
    if User.query.filter_by(contact=contact).first() is not None:
        return jsonify({'error':"Phone number already in use"}),HTTP_409_CONFLICT
    
    


    #We now work on the logic that stores a new user to the database
    #So that we can easily catch the errors that arise during the process of registering a user.

    try:
        # Encrypting the password for security, we use bcrypt , ensure to install it and import it
        hashed_password = bcrypt.generate_password_hash(password)

        #Creating the new user
        new_user = User(first_name=first_name,last_name=last_name,password=hashed_password,email=email,contact=contact,biography=biography,user_type=user_type)

        #In order to store the new user object we have to add that object to the session and then commit,
        db.session.add(new_user)
        db.session.commit()

        #User  name
        username = new_user.get_fullName()

        return jsonify({
            'message': username + "has been successfully created as" + new_user.user_type,
            'user':{
                'id':new_user.id,
                'first_name':new_user.first_name,
                'last_name':new_user.last_name,
                'email':new_user.email,
                'user_type':new_user.user_type,
                'biography':new_user.biography,
                
                


            }
        }),HTTP_201_CREATED




    except Exception as e:
        db.session.rollback()

        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR





#Login User

@auth.post('/login')
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    try:
        #Validate the data to make sure the email and password are valid.
        if not email or not password:
            return jsonify({
                'message':'Email address and password are reqired!'
            }),HTTP_400_BAD_REQUEST
        
        #Make a query to the user to ensure that the email addres entered exists in the database
        user = User.query.filter_by(email=email).first()

        # So if the user exists , we go aheaad and perform different logic to return a different response.

        if user: #Exists,
            #Ensure we check the password whether it matches the one tht was entered into the database.
            is_correct_password = bcrypt.check_password_hash(user.password,password)

            #If the password is true, we ensure we login the user and create the access token.
            if is_correct_password:
                access_token = create_access_token(identity=user.id)
                refresh_token = create_refresh_token(identity = user.id)

                return jsonify({
                    'user':{
                        'id':user.id,
                        'user_name':user.get_fullName(),
                        'email':user.email,
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }
                }),HTTP_200_OK
            
            # Incase the password is wrong
            else:
                return jsonify({
                    'message':'Invalid Paasword'
                })
            
# Incase the email doesnot exist
        else:
                return jsonify({
                    'message':"Email address is invalid!"
                }),HTTP_401_UNAUTHORIZED




# Catching errors that arise while filling in the records
    except Exception as e:
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
    




# Refreshing access token to ensure the user stays logged in even when their access token expires
    
@auth.route("token/refresh", methods = ['POST'])
@jwt_required(refresh = True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({'access_token':access_token})
    


    
# Getting all authors








    








    








    
