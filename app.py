# pip install flask
# Flask is a class in module flask
# render_template is used to get render html pages
from flask import Flask , render_template

# create an instance of Flask
app=Flask(__name__)


# this tells the app that at '/' we need to run index()
@app.route('/') #this is the decorator to the function index()
@app.route('/index') # you can add more than one routes 
def index():
    return render_template('index.html',current_title='NEW TITLE') # here you can add the required html and pass values to the html . We can use {{ }} to use passed values in the html file

@app.route('/about')
def about():
	return render_template('about.html')
if __name__=='__main__' :

    app.run(debug=True)



