from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:admin@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/blog')
def bloglist():
    blog_id = request.args.get('id')
    
    if blog_id:
        blog = Blog.query.get(blog_id)
        return render_template('blog.html', blog_title = blog.title, blog_body = blog.body)
    else:
        blogs = Blog.query.all()
        return render_template('bloglist.html', title = 'Bloglist', blogs = blogs)


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
            return redirect('/blog')
        else:
            return render_template('newpost.html', title = 'New Blog Post', blog_body = blog_body,
                                blog_title = blog_title, title_error = title_error, body_error = body_error)
    
    return render_template('newpost.html', title = 'New Blog Post')


if __name__ == '__main__':
    app.run()
