from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class BaseCurriculum(db.Model):
	__tablename__ = 'base_curriculum'

	# 课程号
	id = Column(Integer, primary_key=True)
	# # 课程号
	# kch = Column(String(256))

	# 课程代码
	code = Column(String(256))
	# 课程名称
	name = Column(String(256))
	# 课程英文名
	english_name = Column(String(256))
	# 课程别名
	other_name = Column(String(256))
	# 课程介绍
	introduction = Column(String(256))
	# 学分
	credits = Column(String(256))
	# 总学时
	hours = Column(String(256))
	# 理论学时
	theory_hours = Column(String(256))
	# 实践学时
	practice_hours = Column(String(256))
	# 其他学时
	other_hours = Column(String(256))
	# # 参考书目
	# textbook_id = Column(String(256))
	# # 开课单位
	# holder = Column(String(256))
	
	# 考试形式
	"""
	1. 考试
	2. 考查
	"""
	examination_form = Column(String(256))

	# 授课方式码
	"""
	1. 面授讲课
	2. 辅导
	3. 录像讲课
	4. 网络教学
	5. 实验
	6. 实习
	9. 其他
	"""
	teaching_form = Column(String(256))
	# 课程费用
	cost = Column(String(256))

	def __str__(self):
		return "{},{}".format(self.name,self.code)