from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class AttendanceStudent(db.Model):
	__tablename__ = 'attendance_student'

	id = Column(Integer, primary_key=True)

	# 学期名称
	term_name = Column(String(256))
	# 行政班级名称
	class_name = Column(String(256))
	# 学号
	account = Column(String(256))
	# 旷课次数
	absence_times = Column(String(256))
	# 迟到次数
	come_lately_times = Column(String(256))
	# 早退次数
	leave_early_times = Column(String(256))
	# 请假次数
	ask_for_leave_times = Column(String(256))