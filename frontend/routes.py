from locale import currency
from urllib import response
from flask import Blueprint, blueprints, flash,render_template,session,redirect, url_for
from flask_login import current_user
from flask import request
import requests
import forms

from api.book_client import BookClient
from api.order_client import OrderClient
from api.user_api import UserClient

blueprint = Blueprint('frontend',__name__)

@blueprint.route('/',methods=['GET'])
def index():
    if current_user.is_authenticated:
        session['order'] = OrderClient.get_order_from_session()
    try:
        books = BookClient.get_books()
    except:
        books = {'result':[]}
    return render_template('index.html',books=books)

@blueprint.route('/register',methods=['GET','POST'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            
            if UserClient.user_exists(username):
                flash("Please try another username")
                return render_template('register.html',form=form)
            else:
                user = UserClient.create_user(form)
                if user:
                    flash("Registerd. Please login")
                    return redirect(url_for('frontend.login'))
        else:
            flash("Errors")

        return render_template('register.html',form=form)
@blueprint.route('/login',methods=['GET','POST'])
def login():
    form = forms.LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            api_key = UserClient.login(form)
            if api_key:
                session['user_api_key'] = api_key
                user = UserClient.get_user()
                session['user'] = user['result']
                flash('welcome back')
                return redirect(url_for('frontend.index'))
            else:
                flash('cannot Login')
        else:
            flash('cannot login')

    return render_template('login.html',form=form)

@blueprint.route('/logout',methods=['GET'])
def logout():
    session.clear()
    flash('Logged out')
    return redirect(url_for('frontend.index'))


@blueprint.route('/book/<slug>',methods=['GET','POST'])
def book_details(slug):
    response = BookClient.get_book(slug)
    book = response['result']
    form = forms.ItemForm(book_id =book['id'])
    if request.method == 'POST':
        if 'user' not in session:
            flash("please login")
            return redirect(url_for('frontend.login'))

        order= OrderClient.add_to_cart(book_id=book['id'],quantity=1)
        session['session'] = order['result']
        flash("Book added to cart")
    
    return render_template('book_info.html',book=book,form=form)