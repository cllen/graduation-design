from .configuration import Configuration
from .user import User

# 教学基本数据
from .base_curriculum import BaseCurriculum
from .base_major import BaseMajor
from .base_term import BaseTerm

# 年级班级数据
from .grade_class import GradeClass
from .grade_grade import GradeGrade

# 教学计划
from .plan_teaching import PlanTeaching
from .plan_course import PlanCourse
from .plan_course_scheduling import PlanCourseScheduling
from .plan_course_scheduling_and_base_major import PlanCourseSchedulingAndBaseMajor
from .plan_course_scheduling_and_grade_grade import PlanCourseSchedulingAndGradeGrade
from .plan_course_scheduling_and_grade_class import PlanCourseSchedulingAndGradeClass

# 任务
from .task_elective import TaskElective
