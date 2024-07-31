from flask import Flask , make_response , jsonify
from model import db

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'HELLOOO /n Working'
@app.route('/api/products' , methods=['GET', 'POST'])
def products():
    return make_response(jsonify({"products" : db}),200)



if __name__ == '__main__':
    app.run(debug=True)


