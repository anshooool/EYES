# EYES

<h1>Semester 5 Project <span style='color: red;'>EYES</span> (Surveillance Software)</h1>


<img width="1440" alt="Screenshot 2023-08-27 at 10 41 05 PM" src="https://github.com/anshooool/EYES/assets/140979513/0422501f-7919-402f-88f9-4925fa375e56">


<b>Basic slave command and control GUI</b>



<img width="776" alt="Screenshot 2023-07-31 at 1 35 24 AM" src="https://github.com/anshooool/EYES/assets/140979513/1055a56b-9c0a-4028-8a95-1108a3ebacca">



<b>Optional Login Panel </b>

<img width="512" alt="Screenshot 2023-07-31 at 1 41 10 AM" src="https://github.com/anshooool/EYES/assets/140979513/63e69276-15fe-4869-83d3-d347e324c47a">





<b>CLIENT TCP communication Module</b> (Unencrypted)

<img width="1440" alt="Screenshot 2023-08-27 at 9 53 59 PM" src="https://github.com/anshooool/EYES/assets/140979513/4287b8b4-d6fb-4773-806a-66dd34f92ea1">

The client tries to reconnect to the server recursively once the client is excuted and run as a background process

<img width="1440" alt="Screenshot 2023-08-27 at 9 54 05 PM" src="https://github.com/anshooool/EYES/assets/140979513/1348ce13-f47c-4df9-8d1e-494de05f82e1">
<img width="1440" alt="Screenshot 2023-08-27 at 9 54 20 PM" src="https://github.com/anshooool/EYES/assets/140979513/9e35d95a-e0f7-4a38-8355-abdef2b28aa3">

The client will keep running and try reconnecting even if the server is not listening or is offline

<img width="1440" alt="Screenshot 2023-08-27 at 9 54 30 PM" src="https://github.com/anshooool/EYES/assets/140979513/597f67a0-fa27-4979-a2e7-6c61db1b5887">


The client will wait for the server to be online again and reconnect even if the connection is closed by the server

<img width="1440" alt="Screenshot 2023-08-27 at 9 54 35 PM" src="https://github.com/anshooool/EYES/assets/140979513/7e0356b4-ac4e-4728-8468-a8184f294fae">


<b>SHELL MODULE</b>

whenever "RSHELL" command is recieved the client executed all the terminal commands recieved from the control server and send the console output back to the server

<img width="1440" alt="Screenshot 2023-08-27 at 10 03 41 PM" src="https://github.com/anshooool/EYES/assets/140979513/21559c40-5e14-407e-846f-7b68e76d82ca">


<b>WEBSITE BLOCK SCRIPT</b>

Script blocks sites on client after receiveing command from the control server by executing commands on the client that modify the hosts file of the system 

require elevated privileges
The hosts file (/etc/hosts) is specific to Unix-like systems. On Windows, the hosts file is located at C:\Windows\System32\drivers\etc\hosts.

<img width="1440" alt="Screenshot 2023-08-27 at 10 23 07 PM" src="https://github.com/anshooool/EYES/assets/140979513/283215f6-0f13-43ec-b114-38b442eb914f">

Site Blocked

<img width="1440" alt="Screenshot 2023-08-27 at 10 23 26 PM" src="https://github.com/anshooool/EYES/assets/140979513/58444180-d20d-4911-9c5c-5ca06ad24f2f">

<b>PYTHON SERVER TCP non GUI (Single client)</b>

<img width="602" alt="Screenshot 2023-08-31 at 1 26 42 AM" src="https://github.com/anshooool/EYES/assets/140979513/d910d2df-d893-4ee8-adc2-c90128f0c6f8">

<b>KEYLOGGER MODULE </b>

<img width="1440" alt="Screenshot 2023-08-31 at 1 53 07 AM" src="https://github.com/anshooool/EYES/assets/140979513/58de62b4-ea74-43a6-891d-1dee8a2c1be6">



<b>SCREENSHOT MODULE </b>

<img width="1440" alt="Screenshot 2023-08-31 at 1 49 28 AM" src="https://github.com/anshooool/EYES/assets/140979513/67b306cb-e2fe-488b-8152-16a5f8f677cc">

<b> Features yet to be added </b>
<ul>
  <li>Persistence</li>
  <li>Fake login prompt</li>
  <li>Video/Audio Streaming</li>
  <li>Live Desktop</li>
  <li>Apple Script/li>
    
</ul>


