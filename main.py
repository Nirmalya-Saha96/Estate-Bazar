from EstateBazar import create_app

#ML
import numpy as np
from keras.models import load_model

#SOCKET
from flask_socketio import SocketIO
from flask_session import Session

from flask import Blueprint, render_template, request, flash, jsonify
from flask import redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit

app = create_app()
Session(app)
model_loaded = load_model('model.h5')

if __name__ == '__main__':
    socketio = SocketIO(app, manage_session=False)

    @socketio.on('join', namespace='/details')
    def join(message):
        room = session.get('room')
        join_room(room)
        print("joined")
        emit('status', {'msg':  session.get('username') + ' has entered the auction.'}, room=room)


    @socketio.on('text', namespace='/details')
    def text(message):
        room = session.get('room')
        emit('message', {'msg': session.get('username') + 'bids: ' + message['msg']}, room=room)


    @socketio.on('left', namespace='/details')
    def left(message):
        room = session.get('room')
        username = session.get('username')
        leave_room(room)
        session.clear()
        emit('status', {'msg': username + ' has left the room.'}, room=room)

    socketio.run(app, debug=True)
