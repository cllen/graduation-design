from ._imports_ import *

# 第三方
logger = logging.getLogger(__name__)

# 自己的库


# 业务代码
from . import bp

from ..models import (
	User as UserModel,
	PlanCourseScheduling as PlanCourseSchedulingModel,
)


@bp.route('/student-scheduling',methods=('GET',), endpoint="student-scheduling")
@login_required(required_user_types=[UserType.student])
def student_elective():
	logger.debug(session)
	page = request.args.get('page', 1, type=int)

	pagination = PlanCourseSchedulingModel.query.paginate(
		page, 
		per_page=8,
		error_out=False)
	return render_template(
		'student/scheduling.html',
		# _base.html requires data.
		current_app=current_app,
		current_user=current_user,

		items=pagination.items,
		pagination=pagination,
		ElectiveStatus=ElectiveStatus,)
