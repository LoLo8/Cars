from __future__ import print_function # In python 2.7
from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import sys, re

app = Flask(__name__)
app.secret_key = 'SecretKey'
mysql = MySQLConnector(app,'carsdb')

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/view/<id>')
def index():

	return render_template('view.html')

@app.route('/edit/<id>')
def index():

	return render_template('edit.html')

@app.route('/delete/<id>')
def index():

	return render_template('delete.html')

@app.route('/add')
def index():

	return render_template('add.html')

@app.route('/edit_car', methods=['POST'])
def index():

	return redirect('/')

@app.route('/add_car', methods=['POST'])
def index():

	return redirect('/')

@app.route('/delete_car')
def index():

	return redirect('/')

