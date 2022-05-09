from flask import Blueprint
bp = Blueprint('views',__name__)

from . import (
	login,
	
	student_elective,
	student_scheduling,

	teacher_elective,
)