# 第三方库
from flask import Blueprint
import os


# 自己的库
from libs.web_utils.settings import BaseSettings

# 业务代码
from .admins import (
	Configuration as ConfigurationAdmin,
	User as UserAdmin,

	# 教学基本数据
	BaseCurriculum as BaseCurriculumAdmin,
	BaseMajor as BaseMajorAdmin,
	BaseTerm as BaseTermAdmin,

	# 年级班级数据
	GradeGrade as GradeGradeAdmin,
	GradeClass as GradeClassAdmin,

	# 教学计划
	PlanTeaching as PlanTeachingAdmin,
	PlanCourse as PlanCourseAdmin,
	PlanCourseScheduling as PlanCourseSchedulingAdmin,

	# 任务
	TaskElective as TaskElectiveAdmin,
)
from .models import (
	Configuration as ConfigurationModel,
	User as UserModel,

	# 教学基本数据
	BaseCurriculum as BaseCurriculumModel,
	BaseMajor as BaseMajorModel,
	BaseTerm as BaseTermModel,

	# 年级班级数据
	GradeGrade as GradeGradeModel,
	GradeClass as GradeClassModel,

	# 教学计划
	PlanTeaching as PlanTeachingModel,
	PlanCourse as PlanCourseModel,
	PlanCourseScheduling as PlanCourseSchedulingModel,

	# 任务
	TaskElective as TaskElectiveModel,

)

class TMS:

	def __init__(self,app=None,admin=None,db=None):

		if None not in [app,admin,db]:
			self.init_app(app,admin)

	def init_app(self,app,admin,db):


		self.app = app
		self.admin = admin
		app.tms = self

		"""
			管理后台视图
		"""
		# 系统
		admin.add_view(ConfigurationAdmin(name='设置',category="系统数据"))
		admin.add_view(UserAdmin(UserModel, db.session, name=u'用户',category="系统数据"))

		# 基础教学
		admin.add_view(BaseMajorAdmin(BaseMajorModel, db.session, name=u'专业',category="基础教学数据"))
		admin.add_view(BaseCurriculumAdmin(BaseCurriculumModel, db.session, name=u'课程',category="基础教学数据"))
		admin.add_view(BaseTermAdmin(BaseTermModel, db.session, name=u'学期',category="基础教学数据"))

		# 年级班级
		admin.add_view(GradeGradeAdmin(GradeGradeModel, db.session, name=u'年级',category="年级班级数据"))
		admin.add_view(GradeClassAdmin(GradeClassModel, db.session, name=u'班级',category="年级班级数据"))

		# 教学计划
		admin.add_view(PlanTeachingAdmin(PlanTeachingModel, db.session, name=u'培养方案',category="教学计划数据"))
		admin.add_view(PlanCourseAdmin(PlanCourseModel, db.session, name=u'每学期课程',category="教学计划数据"))
		admin.add_view(PlanCourseSchedulingAdmin(PlanCourseSchedulingModel, db.session, name=u'排课',category="教学计划数据"))

		# 教学计划
		admin.add_view(TaskElectiveAdmin(TaskElectiveModel, db.session, name=u'选课',category="任务数据"))


		# urls
		try:
			getattr(app,'urls')
		except:
			app.urls = {}
		urls = {
			'login_url':"/{}/login".format(app.config['PROJECT_NAME']),
			'logout_url':"/{}/logout".format(app.config['PROJECT_NAME']),
			'home_url':"/{}/home".format(app.config['PROJECT_NAME']),
			'student_scheduling_url':"/{}/student-scheduling".format(app.config['PROJECT_NAME']),
			'student_elective_url':"/{}/student-elective".format(app.config['PROJECT_NAME']),
			'student_elective_api':"/{}/api/v1/student-elective".format(app.config['PROJECT_NAME']),
			
			'teacher_elective_url':"/{}/teacher-elective".format(app.config['PROJECT_NAME']),
			'teacher_elective_api':"/{}/api/v1/teacher-elective".format(app.config['PROJECT_NAME']),
		}
		app.urls.update(urls)



		"""
			注册蓝图：views / api
		"""
		from .apis.v1 import bp as bp_apis
		from .views import bp as bp_views
		app.register_blueprint(
			bp_apis,
			url_prefix='/{}/api/v1'.format(
				app.config['PROJECT_NAME'],
			)
		)
		app.register_blueprint(
			bp_views,
			url_prefix='/{}'.format(
				app.config['PROJECT_NAME'],
			)
		)
