from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class TextbookTerm(db.Model):
	__tablename__ = 'textbook_term'

	id = Column(Integer, primary_key=True)

	# 学期码
	term_code = Column(String(256))
	# 专业名称
	major_name = Column(String(256))
	# 年级代码
	grade_code = Column(String(256))
	# 课程名称
	course_name = Column(String(256))
	# 教材代码
	textbook_code = Column(String(256))
	# 选用数量
	used_numbers = Column(String(256))