# 基于 Django 的智慧课程管理系统系统

## 技术栈
后端: Python 3.x, Django 4.2

数据库: MySQL 8.0 (InnoDB 引擎)

前端: HTML5, CSS3 (Backdrop-filter), JavaScript

开发工具: PyCharm, Git

## 快速开始

1. 克隆项目
```
git clone https://github.com/你的用户名/你的项目名.git
cd 你的项目名
```
2. 环境配置
建议使用虚拟环境
```
python -m venv venv
source venv/bin/activate  # Windows 使用 venv\Scripts\activate
pip install -r requirements.txt
```
3. 数据库迁移
请先在 MySQL 中创建数据库，并修改 settings.py 中的数据库配置，然后执行：
```
python manage.py makemigrations
python manage.py migrate
```
4. 运行系统
```
python manage.py runserver
```
访问 http://127.0.0.1:8000 即可预览效果。

## 预览
视频链接：https://www.bilibili.com/video/BV1xrcMznEck/?share_source=copy_web&vd_source=83481e9465cd9f75fa1a4a17e7d3e3a4

<img width="1706" height="944" alt="首页" src="https://github.com/user-attachments/assets/388b9a32-fdd7-4e98-939e-4738c5ccd164" />
<img width="1706" height="944" alt="在线课程" src="https://github.com/user-attachments/assets/933a565c-2e2c-4e7e-9364-adae72a49724" />
