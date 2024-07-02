import csv
import time
import socket
import json

# Define the UDP connection parameters, file path, and time interval
UDP_IP = "127.0.0.1"
UDP_PORT = 8000
file_path = 'filepath'
time_interval = 0.1 # Default : 0.1 seconds

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_udp_message(message):
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

def read_csv_and_send(filepath):
    with open(filepath, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        headers = csv_reader.fieldnames[1:]  # Skip the first column header (timestamp)
        
        for row in csv_reader:
            # Create a dictionary without the first column
            filtered_row = {header: row[header] for header in headers}
            message = json.dumps(filtered_row)
            send_udp_message(message)
            print(f"Sent: {message}")
            time.sleep(time_interval)  

if __name__ == "__main__": 
    read_csv_and_send(file_path)