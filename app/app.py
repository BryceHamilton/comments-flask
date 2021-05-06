from typing import List, Dict
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)


config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'comments'
    }


@app.route('/api/v1/comments' , methods=['GET'])
def test_comments():
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    comments = cur.execute('SELECT * FROM comments;')
    return jsonify(cur.fetchall())

@app.route('/api/v1/comments/add' , methods=['POST'])
def add_comment():
    # make sure to receive the comment to add
    comment = request.json['comment']
    authorName = request.json['authorName']
    authorEmail = request.json['authorEmail']
    date = request.json['date']
    print(comment.encode("utf-8")) #can't be printed out (gives an error) unless encoded to utf-8 
    print(authorName)
    print(authorEmail)
    print(date)
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    commentAdd = cur.execute("INSERT INTO comments(author, author_email, content, date) VALUES(%s,%s,%s,%s)", (authorName, authorEmail, comment, date))
    mysql.get_db().commit()
    comments = cur.execute('SELECT * FROM comments;')
    return  jsonify(cur.fetchall())

if __name__ == '__main__':
    app.run(host='0.0.0.0')