from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class InternshipExtramuralAcceptance(db.Model):
	__tablename__ = 'internship_extramural_acceptance'

	id = Column(Integer, primary_key=True)

	
	# 企业编号
	numbering = Column(String(2000))
	# 接纳日期
	date = Column(String(2000))
	# 最大接纳实习生人数
	max_number = Column(String(2000))
	# 实际接纳实习生人数
	practical_number = Column(String(2000))
	# 实习生留基地就业人数
	stay_number = Column(String(2000))
	# 实习生待遇
	treatment = Column(String(2000))