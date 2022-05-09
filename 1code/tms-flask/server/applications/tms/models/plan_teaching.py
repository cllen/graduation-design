from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text
from applications import db

from sqlalchemy.orm import relationship, backref

import json

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PlanTeaching(db.Model):
	__tablename__ = 'plan_teaching'

	"""
		总体教学计划、或者叫人才培养方案，限定到：专业、学制、年级，每个班只有一份培养方案。
	"""

	id = Column(Integer, primary_key=True)

	# 培养方案名称
	name = Column(String(256))

	# 培养方案代码
	code = Column(String(256))

	# 专业
	major_id = Column(Integer, ForeignKey('base_major.id'))
	major = relationship('BaseMajor',
		foreign_keys=[major_id],
		backref=backref('plan_teaching', lazy='dynamic'))

	# 学制
	education_system = Column(String(256))

	# 招生对象
	prospective_student = Column(String(256))

	# 领域方向
	fields = Column(String(1080))

	# 职业岗位
	professions = Column(String(1080))

	# 培养方案内容
	content = Column(Text(108000))

	# 教学计划(json)
	plan = Column(Text(108000))

	# 学分
	credit = Column(Text(108000))

	def __str__(self):
		return "{},{}".format(self.name,self.code)


	def current_term_situation(self,term):

		from operator import itemgetter
		from itertools import groupby

		logger.debug('>> plan_teachuing.model')
		logger.debug(json.loads(self.credit)[0])
		logger.debug(term)
		required_credit = json.loads(self.credit)[0][term]

		plan_json = json.loads(self.plan)

		commend_course_ids = [course for course in plan_json if course[term] != ""]

		commend_course_ids.sort(key=itemgetter('课程类型')) #需要先排序，然后才能groupby。lst排序后自身被改变
		groupby_commend_course_ids = groupby(commend_course_ids,itemgetter('课程类型')) 

		return {
			'required_credit':int(required_credit),
			'commend_course_ids':groupby_commend_course_ids,
		}



