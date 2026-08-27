# models.py

from db import db
from sqlalchemy import and_

class User(db.Model):

    # （设置表名）
    __tablename__ = 'user_list'

    # （设置主键）
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(255),)

    password = db.Column(db.String(255),)

# 返回一个可以用来表示对象的可打印字符串：（相当于java的toString）
    def __repr__(self):
        return '<User 用户名：%r 密码：%r>' % (self.username, self.password)# 操作数据库

# 增
def add_object(user):
    db.session.add(user)
    db.session.commit()
    print("添加 % r 完成" % user.__repr__)

# 查 （用到and的时候需要导入库from sqlalchemy import and_）
def query_object(user, query_condition_u, query_condition_p):
    result = user.query.filter(and_(user.username == query_condition_u, user.password == query_condition_p))
    print("查询 % r 完成" % user.__repr__)
    return result

# 删
def delete_object(user):
    result = user.query.filter(user.username == '11111').all()
    db.session.delete(result)
    db.session.commit()

#改
def update_object(user):
    result = user.query.filter(user.username == '111111').all()
    result.title = 'success2018'

