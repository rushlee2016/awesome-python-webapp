#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import User, Blog

from transwarp import db

db.create_engine(user='www-data', password='www-data', database='awesome')

#===============================================================================
# # 创建用户
# user = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
# user.insert()
# print 'new user id:', user.id
#  
# # 创建BLOG
# blog = Blog(user_id = user.id, user_name = user.name, user_image = user.image, name = 'Test Blog', summary = 'A wolf had been badly wounded by dogs. He lay sick and maimed in his lair.')
# blog.insert()
# print 'new blog id:', blog.id, 'summary:', blog.summary
#===============================================================================

user = User.find_first('where email=?', 'test@example.com')
print 'find user\'s name:', user.name
blog2 = Blog(user_id = user.id, user_name = user.name, user_image = user.image, name = 'Learn python', summary = 'A wolf had been badly wounded by dogs. He lay sick and maimed in his lair.He felt very hungry and thirsty. When a sheep passed by')
blog2.insert()

#===============================================================================
# u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
#  
# u.insert()
#  
# print 'new user id:', u.id
#  
# 
# print 'find user\'s name:', u1.name
#  
# u1.delete()
#  
# u2 = User.find_first('where email=?', 'test@example.com')
# print 'find user:', u2
#===============================================================================
