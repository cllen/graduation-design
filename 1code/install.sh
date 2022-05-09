#! /bin/bash

# 决定使用的数据库：
# supervisor只会维护production,development两个环境。
source config.conf
export TMS_CONFIG=$config_name
export OAUTH2_CONFIG=$config_name

# 安装virtualenv、创建venv、安装requirements.txt
pip3 install virtualenv			# 安装python的虚拟环境

virtualenv -p python3 oauth2-flask/venv/ 			# 创建oauth2的python虚拟环境
source oauth2-flask/venv/bin/activate	# 为oauth2的python虚拟环境安装依赖
pip3 install -r oauth2-flask/server/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
deactivate

virtualenv -p python3 tms-flask/venv/ 				# 创建tms的python虚拟环境
source tms-flask/venv/bin/activate		# 为tms的python虚拟环境安装依赖
pip3 install -r tms-flask/server/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
deactivate

# 安装supervisor、复制配置环境（注意配置里的文件夹路径要对的上！）
sudo apt-get install supervisor -y		# 安装supervisor
sudo cp oauth2-flask/server/supervisor.conf /etc/supervisor/conf.d/oauth2.conf
sudo cp tms-flask/server/supervisor.conf /etc/supervisor/conf.d/tms.conf

# 部署数据库:tms
source tms-flask/venv/bin/activate
cd tms-flask/server/
export FLASK_APP=manage.py
sudo chmod 777 ./*
flask deploy
cd ../../
deactivate
# 部署数据库:oauth2
source oauth2-flask/venv/bin/activate
cd oauth2-flask/server/
export FLASK_APP=manage.py
sudo chmod 777 ./*
flask deploy
cd ../../
deactivate


sudo supervisorctl reload
