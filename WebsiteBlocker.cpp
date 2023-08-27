#include <iostream>
#include <cstdlib>

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


