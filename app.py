#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:38:32 2022

@author: ben
"""

from flask import Flask, render_template, request ,redirect, send_file, flash, session, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
from flask_session import Session
import os

sess = Session()
app = Flask(__name__,static_url_path='')

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = {'xml'}

@app.route('/upload', methods=['POST'])
def upload_file():
    #try:
        #if os.path.exists("./folder/new.xml"):
        #    print("removed")
        #    os.remove("./folder/new.xml")
        f = request.files['json']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        message=" uploaded successfully"
        return f.filename+message

@app.route('/<path:path>', methods=['GET'])
def send_static(path):
    return send_from_directory('static', path)                           
                             
                             
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    sess.init_app(app)

    app.debug = True
    app.run(host='0.0.0.0',port=5001, debug=True)
