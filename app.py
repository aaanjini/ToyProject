from bs4.element import SoupStrainer
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
from bson.objectid import ObjectId

app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbsparta

#01 등록
#html

@app.route('/')
def root():
    #return "this is home"
    return render_template('music.html')


@app.route('/add')
def home():
    #return "this is home"
    return render_template('addMusic.html')


#api
@app.route('/add/music', methods=['POST'])
def write_review():
    musicUrl = request.form['musicUrl']
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    r = requests.get(musicUrl, headers=headers).text
    soup = BeautifulSoup(r, 'html.parser')

    imgUrl = soup.select('.song-main-infos .photo-zone a')[0]['href']
    name = soup.select('.song-main-infos .info-zone h2')[0].text.strip()
    artist = soup.select('.song-main-infos .info-zone ul li .value')[0].text
    doc = {
        'imgUrl':imgUrl,
        'name':name,
        'artist':artist
    }

    id = db.music.insert_one(doc).inserted_id

    return jsonify({'msg':'등록됨', 'id':str(id)})



@app.route('/add/music/<id>', methods=['GET'])
def added_music(id):

    if id == "undefined":
        music = ""
        return jsonify({'music':music, 'msg':'보여주기'})
 

    music_added = db.music.find_one({'_id':ObjectId(id)})

    artist = music_added['artist']
    url =  music_added['imgUrl']
    name = music_added['name']
 
    return jsonify({"artist":artist, 'url':url, 'name':name ,'msg':'보여주기'})




if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)