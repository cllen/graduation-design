
# 考试形式
class ExaminationForm:
	exam = "考试"
	check = "考查"

# 授课方式
class TeachingForm:
	face2face = "面授讲课"
	guidance = "辅导"
	video = "录像讲课"
	internet = "网络教学"
	experiment = "实验"
	practice = "实习"
	others = "其他"

# 学制
class EducationSystem:
	three = "三年制"
	five = "五年制"

# 课程分类
class CourseClassification:
	cultua_basic_course = "文化基础课"
	professional_basic_course = "专业基础课"
	professional_course = "专业课"
	recommended_elective_course = "推荐选修课"
	random_elective_course = "任意选修课"
	course_design_and_practice = "课程设计与实习"
	taking_post_to_practice = "顶岗实习或实训"
	social_practice = "社会实践"
	military_training = "军训"

# 课程属性
class Nature:
	required = "必修"
	restricted = "限选"
	random = "任选"
	others = "其他"

class UserType:
	student = '学生'
	teacher = '教师'

# 学期

class Term:
	one = '第一学期'
	two = '第二学期'
	three = '第三学期'
	four = '第四学期'
	five = '第五学期'
	six = '第六学期'
	seven = '第七学期'
	eight = '第八学期'
	nine = '第九学期'
	ten = '第十学期'


class AdminAccessErrorReason:
	not_teacher = 'not teacher'
	not_logined = 'not logined'

class ElectiveStatus:
	selected = '待审核'
	rejected = '驳回'
	approved = '通过'
