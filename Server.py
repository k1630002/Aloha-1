from websocket_server import WebsocketServer
from APIManager import APIManager

ClientConnections = []
PORT = 9001
api = APIManager()

def new_client(client, server):
	ClientConnections.append(client)


# Called for every client disconnecting
def client_left(client, server):
	ClientConnections.remove(client)

# Called when a client sends a message
def message_received(client, server, message):
	api.registerNewClient(message)


server = WebsocketServer(PORT)

server.set_fn_new_client(new_client)

server.set_fn_client_left(client_left)

server.set_fn_message_received(message_received)

server.run_forever()
