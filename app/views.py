"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, send_from_directory
from .forms import NewPropertyForm
from app.models import PropertyProfile, db
from werkzeug.utils import secure_filename
import os

###
# Routing for your application.
###ß

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Properties")

@app.route('/properties/create', methods=["GET", "POST"])
def newproperty():

    form=NewPropertyForm()
    if request.method=='POST' and form.validate_on_submit():
        title = request.form['title']
        numofbedrooms = request.form['numofbedrooms']
        numofbathrooms = request.form['numofbathrooms']
        location = request.form['location']
        price = request.form['price']
        ptype = request.form['ptype']
        description = request.form['description']
        photo = save_photos(form.photo.data) 
        prop = PropertyProfile(title, description, numofbedrooms, numofbathrooms, price, ptype, location, photo)
        db.session.add(prop)
        db.session.commit()
        return redirect(url_for('listproperties'))
    return render_template('newproperty.html', form=form)

@app.route('/properties', methods=["GET"])
def listproperties():
    properties=db.session.query(PropertyProfile).all()
    return render_template('listproperties.html', properties=properties)

@app.route('/properties/<propertyid>', methods=["GET"])
def showproperty(propertyid):
    property = db.session.query(PropertyProfile).filter(PropertyProfile.id == propertyid).first()
    return render_template('showpropertyid.html', property=property)

def save_photos(photo):
    filename = secure_filename(photo.filename)
    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename

@app.route('/get_image/<filename>')
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
