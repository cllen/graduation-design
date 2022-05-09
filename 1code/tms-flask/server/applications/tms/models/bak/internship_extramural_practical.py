from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class InternshipExtramuralPractical(db.Model):
	__tablename__ = 'internship_extramural_practical'

	id = Column(Integer, primary_key=True)

	# 受训起日期
	start_date = Column(String(2000))
	# 受训结束日期
	end_date = Column(String(2000))
	# 企业编号
	enterprise_numbering = Column(String(2000))
	# 受训岗位名称
	position_name = Column(String(2000))
	# 实训导师
	practice_supervisor_name = Column(String(2000))
	# 是否购买实习责任保险
	is_bought_insurance = Column(String(2000))
	# 保险费支付者
	insurance_payer = Column(String(2000))
	# 实习薪酬
	salary = Column(String(2000))
	# 是否是顶岗实习
	is_post_practice = Column(String(2000))
	# 学生户籍性质码
	student_household_register = Column(String(2000))