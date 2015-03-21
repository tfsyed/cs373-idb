from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)
app.debug = True

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/group/<name>')
def group(name=None):
    if name == 'alkali':
        return render_template('alkaliLayout.html', name=name)
    elif name =='alkaline-earth':
        return render_template('alkalinearthLayout.html', name=name)
    else:
        return "Page not found!"

# @app.route('/css/<name>')
# def sstatic(name=None):
#     return send_from_directory('css', filename=name)
#
# @app.route('/images/<name>')
# def images(name=None):
#     return send_from_directory('images', filename=name)

# @app.route('/scripts/<name>')
# def scripts(name=None):
#     return send_from_directory('scripts', filename=name)


if __name__ == '__main__':
    app.run()