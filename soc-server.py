import socket
import des


def server_program():
    host = 'localhost' # as both code is running on same pc
    port = 5000 
    key = 'A5FF7CA1C855FD39' # key must be same as client key

    server_socket = socket.socket() # instantiate
    server_socket.bind((host, port))  # bind host address and port together

    print(f"Server started at {host}:{port}") 

    server_socket.listen(2) # put the socket into listening mode
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    while True: # receive data stream
        data = conn.recv(1024).decode() # receive data from the client
        print('Received from client: ' + data)

        # if data is not received break
        if not data:
            break

        decrypted_msg = des.des_decrypt(data, key) # decrypt message

        print('Decrypted Message: ', decrypted_msg)
        print('\n')

        message = input('Enter message you want to send to the client: ') # take input
        encrypted_msg = des.des_encrypt(message, key) # encrypt message
        print('Encrypted Message: ', encrypted_msg)

        conn.send(encrypted_msg.encode())  # send data to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()