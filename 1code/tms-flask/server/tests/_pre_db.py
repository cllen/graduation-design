import etc
from etc import config
from applications.tms.models import (
	Configuration as ConfigurationModel,
	BaseMajor as BaseMajorModel,
	BaseCurriculum as BaseCurriculumModel,
	BaseTerm as BaseTermModel,

	GradeGrade as GradeGradeModel,
	GradeClass as GradeClassModel,

	PlanCourse as PlanCourseModel,
	PlanTeaching as PlanTeachingModel,
	PlanCourseScheduling as PlanCourseSchedulingModel,
	PlanCourseSchedulingAndGradeClass as PlanCourseSchedulingAndGradeClassModel,
	PlanCourseSchedulingAndGradeGrade as PlanCourseSchedulingAndGradeGradeModel,
	PlanCourseSchedulingAndBaseMajor as PlanCourseSchedulingAndBaseMajorModel,
	PlanCourseScheduling as PlanCourseScheduling,

	TaskElective as TaskElectiveModel,
)

import json

# 专业
test_major_name = '测试专业名称'
test_major_code = '测试专业代码'
test_major_education_system = '五年制'
test_major_total_credit = '40'

# 课程
test_curriculum_name = '测试课程'
test_curriculum_code = '测试课程代码'
test_curriculum_credits = '3'
test_curriculum_examination_form = '考试'
test_curriculum_teaching_form = '面授讲课'

# 学期
test_term_code = '测试学期代码'
test_term_name = '测试学期'
test_term_year = '测试学年'

# 年级
test_grade_code = '测试年级代码'
test_grade_name = '测试年级名称'
test_grade_year = '测试年级年份'
test_grade_state = True

# 班级
test_class_code = '测试班级代码'
test_class_name = '测试班级名字'
test_class_plan_teaching_id = 1
test_class_current_term = '第一学期'

# 培养方案
test_plan_teaching_name = '测试培养方案名称'
test_plan_teaching_code = '测试培养方案代码'
test_plan_teaching_plan = json.dumps([
	{"课程类型":"必修","课程名":"计算机网络基础","学分":"2","第一学期":"40","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""},
	{"课程类型":"必修","课程名":"网络攻防技术","学分":"2","第一学期":"40","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""},
	{"课程类型":"必修","课程名":"网络服务配置管理","学分":"2","第一学期":"40","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""},
	{"课程类型":"必修","课程名":"计算机组装与维护","学分":"2","第一学期":"40","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""},
	{"课程类型":"选修","课程名":"Dreamweaver网页设计","学分":"1","第一学期":"40","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""},
	{"课程类型":"选修","课程名":"Access数据库应用技术","学分":"1","第一学期":"40","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""},
	{"课程类型":"选修","课程名":"python程序编写与入门","学分":"1","第一学期":"40","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""},
	{"课程类型":"选修","课程名":"网络综合布线","学分":"1","第一学期":"40","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""},
	{"课程类型":"选修","课程名":"电工基础","学分":"1","第一学期":"40","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""}
])
test_plan_teaching_credit = json.dumps([
	{"项":"学分","第一学期":"10","第二学期":"","第三学期":"","第四学期":"","第五学期":"","第六学期":"","第七学期":"","第八学期":"","第九学期":"","第十学期":""}
])

# 每学期课程
test_plan_course_curriculumid = 1
test_plan_course_termid = 1

# 排课的限制
test_plan_course_scheduling_and_base_major_planid = 1
test_plan_course_scheduling_and_base_major_classid = 1

test_plan_course_scheduling_and_grade_class_pid = 1
test_plan_course_scheduling_and_grade_class_classid = 1

test_plan_course_scheduling_and_grade_grade_pid = 1
test_plan_course_scheduling_and_grade_grade_gradeid = 1

# 排课
test_plan_course_scheduling_plancourseid = 1
test_plan_course_scheduling_termid = 1
test_plan_course_scheduling_teaching_datetimes = json.dumps(json.loads(json.dumps({"\u7b2c\u4e00\u8282": {"\u5468\u4e00": 0, "\u5468\u4e8c": 0, "\u5468\u4e09": 0, "\u5468\u56db": 0, "\u5468\u4e94": 0}, "\u7b2c\u4e8c\u8282": {"\u5468\u4e00": 0, "\u5468\u4e8c": 1, "\u5468\u4e09": 0, "\u5468\u56db": 0, "\u5468\u4e94": 0}, "\u7b2c\u4e09\u8282": {"\u5468\u4e00": 0, "\u5468\u4e8c": 1, "\u5468\u4e09": 0, "\u5468\u56db": 0, "\u5468\u4e94": 0}, "\u7b2c\u56db\u8282": {"\u5468\u4e00": 0, "\u5468\u4e8c": 0, "\u5468\u4e09": 0, "\u5468\u56db": 1, "\u5468\u4e94": 0}, "\u7b2c\u4e94\u8282": {"\u5468\u4e00": 0, "\u5468\u4e8c": 0, "\u5468\u4e09": 0, "\u5468\u56db": 1, "\u5468\u4e94": 0}, "\u7b2c\u516d\u8282": {"\u5468\u4e00": 0, "\u5468\u4e8c": 0, "\u5468\u4e09": 0, "\u5468\u56db": 0, "\u5468\u4e94": 0}})))
expected_members = 2

# 配置数据
configuration = ConfigurationModel(

	client_id=config['testing'].testing_client_id,
	client_secret=config['testing'].testing_client_secret,

	client_default_uri='{tms_domain}/tms/home'.format(tms_domain=etc.tms_domain),
	client_code2token_api='{tms_domain}/tms/code_callback'.format(tms_domain=etc.tms_domain),
	authorization_code_api='{oauth2_domain}/oauth2/authorization/authorize'.format(oauth2_domain=etc.oauth2_domain),
	code2token_api='{oauth2_domain}/oauth2/authorization/token'.format(oauth2_domain=etc.oauth2_domain),
	token2userinfo_api='{oauth2_domain}/oauth2/resource/api/v1/user'.format(oauth2_domain=etc.oauth2_domain),
	redis_db=0,
	redis_host='localhost',
	redis_port=16379,
	redis_password=None,
)

# 专业
major = BaseMajorModel(
	code=test_major_code,
	name=test_major_name,
	education_system=test_major_education_system,
	# total_credits=test_major_total_credit
)

# 课程
curriculum = BaseCurriculumModel(
	name=test_curriculum_name,
	code=test_curriculum_code,
	credits=test_curriculum_credits,
	examination_form=test_curriculum_examination_form,
	teaching_form=test_curriculum_teaching_form,
)

# 学期
term = BaseTermModel(
	name=test_term_name,
	code=test_term_code,
	year=test_term_year,
)

# 年级
grade = GradeGradeModel(
	code=test_grade_code,
	name=test_grade_name,
	year=test_grade_year,
	state=test_grade_state,
)

# 班级
_class = GradeClassModel(
	code=test_class_code,
	name=test_class_name,
	grade_id=1,
	major_id=1,
	plan_teaching_id=test_class_plan_teaching_id,
	current_term=test_class_current_term,
)

# 培养方案
plan_teaching = PlanTeachingModel(
	name=test_plan_teaching_name,
	code=test_plan_teaching_code,
	plan=test_plan_teaching_plan,
	credit=test_plan_teaching_credit
)

# 每学期课程
plan_course = PlanCourseModel(
	base_curriculum_id=test_plan_course_curriculumid,
	base_term_id=test_plan_course_termid
)

# 排课
plan_course_scheduling = PlanCourseSchedulingModel(
	plan_course_id=test_plan_course_scheduling_plancourseid,
	base_term_id=test_plan_course_scheduling_termid,
	teaching_datetimes=test_plan_course_scheduling_teaching_datetimes,
	expected_members=expected_members,
)

def pre_db(session):

	session.add(configuration)
	session.add(major)
	session.add(curriculum)
	session.add(term)
	session.add(grade)
	session.add(plan_teaching)
	session.add(_class)
	session.add(plan_course)
	session.add(plan_course_scheduling)
	session.commit()
