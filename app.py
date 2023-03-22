from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# 相当于数据存储
messages = []


@app.route('/', methods=['GET'])
def index():
    # 把消息放进去
    messages_with_timestamps = []
    for message in messages:
        message_with_timestamp = {'message': message['message'], 'timestamp': message['timestamp']}
        messages_with_timestamps.append(message_with_timestamp)
    messages_with_timestamps.reverse()

    return render_template('index.html.jinja2', messages=messages_with_timestamps)


@app.route('/post/add', methods=['POST'])
def add_message():
    message = request.form['message']
    messages.append({'message': message, 'timestamp': datetime.datetime.now()})
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)