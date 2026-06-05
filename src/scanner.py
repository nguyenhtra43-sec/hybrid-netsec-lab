import socket

target ="192.168.26.129" 
ports = [80, 445, 3389]

print(f"Scanning target: {target}")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[*] Port {port} is OPEN")
    s.close()
