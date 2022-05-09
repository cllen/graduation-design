from locust import HttpUser, task, Locust, SequentialTaskSet

class User(HttpUser):

	@task
	def get_login(self):
		self.client.get('/tms/login')

	@task
	def post_login(self):

		account = 20203712062
		password = 123
		scheduling_id = 1 # 图像处理

		result = self.client.post(
			'http://106.55.52.190:5001/oauth2/authorization/authorize',
			{
				'account':account,
				'password':password,
				'response_type':'code',
				'scope':'snsapi_base',
				'client_id':'1',
				'redirect_uri':'http://106.55.52.190:5000/tms/code_callback',
			}
		)

	# @task
	# def post_elective(self):
		# 选课
		result = self.client.post(
			'/tms/api/v1/student-elective',
			json={
				'scheduling_id':scheduling_id,
				'auditive_status':'selected',
			}
		)

	# @task
	# def delete_elective(self):
		# 选课
		result = self.client.delete(
			'/tms/api/v1/student-elective?scheduling_id=1',
		)
