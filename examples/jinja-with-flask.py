from flask   import Flask, render_template, send_from_directory
from hamlike import HamlikeExtension


app = Flask(__name__, template_folder='.')
app.jinja_env.add_extension(HamlikeExtension)


@app.route('/')
def index():
    return render_template('jinja-inherited.hamlike')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
