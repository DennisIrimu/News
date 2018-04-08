from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    function to render 404 error page
    '''
    title = "Page Not Found"
    return render_template('fourOwfour.html', title=title),404
