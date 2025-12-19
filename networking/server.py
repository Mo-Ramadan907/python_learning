import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',5543))
# s.listen(1)
# while True: 
#     client ,address = s.accept()
#     print("connected to address".format(address))
#     client.send("your are connected to the server ".encode())
#     client.close()
HOST = '127.0.0.1'
PORT = 5542

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print(f"Server listening on {HOST}:{PORT}...")
while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    conn.sendall(b"Hello from server")
    conn.close()