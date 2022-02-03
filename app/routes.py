from flask import render_template, request
from app import app
from forms import SuperForm
from utils import Utilities

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    form = SuperForm()

    if form.is_submitted() and form.data['id'] == None:
        app.logger.info(f"letterfield: {form.data['letterfield']}")
        return render_template('index.html',
                                form=form,
                                letters=form.data['letterfield'])

    if form.is_submitted and form.data['id'] == "1":
        app.logger.info(f"patternfield: {form.data['patternfield']}")

        perms = Utilities.get_permuations(form.data['letterfield'], 
                                        form.data['patternfield'])
        app.logger.info(f"returned {len(perms)} permutations.")

        return render_template("permutations.html",
                                letters = form.data['letterfield'],
                                pattern = form.data['patternfield'],
                                perms=perms)

    app.logger.info(f"index served to {request.remote_addr}")
    return render_template('index.html', form=form)


@app.route('/about')
def about():
    title = 'About Us'
    return render_template('about.html', title=title)
