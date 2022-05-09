from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from applications import db
from sqlalchemy.orm import relationship, backref

class PlanCourseSchedulingAndBaseMajor(db.Model):
	__tablename__ = 'plan_course_scheduling_and_base_major'

	plan_course_scheduling_id = Column(Integer, ForeignKey('plan_course_scheduling.id'), primary_key=True)
	base_major_id = Column(Integer, ForeignKey('base_major.id'), primary_key=True)
