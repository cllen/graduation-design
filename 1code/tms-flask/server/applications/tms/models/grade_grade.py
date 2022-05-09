from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from applications import db
from sqlalchemy.orm import relationship, backref

class GradeGrade(db.Model):
	__tablename__ = 'grade_grade'

	id = Column(Integer, primary_key=True)

	# 年级代码（根据年份编号）
	code = Column(String(256))
	# 年级名称
	name = Column(String(256))
	# 所属年份
	year = Column(String(256))
	# 年级状态
	state = Column(Boolean)

	def __str__(self):
		return "{},{}".format(self.name,self.code)
