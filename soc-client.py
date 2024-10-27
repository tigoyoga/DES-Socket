import socket
import des

def client_program():
    host = 'localhost' # as both code is running on same pc
    port = 5000 
    key = 'A5FF7CA1C855FD39' # key must be same as server key

    client_socket = socket.socket() # instantiate
    client_socket.connect((host, port)) # connect to the server

    message = input("Enter message you want to encrypt: ")  # take input

    encrypted_msg = des.des_encrypt(message, key) # encrypt message
    print('Encrypted Message: ', encrypted_msg)

    while message.lower().strip() != 'bye': # until user types 'bye' keep sending messages
        client_socket.send(encrypted_msg.encode()) # send message
        data = client_socket.recv(1024).decode() # receive response
        print('Received from server: ' + data)

        decrypted_msg = des.des_decrypt(data, key) # decrypt message

        # if data is not received break
        if not data: 
            break 

        print('Decrypted Message: ', decrypted_msg)
        print('\n')

        message = input("Enter message you want to encrypt: ") # again take input
        encrypted_msg = des.des_encrypt(message, key) # encrypt message
        print('Encrypted Message: ', encrypted_msg)

    client_socket.close() # close the connection

if __name__ == '__main__':
    client_program()