from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Hello from the home!'})



@app.route('/api/data')
def get_data():
    return jsonify({'message': 'Hello from the backend!'})

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')
    
