from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class InternshipExtramuralBase(db.Model):
	__tablename__ = 'internship_extramural_base'

	id = Column(Integer, primary_key=True)

	# 企业编号
	numbering = Column(String(2000))
	# 基地合作合同编号
	contract_numbering = Column(String(2000))
	# 基地合作合同名称
	contract_name = Column(String(2000))
	# 基地类别码
	code = Column(String(2000))
	# 单位名称
	company_name = Column(String(2000))
	# 企业行政区
	administrative_region = Column(String(2000))
	# 企业地址
	address = Column(String(2000))
	# 企业性质
	nature = Column(String(2000))
	# 法人代表
	legal_representative = Column(String(2000))
	# 企业联系人
	liaison = Column(String(2000))
	# 企业邮政编码
	postcode = Column(String(2000))
	# 企业联系电话
	telephone = Column(String(2000))