from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class InternshipInternalBase(db.Model):
	__tablename__ = 'internship_internal_base'

	id = Column(Integer, primary_key=True)

	
	# 校内基地名称
	name = Column(String(2000))
	# 基地地址
	address = Column(String(2000))
	# 基地邮政编码
	post = Column(String(2000))
	# 基地电话
	telephone = Column(String(2000))
	# 基地负责人
	responsible_officer = Column(String(2000))
	# 累计接纳人数
	accumulative_acceptance = Column(String(2000))