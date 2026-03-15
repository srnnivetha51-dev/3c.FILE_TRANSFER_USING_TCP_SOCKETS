import socket

port = 60001
s = socket.socket()

host = socket.gethostname()
s.bind((host, port))

s.listen(3)
print("Server is waiting for connection...")

while True:
    conn, addr = s.accept()
    print("Connected with client:", addr)

    data = conn.recv(1024)
    print("Message from client:", data.decode())

    filename = 'datafile.txt'
    f = open(filename, 'rb')

    chunk = f.read(1024)
    while chunk:
        conn.send(chunk)
        print("Sending file data...")
        chunk = f.read(1024)

    f.close()
    print("File transfer completed")

    conn.send("File sent successfully".encode())
    conn.close()