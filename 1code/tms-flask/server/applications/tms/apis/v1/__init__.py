from flask import Blueprint
from flask_restx import Api
# from libs.flask_restx_marshmallow import Api
# from libs.flask_restx_patched import Api
bp = Blueprint('apis',__name__)
api = Api(bp)

from . import (
	student_elective,
	teacher_elective,
)