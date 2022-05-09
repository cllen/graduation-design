###
# 运行统一登录系统的测试
###
# 设置环境变量
export FLASK_APP=manage.py
export OAUTH2_CONFIG=testing

# 激活虚拟环境
source /home/ubuntu/projects/graduation-design/1code/oauth2-flask/venv/bin/activate

# 进入代码文件夹
cd /home/ubuntu/projects/graduation-design/1code/oauth2-flask/server

# 暂停要被测试的服务
sudo supervisorctl stop oauth2

# 运行命令，执行测试
flask run-tests

sudo supervisorctl start oauth2

deactivate

###
# 运行教学管理系统的测试
###
# 设置环境变量
export FLASK_APP=manage.py
export TMS_CONFIG=testing

# 激活虚拟环境
source /home/ubuntu/projects/graduation-design/1code/tms-flask/venv/bin/activate

# 进入代码文件夹
cd /home/ubuntu/projects/graduation-design/1code/tms-flask/server

# 暂停要被测试的服务
sudo supervisorctl stop tms

# 运行命令，执行测试
flask run-tests

sudo supervisorctl start tms

deactivate
