from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

npoint_url ="https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(npoint_url).json()
posts_objects = []

for post in posts:
    posts_obj = Post(post['title'],post['subtitle'],post['body'],post['id'])
    posts_objects.append(posts_obj)

@app.route('/')
def home():
    return render_template("index.html",all_posts = posts_objects)

@app.route('/post/<int:id>')
def get_post(id):
    request_post = None
    for blog_post in posts_objects:
        if blog_post.id == id:
            request_post = blog_post



    return render_template("post.html",post=request_post)

if __name__ == "__main__":
    app.run(debug=True)
