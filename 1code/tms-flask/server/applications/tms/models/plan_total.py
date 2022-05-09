from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class PlanTotal(db.Model):
	__tablename__ = 'plan_total'

	id = Column(Integer, primary_key=True)

	# 计划编号
	numbering = Column(String(256))
	# 计划年级
	grade = Column(String(256))
	# 计划专业名称
	major_name = Column(String(256))
	# 总学分要求
	total_credict_required = Column(String(256))
	# 建立年月
	found_date = Column(String(256))
	# 适用学制
	education_system_required = Column(String(256))
	# 培养目标
	training_objective = Column(String(256))
	# 是否可用
	is_enabled = Column(String(256))
	# 附件
	attachment = Column(String(256))
