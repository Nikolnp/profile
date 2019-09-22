from flask import Flask, render_template, redirect, json, url_for, request, abort
app= Flask(__name__)

@app.route('/home')
def index():
	return "Welcome to my website!"

@app.route('/Profile')
def profile():
	return render_template("profile.html")

@app.route('/Contacts')
def contact_form():
	return render_template("contact_form.html")

if __name__ =="__main__":
	app.run()
