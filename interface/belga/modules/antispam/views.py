

from . import *

@antispam.route('/')
def home():
    return render_template('antispam/index.html')
