from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request


import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

doc = {
        'imgUrl':'https://image.genie.co.kr/Y/IMAGE/IMG_ALBUM/082/461/085/82461085_1640932322077_1_600x600.JPG/dims/resize/Q_80,0',
        'name':'Shadow',
        'artist':'더 맨 블랙 (THE MAN BLK)',
        'like':0
    }

id = db.mymusic.insert_one(doc).inserted_id