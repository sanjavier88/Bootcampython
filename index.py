from flask import redirect, render_template, request, session
from app import app
from databse import User
from databse import Contacts


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/new', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        print('hola puto')

    # email = request.form.get('email')
    # password = request.form.get('password')

    # if email and password:
    #     user = User.create_user(
    #         email, password)
    #     session['user'] = user.id

    #     return redirect('/contacts')

    return render_template('new.html')


@app.route('/contacts')
def contacts():
    # user = User.get(session['user'])
    # contacts = Contacts.select().where(Contacts.user == user)
    # # contacts = user.contactss

    return render_template('contacts/index.html', contacts=contacts)


@app.route('/contacts/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        phone = request.form.get('phone')
        cell_phone = request.form.get('cell_phone')

        if fullname and phone and cell_phone:
            user = User.get(session['user'])
            contacts = Contacts.create(
                fullname=fullname, phone=phone, cell_phone=cell_phone, user=user)
            return redirect('/contacts')

    return render_template('contacts/create.html')


@app.route('/contacts/update/<id>', methods=['GET', 'POST'])
def contacts_update(id):
    _contact = Contacts.select().where(Contacts.id == id).first()

    if request.method == 'POST':
        _contact.fullname = request.form.get('full_name')
        _contact.price = request.form.get('phone')
        _contact.save()

    return render_template('contacts/update.html', contact=_contact)


@app.route('/contacts/delete/<id>', methods=['GET'])
def contacts_delete(id):
    contact = Contacts.get(id)
    contact.session.delete(id)

    return render_template('contacts/delete.html',
                           contact=contact)


if __name__ == '__main__':
    app.run(debug=True, port=5500)
