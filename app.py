from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

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

    return render_template('index.html', messages=messages_with_timestamps)


@app.route('/post/add', methods=['POST'])
def add_message():
    message = request.form['message']
    messages.append({'message': message, 'timestamp': datetime.datetime.now()})
    socketio.emit('new_message', {'message': message, 'timestamp': datetime.datetime.now()})
    return redirect(url_for('index'))


if __name__ == '__main__':
    socketio.run(app)