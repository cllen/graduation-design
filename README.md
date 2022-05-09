# 简介

这是毕业设计，有两个子系统组成。

1. 统一登录系统：根据`Oauth2.0`标准、基于`python3.8`、`Flask`开发的认证授权服务端。
2. 教学管理系统：根据《GBT 36342-2018 智慧校园总体框架》、《JYT 1005-2012教育管理信息 中职学校管理信息》、`Oauth2.0`标准（客户端）、`MySQL8.0`数据库所实现。

# 使用的技术

1. Python3.8
2. MySQL8.0
3. Flask
4. Jinja2
5. Flask_admin
6. SQLAlchemy

# 实现的功能

1. 统一身份认证登录（Oauth2）。
2. 专业管理、课程管理。
3. 年级管理、班级管理。
4. 培养方案管理、排课管理、选课管理。

# 文档

1. [1.运维文档（安装、测试）](./0docs/1.运维文档（安装、测试）.md)
2. [2.用户文档（业务使用教程）](./0docs/2.用户文档（业务使用教程）.md)
3. [3.开发者文档1（接口文档）](./0docs/3.开发者文档1（接口文档）.md)
4. [4.开发者文档2（代码结构、二次开发）](./0docs/4.开发者文档2（代码结构、二次开发）.md)
5. [5.架构文档](./0docs/5.架构文档.md)

# 更新

更新是针对`git`的`tag`的说明。

最新稳定版本：`v2.3`。

毕业设计使用的版本：`v2.3`。

1. [x] 2022年4月10日 / `v2.1` / 完成安装、卸载、功能测试、性能测试、文档优化。
2. [x] 2022年4月13日 / `v2.2` / 陈锡成功通过运维文档的安装、成功通过学生角色的用户测试。
3. [x] 2022年4月16日 / `v2.3` / 修改graduation路径。

# 测试日志

1. [x] 2022年4月12日 / 新元 / 测试安装时候，安装失败，因为install.sh脚本有问题。
2. [x] 2022年4月12日 / 陈锡 / 测试安装时候，不知道`1code`是什么。
3. [x] 2022年4月13日 / 陈锡 / 测试安装时候，安装成功，版本为`v2.2`，但是没有注意到配置文件的修改。
