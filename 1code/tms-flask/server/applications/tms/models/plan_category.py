from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class PlanCategory(db.Model):
	__tablename__ = 'plan_category'

	id = Column(Integer, primary_key=True)

	# 课程分类码
	curriculum_classification_coding = Column(String(256))
	# 学分要求
	credit_required = Column(String(256))
	# 计划编号
	plan_numbering = Column(String(256))
