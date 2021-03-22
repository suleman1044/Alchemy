from DB import db
from DB import Category, Post


db.create_all()

py = Category(name = 'Python')
px = Category(name = 'Jython')


Post(title= 'Hello Python!', body = 'Python is pretty cool', category = py)
Post(title= 'Hello Jython!', body = 'Jython is pretty cool', category = px)

db.session.add(py)
db.session.add(px)
db.session.commit()

#Category.query.filter_by(name='Jython').delete()

print(py.posts)
#x = Post.query.with_parent(px).filter(Post.title != 'Snakes').all()
#print(x)


