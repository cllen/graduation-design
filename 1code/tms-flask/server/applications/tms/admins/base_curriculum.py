from ..utils.admin_model_view import ModelView

from ..utils.constants import ExaminationForm,TeachingForm

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class BaseCurriculum(LoginMixin,QueryMixin,ModelView):

	column_labels = {
		'code':'课程代码',
		'name':'课程名称',
		'english_name':'课程英文名',
		'other_name':'课程别名',
		'introduction':'课程介绍',
		'credits':'学分',
		'hours':'总学时',
		'theory_hours':'理论学时',
		'practice_hours':'实践学时',
		'other_hours':'其他学时',
		'examination_form':'考试形式',
		'teaching_form':'授课方式',
		'cost':'课程费用',
	}

	column_list = [
		'id',
		'code',
		'name',
		'credits',
		'hours',
		'examination_form',
		'teaching_form',
		'cost',
	]

	form_choices = {
		'examination_form': [
			(ExaminationForm.exam, ExaminationForm.exam),
			(ExaminationForm.check, ExaminationForm.check),
		],
		'teaching_form': [
			(TeachingForm.face2face, TeachingForm.face2face),
			(TeachingForm.guidance, TeachingForm.guidance),
			(TeachingForm.video, TeachingForm.video),
			(TeachingForm.internet, TeachingForm.internet),
			(TeachingForm.experiment, TeachingForm.experiment),
			(TeachingForm.practice, TeachingForm.practice),
			(TeachingForm.others, TeachingForm.others),
		]
	}

	column_choices = {
		'examination_form': [
			(ExaminationForm.exam, ExaminationForm.exam),
			(ExaminationForm.check, ExaminationForm.check),
		],
		'teaching_form': [
			(TeachingForm.face2face, TeachingForm.face2face),
			(TeachingForm.guidance, TeachingForm.face2face),
			(TeachingForm.video, TeachingForm.video),
			(TeachingForm.internet, TeachingForm.internet),
			(TeachingForm.experiment, TeachingForm.experiment),
			(TeachingForm.practice, TeachingForm.practice),
			(TeachingForm.others, TeachingForm.others),
		]
	}