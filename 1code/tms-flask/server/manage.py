import os
import click
from sqlalchemy import text

from applications import create_app

from tests._pre_db import pre_db

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = create_app(os.getenv('TMS_CONFIG') or 'default')


def _depoly():
	config_name = os.getenv('TMS_CONFIG')
	
	logger.info('当前运行环境：'+config_name)

	if not app.db.engine.table_names() or config_name=='testing':

		if config_name == 'testing':
			logger.info('正在删除测试数据库...')
			app.db.drop_all()
			logger.info('正在创建数据库...')
			app.db.create_all()
			pre_db(app.db.session)

		if config_name == 'development':
			logger.info('正在创建数据库...')
			app.db.create_all()
			app.db.session.commit()
			with open('cms.sql', 'r', encoding='utf8') as f:
				for line in f.readlines():
					query = text(line)
					app.db.session.execute(query)

		app.db.session.commit()

		logger.info('创建数据库成功！')

	else:
		logger.info('数据库已存在！不再创建！')

# 运行测试程序命令
@app.cli.command('deploy')
def deploy():
	_depoly()


# 运行测试程序命令
@app.cli.command('run-tests')
@click.argument('test_names', nargs=-1)
def run_tests(test_names=None):

	"""
		初始化测试数据库
	"""
	logger.info('>>> 正在初始化数据库... <<<')

	logger.info('1/2 正在创建数据表...')

	_depoly()

	logger.info('2/2 正在插入测试数据...')

	logger.info('>>> 初始化数据库成功! <<<')
	
	logger.info('>>> 正在运行测试...	')
	

	"""
		检测代码覆盖
	"""
	COV = None
	# if os.environ.get('FLASK_COVERAGE'):
	import coverage
	COV = coverage.coverage(branch=True, include='./*')
	COV.start()

	"""
		运行测试
	"""
	import unittest
	from libs.HTMLTestRunnerCN import HTMLTestRunner

	if test_names:
		tests = unittest.TestLoader().loadTestsFromNames(test_names)
	else:
		tests = unittest.TestLoader().discover('tests')
	# unittest.TextTestRunner(verbosity=2).run(tests)

	"""
		生成测试报告
	"""
	# 测试报告的备注
	description = [
		"备注:",
		"1. 使用的数据库是测试过程中生成的数据库。",
		"2. 依赖oauth2-flask服务，所以请确保oauth2-flask服务已经在本地启动。",
	]
	try:
		import git
		repo = git.Repo(search_parent_directories=True)
		sha = repo.head.object.hexsha
	except:
		sha = None
	if sha:
		description.append("3. 当前代码版本（git-commit-id）: "+sha)

	# 生成测试报告
	with open('./tmp/教学管理系统功能测试报告.html', 'w', encoding='utf8') as f:
		runner = HTMLTestRunner(stream=f, 
			title='教学管理系统功能测试报告',
			description="\n".join(description),
			tester="黄旭辉",)

		# 运行测试
		runner.run(tests)

	"""
		生成代码覆盖报告
	"""
	if COV:
		COV.stop()
		COV.save()
		print('Coverage Summary:')
		COV.report()
		basedir = os.path.abspath(os.path.dirname(__file__))
		covdir = os.path.join(basedir, 'tmp/coverage')
		COV.html_report(directory=covdir)
		print('HTML version: file://%s/index.html' % covdir)






	

if __name__ == '__main__':
	app.run(debug=True)



