from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from applications import db
from sqlalchemy.orm import relationship, backref

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class GradeClass(db.Model):
	__tablename__ = 'grade_class'

	id = Column(Integer, primary_key=True)

	# 校区代码
	campus_code = Column(String(256))
	# 专业
	major_id = Column(Integer, ForeignKey('base_major.id'))
	major = relationship('BaseMajor',
		foreign_keys=[major_id],
		backref=backref('grade_class', lazy='dynamic'))
	# 年级
	grade_id = Column(Integer, ForeignKey('grade_grade.id'))
	grade = relationship('GradeGrade',
		foreign_keys=[grade_id],
		backref=backref('grade_class', lazy='dynamic'))
	# 行政班代码
	code = Column(String(256))
	# 行政班名称
	name = Column(String(256))
	# 班主任工号
	headteacher_id = Column(Integer, ForeignKey('user.id'))
	headteacher = relationship('User',
		foreign_keys=[headteacher_id],
		backref=backref('headteacher', lazy='dynamic'))
	# 教室编号
	classroom_numbering = Column(String(256))
	# 男生人数
	male_number = Column(Integer)
	# 女生人数
	female_number = Column(Integer)
	# 总人数
	total_number = Column(Integer)
	# 班长学号
	class_monitor_id = Column(Integer, ForeignKey('user.id'))
	class_monitor = relationship('User',
		foreign_keys=[class_monitor_id],
		backref=backref('class_monitor', lazy='dynamic'))

	# # 机构号
	# insitution_id = Column(String(256))
	# 建班年月
	found_date = Column(Date)


	# 培养方案
	plan_teaching_id = Column(Integer, ForeignKey('plan_teaching.id'))
	plan_teaching = relationship('PlanTeaching',
		foreign_keys=[plan_teaching_id],
		backref=backref('class_ids', lazy='dynamic'))

	# 当前学期
	current_term = Column(String(256))

	def __str__(self):
		return "{},{}".format(self.name,self.code)

	@property
	def current_term_situation(self):
		result = self.plan_teaching.current_term_situation(self.current_term)
		logger.debug('>>>> class model')
		logger.debug(result)
		return result


