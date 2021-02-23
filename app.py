#Flask app for OPCDA

_author_ = 'Shaik Saleem'
_version_ = '1.0'

#import liraries
from flask import *
import json
from Models import opcda


app = Flask(__name__)

@app.route("/read", methods =['GET'])
def read():
    return json.dumps(opcda.Read_tags(request.json).__dict__)


@app.route("/write", methods =['POST'])
def write():
    return json.dumps(opcda.Write_SingleTag(request.json).__dict__)

@app.route("/writemultiple", methods =['POST'])
def writemultiple():
    return json.dumps(opcda.Write_MultipleTag(request.json).__dict__)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=85,debug = True)
