
from . import *


@mod.route('/')
def home():
    return render_template('dashboard/index.html')


@mod.route('/login')
def login():
    return render_template('dashboard/login.html')
