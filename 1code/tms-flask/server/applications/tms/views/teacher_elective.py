from ._imports_ import *

# 第三方
logger = logging.getLogger(__name__)

# 自己的库


# 业务代码
from . import bp

from ..models import (
	User as UserModel,
	TaskElective as TaskElectiveModel,
)


@bp.route('/teacher-elective',methods=('GET',), endpoint="teacher-elective")
@catch_exception
@login_required(required_user_types=[UserType.teacher])
def teacher_elective():
	page = request.args.get('page', 1, type=int)

	pagination = TaskElectiveModel.query.paginate(
		page, 
		per_page=20,
		error_out=False)
	return render_template(
		'teacher/elective.html',
		# _base.html requires data.
		current_app=current_app,
		current_user=current_user,

		items=pagination.items,
		pagination=pagination)
