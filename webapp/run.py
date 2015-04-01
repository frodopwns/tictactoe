from app import app, socketio
socketio.debug = True
socketio.run(app, host='0.0.0.0')