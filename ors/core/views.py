from ors.core import bp
from flask import render_template, redirect, url_for, flash, request
from ors.core.forms import FreeQuoteForm, FullContactForm


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')


@bp.route('/about')
def about():
    return render_template('about.html', title='About')


@bp.route('/crates')
def crates():
    return render_template('crates.html', title='Crates')


@bp.route('/move-management')
def move_management():
    return render_template('move-management.html', title='Management')


@bp.route('/IT', methods=['GET', 'POST'])
def reloc_it():
    form = FreeQuoteForm()
    if form.validate_on_submit():
        flash("ORS is no longer in business")
        return redirect(url_for('core.reloc_it'))

    return render_template('relocation-IT.html', title='IT', dd=True, form=form)


@bp.route('/library', methods=['GET', 'POST'])
def library():
    form = FreeQuoteForm()
    if form.validate_on_submit():
        flash("ORS is no longer in business")
        return redirect(url_for('core.library'))

    return render_template('relocation-library.html', title='Library',
                            form=form, dd=True)


@bp.route('/office', methods=['GET', 'POST'])
def office():
    form = FreeQuoteForm()
    if form.validate_on_submit():
        flash("ORS is no longer in business")
        return redirect(url_for('core.office'))

    return render_template('relocation-office.html', title='Office',
                            form=form, dd=True)


@bp.route('/warehouse', methods=['GET', 'POST'])
def warehouse():
    form = FreeQuoteForm()
    if form.validate_on_submit():
        flash("ORS is no longer in business")
        return redirect(url_for('core.warehouse'))

    return render_template('relocation-warehouse.html', title='Warehouse',
                            form=form, dd=True)


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = FullContactForm()
    if form.validate_on_submit():
        flash("ORS is no longer in business")
        return redirect(url_for('core.contact'))

    return render_template('contact.html', title='Contact', form=form)
