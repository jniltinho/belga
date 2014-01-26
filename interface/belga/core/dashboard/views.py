
from . import *


@mod.route('/')
def home():
    return render_template('dashboard/index.html')
