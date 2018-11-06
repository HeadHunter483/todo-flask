from flask import Flask
from os import path

root_folder = path.abspath('app/')
app = Flask(__name__, root_path=root_folder)
