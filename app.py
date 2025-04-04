from flask import Flask, render_template, request, url_for

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
       return render_template('index.html')
    elif request.method =="POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'cscholl' and password == 'password':
            return 'Success'
        else:
            return 'Failure'
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    return 



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)