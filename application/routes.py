from application import app, db
from flask import render_template, flash, redirect, url_for, request, Markup
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from application.forms import LoginForm, RegistrationForm, ItemForm
from application.models import User, Post
import os
import locale
locale.setlocale( locale.LC_ALL, '' )

prices = {'Glass': 0.1, 'Plastic': 0.05, 'Aluminum': 0.05}

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/dashboard')
@login_required
def dashboard():
    page = request.args.get('page', 1, type=int)
    total = 0
    for item in list(Post.query.filter(Post.user_id == current_user.id)):
        try:
            total += prices[item.material] * int(item.count)
        except:
            print("Darn")
    items = current_user.items_tracked().paginate(
        page, app.config['ITEMS_PER_PAGE'], False)
    next_url = url_for('dashboard', page=items.next_num) if items.has_next else None
    prev_url = url_for('dashboard', page=items.prev_num) if items.has_prev else None
    return render_template('dashboard.html', title='Home',
                           items=items.items, next_url=next_url,
                           prev_url=prev_url, total=locale.currency(total, grouping=True))

@app.route('/map')
@login_required
def map():
    return render_template('map.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out.')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data.strip(), email=form.email.data.strip())
        user.set_password(form.password.data.strip())
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)

@app.route('/tracking', methods=['GET', 'POST'])
@login_required
def tracking():
    form = ItemForm()
    if form.validate_on_submit():
        input_item = Post(material=form.material.data.strip(), count=form.count.data,
            value=locale.currency(prices[form.material.data.strip()] * int(form.count.data), grouping=True), author=current_user)
        db.session.add(input_item)
        db.session.commit()
        flash('You have inputted a new item to be recycled!')
        return redirect(url_for('tracking'))
    return render_template("tracking.html", title='Tracking', form=form)

@app.route('/qrscan', methods=['GET', 'POST'])
@login_required
def qrscan():
    data = request.json['data'].split(',')
    for item in data:
        stripped = str(item)[1:-1].split(' ')
        count = stripped[1]
        material = stripped[0]
        input_item = Post(material=material, count=count, value=locale.currency(prices[material] * int(count), grouping=True), author=current_user)
        db.session.add(input_item)
        db.session.commit()
    flash('You have inputted a new item to be recycled!')
    return redirect(url_for('tracking'))

@app.route('/delete_item/<item_id>', methods=['POST'])
@login_required
def delete_item(item_id):
    item = Post.query.filter_by(id=item_id).first_or_404()
    try:
        db.session.delete(item)
        db.session.commit()
        flash('You have deleted the item.')
        return redirect(url_for('dashboard'))
    except:
        flash('You have not deleted the item.')
        return redirect(url_for('dashboard'))
