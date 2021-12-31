from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# dtail 화면 보여주기
@app.route('/detail.html')
def detail():
    return render_template('detail.html')

# popup 화면 보여주기
@app.route('/popup.html')
def popup():
    return render_template('popup.html')



# API 역할을 하는 부분

#음악리스트 보여주기
@app.route('/api/list', methods=['GET'])
def show_music():
    music = list(db.mymusic.find({}, {'_id': False}).sort('like',-1))
    return jsonify({'musics': music})

#음악 좋아요
@app.route('/api/like', methods=['POST'])
def like_music():
    name_receive = request.form['name_give']

    target_music = db.mymusic.find_one({'name': name_receive})
    current_like = target_music['like']

    new_like = current_like + 1

    db.mymusic.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})


# 댓글 저장
@app.route('/comment', methods=['POST'])
def make_comment():
    nick_receive = request.form['nick_give']
    comment_receive = request.form['comment_give']

    doc = {'nick': nick_receive,
           'comment': comment_receive,
           }
    db.toy_comment.insert_one(doc)

    return jsonify({'msg': '댓글 등록 완료!'})


# 댓글 보기
@app.route('/comment', methods=['GET'])
def read_comment():
    comments = list(db.toy_comment.find({}, {'_id': False}))
    return jsonify({'all_comments': comments})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)