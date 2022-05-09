import re
import unittest
import json
import requests
from pprint import pprint

from applications import create_app

from werkzeug.urls import url_parse, Href

# from libs.werkzeug2_0_3.urls import Href

from etc import config

from applications.tms.models import (
    User as UserModel,
)

from applications.tms.utils.constants import ElectiveStatus

import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logging.getLogger("requests").setLevel(logging.INFO)

def get_url_args(url):
    parser = url_parse(url)
    args = parser.query.split('&')
    args = {arg.split('=')[0]:arg.split('=')[1] for arg in args}
    return args

class TaskElectiveTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing','testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

        self._student_login()

    def tearDown(self):
        self.app_context.pop()

    def _student_login(self):

        """test student oauh2 login"""

        try:
            # 初始化数据库时没有用户。
            user = UserModel.query.filter_by(account=config['testing'].testing_student_account).first()
        except:
            user = None

        # self.assertEqual(user,None)
        self.assertIsNone(user)

        # 获取登录参数
        # print('>> getting ',self.app.urls['login_url'])
        resp = self.client.get(self.app.urls['login_url'])
        logger.debug(resp.headers)
        payload = get_url_args(resp.location)
        payload.update({
            'account':config['testing'].testing_student_account,
            'password':config['testing'].testing_student_password,
        })

        
        # 账号密码登录
        # print('>> posting ',self.app.settings.authorization_code_api)
        resp2 = requests.post(
            self.app.settings.authorization_code_api,
            # data=json.dumps(payload),
            data=payload,
            allow_redirects=False
        )
        
        # code回调
        self.assertIsNotNone(resp2.headers.get('Location'))
        # print('>> getting ',resp2.headers['Location'])
        resp = self.client.get(
            resp2.headers['Location'],
            follow_redirects=False
        )
        self.assertEqual(resp.status_code,302)

        # 登录成功，数据库存在用户。
        user = UserModel.query.filter_by(account=config['testing'].testing_student_account).first()

        self.assertIsNotNone(user)

    def test_post_elective(self):

        """测试学生登录、选课、退课功能"""

        # logger.debug('>> posting ',self.app.urls['student_elective_api'])

        # 第一次尝试请求申请课程
        params = {'scheduling_id':1,'auditive_status':ElectiveStatus.selected,}
        resp = self.client.post(
            self.app.urls['student_elective_api'],
            # data=params,
            json=params,
        )
        print("第一次请求选课参数：",params)
        print("第一次请求选课结果：",resp.get_json())
        self.assertEqual(resp.get_json()['error_code'],1210)


        print("将测试学生添加班级：user.class_id = 1")

        user = UserModel.query.first()
        user.class_id = 1
        self.app.db.session.commit()

        # 第二次尝试请求申请课程
        resp = self.client.post(
            self.app.urls['student_elective_api'],
            json=params
        )
        print("第二次请求选课参数：",params)
        print("第二次请求选课结果：",resp.get_json())
        self.assertEqual(resp.get_json()['error_code'],0)

        

        # 退课
        href = Href(self.app.urls['student_elective_api'])

        url =  href(scheduling_id=params['scheduling_id'])

        print("第一次请求退课url：[DELETE] ",url)

        resp = self.client.delete(
           url
        )
        print("第一次请求退课结果：",resp.get_json())
        self.assertEqual(resp.get_json()['error_code'],0)


    # def test_verified_elective(self):



