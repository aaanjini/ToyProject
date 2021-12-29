from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_music():
    music = list(db.mymusic.find({}, {'_id': False}).sort('like',-1))
    return jsonify({'musics': music })


@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']

    target_music = db.mymusic.find_one({'name': name_receive})
    current_like = target_music['like']

    new_like = current_like + 1

    db.mymusic.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)