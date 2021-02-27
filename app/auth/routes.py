from flask import render_template, redirect, url_for, flash, request, jsonify, abort
from app.auth import bp
import requests


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return jsonify({'username': 'test@test.com', "firstname": "Test", "surname": "User", "status": "authenticated"})


@bp.route('/users', methods=['GET', 'POST'])
def users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data = response.json()
    return jsonify(data)