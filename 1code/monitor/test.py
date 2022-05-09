import requests
from pprint import pprint

response = requests.post(
	'http://106.55.52.190:5000/tms/api/v1/student-elective',
	json={
		'scheduling_id':1,
		'auditive_status':'selected',
	}
)

pprint(response.json())