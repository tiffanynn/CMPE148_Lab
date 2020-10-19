from socket import *
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("mail.smtp2go.com", 2525)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

username = "user@sample.com"
password = "password"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
auth = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(auth)
recv_auth = clientSocket.recv(1024).decode()
print(recv_auth)
if recv1[:3] != '250':
    print('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: source@gmail.com \r\n"
clientSocket.send(mailFrom.encode())
recv_mailFrom = clientSocket.recv(1024).decode()
print("mailFrom: ")
print(recv_mailFrom)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: destination@gmail.com \r\n"
clientSocket.send(rcptTo.encode())
recv_rcptTo = clientSocket.recv(1024).decode()
print("rcptTo: ")
print(recv_rcptTo)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
data = "data \r\n"
clientSocket.send(data.encode())
recv_data = clientSocket.recv(1024).decode()
print("data: ")
print(recv_data)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send message data.
subject = "Subject: smtp lab \r\n\r\n"
clientSocket.send(subject.encode())
message = raw_input("Enter message: \r\n")
clientSocket.send(message.encode())
recv_message = clientSocket.recv(1024).decode()
print("message: ")
print(recv_message)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv_endmsg = clientSocket.recv(1024).decode()
print("endmsg: ")
print(recv_endmsg)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
recv_quit = clientSocket.recv(1024)
print (recv_quit)
clientSocket.close()