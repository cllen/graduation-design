from ._imports_ import *


@app.teardown_appcontext
def teardown(exc=None):
	if exc is None:
		