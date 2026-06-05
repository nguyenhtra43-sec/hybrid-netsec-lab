import socket
import time

target_ip = "192.168.26.129"  # IP Windows Server 
target_port = 3389            # Cổng RDP
username = "Administrator"
passwords = ["123456", "password", "admin123", "P@ssword!", "Welcome1"]

print(f"[*] Starting simulated Brute-Force attack on {target_ip}:{target_port}")
print(f"[*] Targeting user account: {username}\n")

for password in passwords:
    print(f"[!] Attempting login - User: {username} | Pass: {password}")
    try:
        # Giả lập gửi gói tin kết nối xác thực
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((target_ip, target_port))
        
        # Thao tác giả lập gửi dữ liệu xác thực lỗi
        s.sendall(b"FAKE_RDP_AUTH_PAYLOAD") 
        s.close()
    except Exception:
        pass
    
    # Giãn cách 1 giây giữa các lần thử để giả lập hành vi thực tế
    time.sleep(1)

print("\n[*] Simulation completed. Check Windows Event Viewer for Event ID 4625/4624.")
