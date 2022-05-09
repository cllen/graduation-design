from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class AttendanceTeacher(db.Model):
	__tablename__ = 'attendance_teacher'

	id = Column(Integer, primary_key=True)

	# 学期名称
	term_name = Column(String(256))
	# 教师姓名
	teacher_name = Column(String(256))
	# 出勤次数
	attendance_times = Column(String(256))
	# 旷课次数
	absence_times = Column(String(256))
	# 迟到次数
	come_lately_times = Column(String(256))
	# 早退次数
	leave_early_times = Column(String(256))
	# 请假次数
	ask_for_leave_times = Column(String(256))
	# 记勤次数
	record_times = Column(String(256))