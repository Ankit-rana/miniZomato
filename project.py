##################################################################################
#name   : project.py
#author : ankit rana
#details: this is small flask project showing integration of mongodb with pymongo
#copyright
##################################################################################

from pymongo import MongoClient
from flask import Flask,render_template

#make a connection to the database system
connection = MongoClient('localhost',27017)
#get 'zomato' database from system
db=connection.zomato
#get collection inside database
restra=db.restaurants




#create instance of flask app
app = Flask(__name__)

@app.route('/')
@app.route('/restaurant')
def home():
	list=restra.find()
	return render_template('index.html',restra_list=list)

@app.route('/restaurant/<float:restra_name>/')
def show_items(restra_name):
	restra_info=restra.find_one({"name":restra_name})
	return render_template('details.html',restra_info=restra_info)


#check if progg is ran by the python interpretor only
if __name__=="__main__":
	app.debug=True
	app.run('0.0.0.0',8000) #application will run on all public ip of system 


