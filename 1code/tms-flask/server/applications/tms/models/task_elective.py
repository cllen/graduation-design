from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from applications import db
from sqlalchemy.orm import relationship, backref

class TaskElective(db.Model):
	__tablename__ = 'task_elective'

	id = Column(Integer, primary_key=True)

	# 学生
	student_id = Column(Integer, ForeignKey('user.id'))
	student = relationship('User',
		foreign_keys=[student_id],
		backref=backref('task_elective_ids', lazy='dynamic'))

	# 课程
	plan_course_scheduling_id = Column(Integer, ForeignKey('plan_course_scheduling.id'))
	plan_course_scheduling = relationship('PlanCourseScheduling',
		foreign_keys=[plan_course_scheduling_id],
		backref=backref('task_elective_ids', lazy='dynamic'))

	# 是否代选
	is_agent_selected = Column(Boolean)
	# 选课审核状态
	auditive_status = Column(String(16))
	# 选课时间
	selected_datetime = Column(DateTime)
	# 审核时间
	audited_datetime = Column(DateTime)

	# 审核人
	auditor_id = Column(Integer, ForeignKey('user.id'))
	auditor = relationship('User',
		foreign_keys=[auditor_id],
		backref=backref('task_elective_auditor', lazy='dynamic'))

	def __str__(self):
		return "{},{}".format(self.plan_course_scheduling.plan_course.base_curriculum.name,self.student.username)

