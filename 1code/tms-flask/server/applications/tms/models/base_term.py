from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class BaseTerm(db.Model):
	__tablename__ = 'base_term'

	id = Column(Integer, primary_key=True)
	# 学期码
	code = Column(String(2000))
	# 学年（度）
	year = Column(String(2000))
	# 学期名称
	name = Column(String(2000))
	# 学期开始日期
	start_date = Column(String(2000))
	# 学期结束日期
	end_date = Column(String(2000))

	def __str__(self):
		return "{},{}".format(self.name,self.code)