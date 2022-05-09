from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from applications import db
from sqlalchemy.orm import relationship, backref

class PlanCourseSchedulingAndGradeClass(db.Model):
	__tablename__ = 'plan_course_scheduling_and_grade_class'

	plan_course_scheduling_id = Column(Integer, ForeignKey('plan_course_scheduling.id'), primary_key=True)
	grade_class_id = Column(Integer, ForeignKey('grade_class.id'), primary_key=True)
