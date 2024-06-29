from app import app

@app.route('/')
def home():
    return "Nigga what"
@app.route('/index')
def index():
    return "Hello World!"
