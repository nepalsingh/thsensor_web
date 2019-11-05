from flask import Flask, request, jsonify
import bcrypt, datetime, uuid
from flask_restful import Resource, Api


app = Flask(__name__)







if __name__ == "__main__":
   app.run(host='0.0.0.0',port=5180) 