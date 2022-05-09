from ... import BaseMiniOrm

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MiniOrm(BaseMiniOrm):

	def __init__(self,db=None,**kwargs):
		if db:
			self.db = db

	def __call__(self,Model):
		self.Model = Model
		return self

	def get(self,**kwargs):
		# logger.info(kwargs)
		return self.Model.query.filter_by(**kwargs).all()

	def save(self, dont_commit=False, **kwargs):
		instance = self.Model(**kwargs)
		self.db.session.add(instance)
		if dont_commit == False:
			self.db.session.commit()
		return instance

	def update(self,instance, dont_commit=False, **kwargs):
		for key,value in kwargs.items():
			setattr(instance,key,value)
		if dont_commit == False:
			self.db.session.commit()
		return instance

	def delete(self,instance, dont_commit=False):
		self.db.session.delete(instance)
		if dont_commit == False:
			self.db.session.commit()

	def first(self):
		return self.db.session.query(self.Model).first()