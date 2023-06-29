from flask import Flask, render_template, request, make_response, Response

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/task7/', methods=['GET', 'POST'])
def task7():
    if request.method == 'POST':
        digit = request.form.get('digit')
        result = str(pow(int(digit), 2)) 
        context = {
            'digit': digit,
            'result': result,
        }
        return render_template('task7_answer.html', **context)
    return render_template('task7.html')

@app.route('/task9/', methods=['GET', 'POST'])
def task9():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        context = {
            'name': name,
            'email': email,
        }
        response = make_response(render_template('task9_answer.html', **context))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        
        return response
    return render_template('task9.html')

@app.route('/clear_cookies/')
def clear_cookies():
    response = make_response(render_template('task9.html'))
    response.set_cookie('name', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response