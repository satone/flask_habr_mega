from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'satone'}
    return f'''<html><head><title>Zopa</title></head><body><h1>Hello, {user['username']}</h1></body></html>'''
