
from flask import Flask,render_template,request,redirect,url_for



# Create a global variable called tasks to stor all the incoming values.
tasks = []


# App instance for the flask class.
app = Flask(__name__,template_folder='templetes') # Ensure to name the templete folder according to how you named your folder.
@app.route('/')
def home():
    # Now we render the html file to the app
    return render_template('index.html',tasks = tasks) # Name it according to how you named your html file.



# Function to enable us create new tasks.
@app.route('/add', methods = ['POST','GET'])
def create_new_task():
    task = request.form.get('task')   # This line means that we are targetting the value for the task which the user has entered. We now access the form and access to the particular field the client is going to be working with.
    tasks.append(task) # We append the data that is coming from th list.
    

    # Redirect to a particular route.
    # So we import the redirect class  from flask
    return redirect(url_for('home')) # We redirect to home because it contains our html file.
    

    
    # Method to delete
@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]

        # Now we redirect to our home
    return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(debug=True)
    