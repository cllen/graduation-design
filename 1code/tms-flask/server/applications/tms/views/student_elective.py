from ._imports_ import *

# 第三方
logger = logging.getLogger(__name__)

# 自己的库


# 业务代码
from . import bp

from ..models import (
	User as UserModel,
	PlanCourseScheduling as PlanCourseSchedulingModel,
	TaskElective as TaskElectiveModel,
	PlanCourseSchedulingAndGradeClass as PlanCourseSchedulingAndGradeClassModel,
)


@bp.route('/student-elective',methods=('GET',), endpoint="student-elective")
@catch_exception
@login_required(required_user_types=[UserType.student])
def student_elective():

	page = request.args.get('page', 1, type=int)

	# scheduling_ids = current_app.db.session.query(
	# 	PlanCourseSchedulingModel
	# ).join(
	# 	TaskElectiveModel
	# ).filter(
	# 	TaskElectiveModel.student_id==current_user.id
	# ).paginate( # .all()
	# 	page, 
	# 	per_page=20,
	# 	error_out=False)

	elective_ids = current_app.db.session.query(
		TaskElectiveModel
	).filter(
		TaskElectiveModel.student_id==current_user.id
	).paginate( # .all()
		page, 
		per_page=20,
		error_out=False)

	required_scheduling_ids = current_app.db.session.query(
		PlanCourseSchedulingModel
	).join(
		PlanCourseSchedulingAndGradeClassModel
	).filter(
		PlanCourseSchedulingAndGradeClassModel.grade_class_id==current_user.class_id
	).paginate( # .all()
		page, 
		per_page=20,
		error_out=False)

	# logger.debug(elective_ids)

	# 我的这个学习在修的学分
	my_this_term_credit = sum([
		int(i.plan_course.base_curriculum.credits) for i in required_scheduling_ids.items
	]+[
		int(i.plan_course_scheduling.plan_course.base_curriculum.credits) for i in elective_ids.items
	])

	if not hasattr(current_user, '_class') or not current_user._class != None:
		raise HTMLException(1301)
	# elif not hasattr(current_user._class,'current_term_situation'):
	# 	raise HTMLException(1302)
	else:
		try:
			current_term_situation=current_user._class.current_term_situation
		except:
			raise HTMLException(1303)
	


	return render_template(
		'student/elective.html',

		# _base.html requires data.
		current_app=current_app,
		current_user=current_user,

		required_scheduling_ids=required_scheduling_ids.items,
		elective_ids=elective_ids.items,
		elective_spagination=elective_ids,

		my_scheduling=current_user.my_scheduling,
		current_term_situation=current_term_situation,
		my_this_term_credit=my_this_term_credit,
		ElectiveStatus=ElectiveStatus,
		)
