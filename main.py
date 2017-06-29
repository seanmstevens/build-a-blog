from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.add_template_global(len, name='len')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:admin@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))
    pubdate = db.Column(db.DateTime)

    def __init__(self, title, body, pubdate = None):
        self.title = title
        self.body = body
        if pubdate is None:
            pubdate = datetime.utcnow()
        self.pubdate = pubdate

@app.route('/blog')
def bloglist():
    blog_id = request.args.get('id')

    if blog_id:
        blog = Blog.query.get(blog_id)
        return render_template('blog.html', 
                               blog_title=blog.title, 
                               blog_body=blog.body,
                               pub_date=blog.pubdate,)
    else:
        blogs = Blog.query.order_by(Blog.pubdate.desc()).all()
        return render_template('bloglist.html', 
                               title='Bloglist', 
                               blogs=blogs,)


@app.route('/newpost', methods = ['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        blog_title = request.form['blog_title']
        blog_body = request.form['blog_body']
        title_error = body_error = ''

        if not blog_title:
            title_error = "Please add a title to your blog."

        if not blog_body:
            body_error = "Please add some content to your blog post."

        if not title_error and not body_error:
            new_blog = Blog(blog_title, blog_body)
            db.session.add(new_blog)
            db.session.commit()
            blog_id = new_blog.id
            return redirect('/blog?id={0}'.format(blog_id))
        else:
            return render_template('newpost.html', 
                                   title='New Blog Post', 
                                   blog_body=blog_body, 
                                   blog_title=blog_title, 
                                   title_error=title_error, 
                                   body_error=body_error,)

    placeholder = random.choice(["What's on your mind?", "How're you doing today?", "This message is randomly generated!"])
    return render_template('newpost.html', 
                           title='New Blog Post', 
                           placeholder=placeholder,)


if __name__ == '__main__':
    app.run()
