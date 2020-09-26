from flask import Flask, render_template
import json 

app = Flask(__name__)


@app.route('/')
def home():
	return render_template("base.html", title = "Welcome to Marketplace!" )



@app.route('/products')
def products():
	with open ('allproducts.json', 'r') as f:
		allproducts = json.load(f)

	return render_template("products.html", allproducts = allproducts)



@app.route('/product/<product_id>')
def product_details(product_id):
	with open ('allproducts.json', 'r') as f:
		allproducts = json.load(f)

	for item in allproducts:
		if item["ProductId"] == product_id:
			product = item
   
	return render_template("productdetails.html", product = product)



app.run(debug= True)