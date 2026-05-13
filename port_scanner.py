import socket

#get target from user
hostname = input("Enter a website to scan (e.g., google.com): ")

try:
    #convert name to IP address
    target_ip = socket.gethostbyname(hostname)
    print(f"scanning Target : {target_ip}")
    print("-" * 30)

    #the loop
    for port in range(75, 86):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # set timeout to avoid hanging
        
        result = s.connect_ex((target_ip, port))

        if result== 0:
            print (f"port {port}: OPEN")
        elif result == 111:
            print(f"port  {port}: CLOSED")
        else:
            print(f"port  {port}:  Filtered/hidden")
        s.close()
    print("-" * 30)
    print("scan complete.")
except socket.gaierror:
    print("Error: Could not resolve hostname. Check your internet or spelling.")

print ("scanning complete.")
