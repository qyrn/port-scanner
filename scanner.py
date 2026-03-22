import socket
import threading
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host")
parser.add_argument("--start", type=int)
parser.add_argument("--end", type=int)
args = parser.parse_args()

sem = threading.Semaphore(100)

def scan(port):
    with sem:
        s = socket.socket()
        s.settimeout(0.5)
        result = s.connect_ex((args.host, port))
        if result == 0:
           try: 
               s.send(b"HEAD / HTTP/1.0\r\n\r\n")
               banner = s.recv(1024)
               print(f"Port {port} - Banner: {banner.decode('utf-8', errors='ignore').strip()}")
           except:
                print(f"Port {port} ouvert")
        s.close()   

for port in range(args.start, args.end + 1):
    t = threading.Thread(target=scan, args=(port,))
    t.start()