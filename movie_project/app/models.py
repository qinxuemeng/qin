from datetime import datetime
from app import db
#会员
class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer,primary_key=True)#编号
    name = db.Column(db.String(100),unique=True)#昵称
    pwd = db.Column(db.String(100))#密码
    email = db.Column(db.String(100),unique=True)#邮箱
    phone = db.Column(db.String(11),unique=True)#手机号
    info = db.Column(db.Text)#个性简介
    face = db.Column(db.String(255),unique=True)#头像
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)#注册时间
    uuid = db.Column(db.String(255),unique=True)#唯一标志符
    userlogs = db.relationship("Userlog",backref='user')#会员日志外键关系关联

    def __repr__(self):
        return "<User %r>"%self.name
#会员日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer,primary_key=True)#编号
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))#所属会员
    ip = db.Column(db.String(100))#登录ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#登录时间
    def __repr__(self):
        return "<Userlog %r>"%self.id
#标签
class Tag(db.Model):
    __tablename__ = "tag"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100),unique=True)#标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    movies = db.relationship("Movie",backref="tag")#电影外间关系关联
    def __repr__(self):
        return "<Tag %r>" % self.name
#电影
class Movie(db.Model):
    __tablename__ = "movie"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)#标题
    url = db.Column(db.String(255),unique=True)#地址
    info = db.Column(db.Text)#简介
    logo = db.Column(db.String(255), unique=True)#logo
    star = db.Column(db.SmallInteger)#星级
    playnum = db.Column(db.BigInteger)#播放量
    conmentnum = db.Column(db.BigInteger)#评论量
    tag_id = db.Column(db.Integer,db.ForeignKey("tag.id"))#所属标签
    area = db.Column(db.String(255))#上映地区
    release_time = db.Column(db.Date)#上映时间
    length = db.Column(db.String(100))#播放时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#添加时间
    def __repr__(self):
        return "<Movie %r>" % self.title
#上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    logo = db.Column(db.String(255), unique=True)  # logo
    addtime = db.Column(db.DateTime, index=True, default=datetime.now) # 添加时间

    def __repr__(self):
        return "<Preview %r>" % self.title
#评论
class Comment(db.Model):
    __tablename__="comment"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<comment %r>" % self.id

#电影的收藏

class Moviecol(db.Model):
    __tablename__="moviecol"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Moviecol %r>" % self.id
#角色
class Role(db.Model):
    __tablename__="role"
    __table_args__ = {"useexisting": True}
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    auths=db.Column(db.String(600))
    addtime=db.Column(db.DateTime, index=True, default=datetime.now)
    admins=db.relationship("Admin",backref='role')

    def __repr__(self):
        return "<Role %r>" % self.name
#管理员
class Admin(db.Model):
    __tablename__ = "admin"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super=db.Column(db.SmallInteger)
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))#所属角色
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    adminlog=db.relationship("Adminlog",backref='admin') #管理员外键关联
    Oplogs = db.relationship("Oplog", backref='admin')
    def __repr__(self):
        return "<Admin %r>" % self.name
    def check_pwd(self,pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd,pwd)

#管理员日志
class Adminlog(db.Model):
    __tablename__="adminlog"
    __table_args__ = {"useexisting": True}
    id=db.Column(db.Integer,primary_key=True) #编号
    admin_id=db.Column(db.Integer,db.ForeignKey('admin.id'))
    ip=db.Column(db.String(100))
    #登录ip.
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<adminlog %r>" % self.id

#操作日志
class Oplog(db.Model):
    __tablename__="oplog"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id=db.Column(db.Integer,db.ForeignKey('admin.id'))
    ip=db.Column(db.String(100))
    #登录ip
    reason=db.Column(db.String(600))
    #操作原因
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)
#if __name__ == '__main__':





