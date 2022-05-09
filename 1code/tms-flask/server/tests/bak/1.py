a = {'第一节':0,'第二节':1,'第三节':2,'第四节':3,'第五节':4,'第六节':5,}

class Stock:
	def __init__(self):
		self.stock  = []
	def top(self):
		return self.stock[-1]
	def is_empty(self):
		return True if self.stock == [] else False
	def push(self,val):
		self.stock.append(val)
	def pop(self):
		if self.stock == []:
			return None
		else:
			return self.stock.pop()

	def bottom(self):
		return self.stock[0]
	def len(self):
		return len(self.stock)
	def clean(self):
		self.stock = []
	def list(self):
		return self.stock



def combine_series(series_tuple,unknown_tuple):

	finish = Stock()

	stock = Stock()

	def combine(stock,finish):
		# 如果只有一个
		if stock.len() == 1:
			finish.push(stock.top())
		# 如果有多个
		else:
			finish.push("-".join([stock.bottom(),stock.top()]))

	for index,i in enumerate(unknown_tuple):

		# 如果为空
		if stock.is_empty():
			stock.push(i)
		# 如果不为空
		else:
			print(stock.list())
			print(series_tuple.index(i)-series_tuple.index(stock.top()))
			# 如果不连续
			if series_tuple.index(i)-series_tuple.index(stock.top()) != 1:
				# 连接
				combine(stock,finish)
				# 清空
				stock.clean()
				# 入栈
				stock.push(i)
			# 如果连续，入栈
			else:
				stock.push(i)
	else:
		combine(stock,finish)

	return finish.list()




result = combine_series(
	series_tuple=('第一节','第二节','第三节','第四节','第五节','第六节',),
	unknown_tuple=(('第一节','第二节','第四节','第五节','第六节',))
)

print(result)