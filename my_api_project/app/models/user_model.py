from app.extensions import db
from datetime import datetime



#Inheriting from the mdel class
class User(db.Model):

    #Customizing the table name and it shuold always be in capital

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(200), nullable = False)
    last_name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False, unique = True)
    contact = db.Column(db.String(200), nullable = False, unique = True)
    image = db.Column(db.String(255), nullable = True)
    password = db.Column(db.Text(), nullable = False)
    biography = db.Column(db.Text(), nullable = False)
    user_type = db.Column(db.String(20), nullable = False, default = "author")
    create_at = db.Column(db.DateTime,default = datetime.now() )
    updated_at = db.Column(db.DateTime,onupdate = datetime.now() )




#Define our constructor init
        
        
    def __init__(self, first_name, last_name, email, contact, password,biography, user_type,image=None ):
        
        self.first_name =first_name
        self.last_name =last_name
        self.contact = contact
        self.email =email
        self.password = password
        self.biography = biography
        self.user_type =user_type
        self.image = image 



    def get_fullName(self):
        return f"{self.last_name} {self.first_name}"   

  

    
