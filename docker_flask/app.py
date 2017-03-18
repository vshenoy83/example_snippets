from flask import Flask
app = Flask(__name__)
@app.route('/welcome/<name>',methods=['GET'])
def hello_world(name='there'):
    return 'Hello:' + name
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
