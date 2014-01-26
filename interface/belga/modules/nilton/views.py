

from . import *

@nilton.route('/', methods=["GET", "POST"])
def nilton_view():
    if (request.method == "POST"): print request.form
    return render_template('nilton/index.html')
