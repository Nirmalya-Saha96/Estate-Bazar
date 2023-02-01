from EstateBazar import create_app,db

#ML
import numpy as np
from keras.models import load_model

#SOCKET
from flask_socketio import SocketIO
from flask_session import Session

from flask import Blueprint, render_template, request, flash, jsonify
from flask import redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit

from .EstateBazar.models import Property

app = create_app()
Session(app)
model_loaded = load_model('model.h5')

data = {}

for i in range(20):
    data[str(i)] = []

if __name__ == '__main__':
    socketio = SocketIO(app, manage_session=False)



    @socketio.on('join', namespace='/details')
    def join(message):
        room = session.get('room')
        join_room(room)
        emit('status', {'msg':  session.get('username') + ' has entered the auction.'}, room=room)


    @socketio.on('text', namespace='/details')
    def text(message):
        room = session.get('room')
        propertyId = session.get('propertyId')
        userId = session.get('userId')
        obj = {}
        obj['userId'] = userId
        obj['bid'] = int(message['msg'])
        data[str(propertyId)].append(obj)
        print(data)
        emit('message', {'msg': session.get('username') + 'bids: ' + message['msg']}, room=room)


    @socketio.on('left', namespace='/details')
    def left(message):
        propertyId = message['msg']

        minValue = -1
        maxBid = -1
        userId = -1
        for element in data[str(propertyId)]:
            if element['bid']>minValue:
                maxBid = element['bid']
                userId = element['userId']
        
        propertyObj = Property.query.get(propertyId)
        propertyObj.broughtBy = userId
        propertyObj.soldPrice = maxBid
        propertyObj.isSold = True

        db.session.commit()

        for i in range(20):
            data[str(i)] = []


    socketio.run(app, debug=True)
