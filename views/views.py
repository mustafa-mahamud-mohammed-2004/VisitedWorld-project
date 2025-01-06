from flask import Blueprint, render_template, request

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/')
def main():
    '''This is the home page's route.'''
    return render_template('index.html')
