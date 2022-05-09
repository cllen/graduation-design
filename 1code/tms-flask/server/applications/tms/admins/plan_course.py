from ..utils.admin_model_view import ModelView

from ..utils.constants import CourseClassification,Nature

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class PlanCourse(LoginMixin,QueryMixin,ModelView):

	column_labels = {
		'base_term':'学期',
		'base_curriculum':'课程',
		'is_core':'是否核心课程',
		'course_classification':'课程分类',
		'nature':'课程属性',
	}

	column_list = [
		'id',
		'base_term',
		'base_curriculum',
		'is_core',
		'course_classification',
		'nature',
	]

	form_choices = {
		'course_classification': [
			(CourseClassification.cultua_basic_course, CourseClassification.cultua_basic_course),
			(CourseClassification.professional_basic_course, CourseClassification.professional_basic_course),
			(CourseClassification.professional_course, CourseClassification.professional_course),
			(CourseClassification.recommended_elective_course, CourseClassification.recommended_elective_course),
			(CourseClassification.random_elective_course, CourseClassification.random_elective_course),
			(CourseClassification.course_design_and_practice, CourseClassification.course_design_and_practice),
			(CourseClassification.taking_post_to_practice, CourseClassification.taking_post_to_practice),
			(CourseClassification.social_practice, CourseClassification.social_practice),
			(CourseClassification.military_training, CourseClassification.military_training),
		],
		'nature': [
			(Nature.required, Nature.required),
			(Nature.restricted, Nature.restricted),
			(Nature.random, Nature.random),
			(Nature.others, Nature.others),
		]
	}

	column_choices = {
		'course_classification': [
			(CourseClassification.cultua_basic_course, CourseClassification.cultua_basic_course),
			(CourseClassification.professional_basic_course, CourseClassification.professional_basic_course),
			(CourseClassification.professional_course, CourseClassification.professional_course),
			(CourseClassification.recommended_elective_course, CourseClassification.recommended_elective_course),
			(CourseClassification.random_elective_course, CourseClassification.random_elective_course),
			(CourseClassification.course_design_and_practice, CourseClassification.course_design_and_practice),
			(CourseClassification.taking_post_to_practice, CourseClassification.taking_post_to_practice),
			(CourseClassification.social_practice, CourseClassification.social_practice),
			(CourseClassification.military_training, CourseClassification.military_training),
		],
		'nature': [
			(Nature.required, Nature.required),
			(Nature.restricted, Nature.restricted),
			(Nature.random, Nature.random),
			(Nature.others, Nature.others),
		]
	}