from app import application

@application.route('/')
@application.route('/index')
def index():
    return "flask megatutorial with AWS - is it working ?"
