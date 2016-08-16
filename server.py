from __future__ import print_function # In python 2.7
from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import sys, re

app = Flask(__name__)
app.secret_key = 'SecretKey'
mysql = MySQLConnector(app,'carsdb')

@app.route('/')
def index():
	query = "SELECT * FROM cars"
	return render_template('index.html', cars=mysql.query_db(query))

@app.route('/view/<id>', methods = ['GET'])
def index():
	query = "SELECT * FROM cars WHERE id = :id LIMIT 1"
	return render_template('index.html', car=mysql.query_db(query)[0])

@app.route('/edit/<id>', methods = ['GET'])
def index():
	return render_template('edit.html', id=id)

@app.route('/delete/<id>', methods = ['GET'])
def index():
	return render_template('delete.html', id=id)

@app.route('/add', methods = ['GET'])
def index():
	return render_template('add.html')

@app.route('/add_car', methods=['POST'])
def add_car():
	data =	{	'make': request.form['make'],
				'model' request.form['model']
			}

	# Check all form fields are filled:
	for key, value in data:
		if len(value) == 0:
			flash('red')
			flash('Please fill all form fields.')
			return redirect('/add')

	# Check make/model not already in database:
	query =	"""SELECT make, model FROM cars
				WHERE make = :make
				AND model = :model
			"""	
	if len(mysql.query_db(query, data)) !=0 :
		flash('red')
		flash('{} {} already exists.'.format(data['make'], data['model']))
		return redirect('/add')

	# Valid data, add new car:
	query =	"""INSERT INTO cars (make, model, created_at, updated_at)
				VALUES (:make, :model, NOW(), NOW())
			"""	
	flash('green')
	flash('{} {} added.'.format(data['make'], data['model']))			
	mysql.query_db(query, data)

	return redirect('/')

@app.route('/edit_car/<id>', methods=['POST'])
def edit_car(id):
	data =	{	'id': id,
				'make': request.form['make'],
				'model' request.form['model']
			}

	# Check all form fields are filled:
	for key, value in data:
		if len(value) == 0:
			flash('red')
			flash('Please fill all form fields.')
			return redirect('/edit')

	# Check make/model not already in database:
	query =	"""SELECT make, model FROM cars
				WHERE make = :make
				AND model = :model
				LIMIT 1
			"""	
	car = mysql.query_db(query, data)
	# If it is, don't update:
	if len(car) == 1 :
		if car[0]['make'] == data['model'] and car[0]['model'] == data['model']
			flash('red')
			flash('Make and model hasn\'t changed. No edits made.')
			return redirect('/edit')
		else:
			flash('red')
			flash('{} {} already exists.'.format(data['make'], data['model']))
			return redirect('/edit')				

	# Valid data, edit car:
	query =	"""UPDATE cars SET make = :make, model = :model, updated_at = NOW()
				WHERE id = :id
			"""	
	mysql.query_db(query, data)			
	flash('green')
	flash('{} {} updated.'.format(data['make'], data['model']))

	return redirect('/')

@app.route('/delete_car/<id>')
def delete_car(id):
	data = {'id': id}
	query =	"DELETE FROM cars WHERE id = :id"	
	mysql.query_db(query, data)	
	flash('green')
	flash('Entry deleted.')

	return redirect('/')

