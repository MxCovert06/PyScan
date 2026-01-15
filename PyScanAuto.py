# MxCovert
import socket
# Idea block for what to implement
# 1: Common port auto scan (1-1024)
# 2: Service detection (If possible)
PortMax = 70
timeout = 0.001
def Scan(TargetHost, ScanOptions):
    for i in range(1, PortMax): # port 0 invalid
        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# In this case AF_INET is IPv4 (Address Family)
# Sock_Stream is the socket type
            connection.settimeout(timeout)
            connection.connect((TargetHost, i))
            print(f'{i} ----- TCP OPEN')
            if ScanOptions == 'Y':
                print(f"Banner for port {i}:")
                banner = connection.recv(1024).decode().strip()
                print(banner)
                pass # FIX BANNER GRABBING !!!!!!!
            else:
                connection.close()
        except socket.timeout:
            print(f'{i} ----- Closed: Timeout')
        except ConnectionRefusedError:
            print(f"{i} ----- Closed")
        finally:
            connection.close()
IP = input("Target IP: ")
str(IP)
ScanOptions = input("Grab banners? Y/N: ")

Scan(IP, ScanOptions)
# Speed up maybe?
# Add user input for speed controls, verbosity, Scan type (advanced?)