from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class InternshipInternalPractical(db.Model):
	__tablename__ = 'internship_internal_practical'

	id = Column(Integer, primary_key=True)

	# 学号
	student_id = Column(String(2000))
	# 姓名
	student_name = Column(String(2000))
	# 实习开始日期
	start_date = Column(String(2000))
	# 实习结束日期
	end_date = Column(String(2000))
	# 校内基地名称
	base_name = Column(String(2000))
	# 实习内容
	practice_content = Column(String(2000))
	# 实习岗位
	practice_position = Column(String(2000))
	# 实习导师姓名
	practice_supervisor_name = Column(String(2000))
	# 实习成绩
	practice_grade = Column(String(2000))
