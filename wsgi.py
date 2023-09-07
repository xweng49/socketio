from flask import Flask, render_template
from flask_socketio import SocketIO, Namespace

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Namespace for the app
class AppNamespace(Namespace):
    def on_connect(self):
        print("Client connected to app namespace")

    def on_disconnect(self):
        print("Client disconnected from app namespace")

    def on_custom_event(self, data):
        print(f"{data}Hello World")


# Namespace for Socket.IO
class SocketIONamespace(Namespace):
    def on_connect(self):
        print("Client connected to Socket.IO namespace")

    def on_disconnect(self):
        print("Client disconnected from Socket.IO namespace")

    def on_custom_event(self, data):
        print("Custom event received:", data)
        self.emit('response', {'message': 'Custom event received'})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.on_namespace(AppNamespace('/camera'))  # Connect AppNamespace to '/app'
    socketio.on_namespace(SocketIONamespace('/socketio'))  # Connect SocketIONamespace to '/socketio'
    socketio.run(app, debug=True, host='localhost', port=5000)