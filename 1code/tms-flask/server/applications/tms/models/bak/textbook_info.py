from sqlalchemy import Column, String, Integer, Boolean
from applications import db

class TextbookInfo(db.Model):
	__tablename__ = 'textbook_info'

	id = Column(Integer, primary_key=True)

	
	# 教材代码
	code = Column(String(256))
	# 教材名称
	name = Column(String(256))
	# 中文名称
	chinese_name = Column(String(256))
	# 出版号
	china_index_of_publishing = Column(String(256))
	# 第一作者
	first_author = Column(String(256))
	# 其他作者
	other_author = Column(String(256))
	# 版次
	edition = Column(String(256))
	# 印次
	impression = Column(String(256))
	# 价格
	price = Column(String(256))
	# 出版社
	press = Column(String(256))
	# 出版日期
	press_date = Column(String(256))
	# 是否有练习册
	is_with_workbook = Column(String(256))
	# 是否有教参教辅
	is_with_auxiliary_book = Column(String(256))
	# 内容简介
	introduction = Column(String(256))