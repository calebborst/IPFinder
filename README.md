# About:
IPFinder was a small project I've been working on that generates a random ip, scans to see if its online, grabs the hostname and saves it into a textfile for latter on.
I'm still working on it ̶and h̶o̶p̶e̶f̶u̶l̶l̶y̶ ̶i̶n̶ ̶t̶h̶e̶ ̶f̶u̶t̶u̶r̶e̶ ̶I̶ ̶w̶i̶l̶l̶ ̶h̶a̶v̶e̶ ̶a̶ ̶v̶e̶r̶t̶i̶o̶n̶ ̶f̶o̶r̶ ̶w̶i̶n̶d̶o̶w̶s̶ ̶a̶s̶ ̶o̶f̶ ̶n̶o̶w̶ ̶I̶ ̶m̶a̶d̶e̶ ̶t̶h̶i̶s̶ ̶o̶n̶ ̶l̶i̶n̶u̶x̶ ̶a̶n̶d̶ ̶d̶o̶n̶t̶ ̶t̶h̶i̶n̶k̶ ̶i̶t̶ ̶w̶i̶l̶l̶ ̶w̶o̶r̶k̶ ̶o̶n̶ ̶a̶n̶o̶t̶h̶e̶r̶ ̶O̶S̶.̶
IPFinder now has windows and linux support. (Idk about mac...)

# Usage:
Linux / Windows:
  python IPFinder.py {options}
  1. -s Saves to a text file.
  2. -bl Checks to see if the ip generated is in the blacklist.txt file. (Try keep blacklist short for optimal performance.)
  3. -hd Check the ip to see if it is from a certian type (VPN, Proxy or goverment IP).
  4. -hn Grabs the hostanme and saves it in text file.
  5. -f Makes the program as fast as it can go without breaking it.
  6. -c Only shows IP's that are online in the terminal to make it look more clean.
  7. -ct Shows where the ip is from (displays the country after the ip).
  8. -kp Only keeps ips from a certian country (enter country code only EG: US, CA, CN).

  Eg: python IPFinder.py -s -f 10 -c -ct

# What is needed to be worked on:
  - [x] Windows, Mac and Linux support. (Using a method to detect what os the user is using, this can be achieved.) 
  - [x] To be be able to use multi-threading. (Using my multi threading prosess in another one of my repos.) 
  - [ ] To be able to preform a portscan on the IP's (This can be achieved by using sockets.) 
  - [x] To have a gui instead of being run from the command line. (Either using Iron-python or tinker.) 
  - [X] Add blacklist IP's. (for line in text file if ip == line remove else keep.) 
  - [x] When using -s have the user be able to name the text file. (if -s is being used make sure the argument has a name... thing.... IDK!) 
  - [ ] Try to add a range of IP's to scan through. (122.0-5 will make a list and do -->> iprange = ['122.0', '122.1', '122.2', '122.3', '122.4', '122.5']) 
  - [x] Get the name / type of device by getting it's domain name, realm name or just its hostname. (using sockets, web requests etc. already sort of done.) 

# Notes to self:
  - [x] Add private IP types.
  - [x] Add goverment IP types.

Private IP types:
  1. 10.0. 0.0/8 IP addresses: 10.0. 0.0 – 10.255. 255.255.
  2. 172.16. 0.0/12 IP addresses: 172.16. 0.0 – 172.31. 255.255.
  3. 192.168. 0.0/16 IP addresses: 192.168. 0.0 – 192.168. 255.255.

In IPv4 an address consists of 32 bits which limits the address space to 4294967296 (232) possible unique addresses. IPv4 reserves some addresses for special purposes such as private networks (~18 million addresses) or multicast addresses (~270 million addresses).

# Disclaimer
Made for educational purposes only.
This is still work in progress and only in beta.
