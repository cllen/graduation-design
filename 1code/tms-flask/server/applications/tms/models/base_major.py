from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class BaseMajor(db.Model):
	__tablename__ = 'base_major'

	id = Column(Integer, primary_key=True)

	# # 专业编号
	# numbering = Column(String(256))

	# 专业代码
	code = Column(String(256))
	# 专业名称
	name = Column(String(256))
	# 专业英文名称
	english_name = Column(String(256))
	# 专业简称
	short_name = Column(String(256))
	# 学制
	"""
	1. 三年制
	2. 五年制
	"""
	education_system = Column(String(256))
	# 专业方向名称
	direction = Column(String(256))
	# 建立年月
	found_date = Column(String(256))
	# 专业教师数
	teacher_ids = Column(String(256))
	# # 开设机构号
	# insitution_numbering = Column(String(256))
	# 总学分
	# total_credict = Column(String(256))

	def __str__(self):
		return "{},{}".format(self.name,self.code)