from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class TaskWorkload(db.Model):
	__tablename__ = 'task_workload'

	id = Column(Integer, primary_key=True)

	
	# 学期名称
	term_name = Column(String(2000))
	# 教师姓名
	teacher_name = Column(String(2000))
	# 任教课程门数
	course_numbers = Column(String(2000))
	# 理论总学时
	planned_hours = Column(String(2000))
	# 实践总学时
	actual_hours = Column(String(2000))
	# 其他总学时
	other_hours = Column(String(2000))
	# 学生总数
	student_numbers = Column(String(2000))
	# 总学分数
	total_credit = Column(String(2000))