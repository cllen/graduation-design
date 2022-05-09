from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from applications import db

from sqlalchemy.orm import relationship, backref

class PlanCourse(db.Model):
	__tablename__ = 'plan_course'

	"""
		每学期开设的课程
	"""

	id = Column(Integer, primary_key=True)

	# 课程号 
	base_curriculum_id = Column(Integer, ForeignKey('base_curriculum.id'))
	base_curriculum = relationship('BaseCurriculum',
		foreign_keys=[base_curriculum_id],
		backref=backref('plan_course', lazy='dynamic'))
	# # 课程名称
	# course_name = Column(String(256))

	# 是否核心课程
	is_core = Column(Boolean)
	
	# 课程分类代码
	"""
	如：
		1. 文化基础课
		2. 专业基础课
		3. 专业课
		4. 推荐选修课
		5. 任意选修课
		6. 课程设计与实习
		7. 顶岗实习或实训
		8. 社会实践
		9. 军训
	"""
	course_classification = Column(String(256))
	
	# 课程属性码
	"""
	如：
		1. 必修
		2. 限选：由专业培养计划限定的一类选修课程，要求学生在一组（或几组）课程中（分别）选修某几门课程
		3. 任选：在专业培养计划没有规定，由学生自由选修获取学分的课程
		4. 辅修
		5. 实践
		6. 双必：为第二学位（专业）所开设的必修课
		7. 双选：为第二学位（专业）所开设的必修课
		8. 通选：一类面向全校各专业的限定选修课程，每个学生必须在这类规定的课程范围内选修几门课程，完成一定的学分 
		9. 其他：
	"""
	nature = Column(String(256))
	# 执行学期
	base_term_id = Column(Integer, ForeignKey('base_term.id'))
	base_term = relationship('BaseTerm',
		foreign_keys=[base_term_id],
		backref=backref('plan_course', lazy='dynamic'))

	def __str__(self):
		return "{},{}".format(self.base_term.name,self.base_curriculum.name)
