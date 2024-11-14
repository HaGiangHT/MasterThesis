import socket
import os
import threading
import zipfile
import time
import json

import sys

if len(sys.argv) < 2:
    print("Usage: python server.py <iteration_number>")

iteration_number = int(sys.argv[1])
print(iteration_number)

def receive_data(server_socket, iteration):
    # the amount of clients
    number_clients = 0
    #client_conn = []
    while True:
        conn, addr = server_socket.accept()
        print("Connection from:", addr)

        if iteration < 5:#5
            send_json_file(conn, './initial_balancing.json')
            #if iteration > 0:#0
            os.system('python3 feedback.py')
        else:
            os.system('python3 feedback.py')
            # adjust path
            latest_subdir = max(all_subdirs_of('./runs/detect'), key=os.path.getmtime)
            print(latest_subdir)
            balancing_json = latest_subdir + '/new_balancing.json'
            send_json_file(conn, balancing_json)

        # Receive the zip file containing multiple images
        with open(f'received_images{number_clients}.zip', 'wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)

        print("Images received and saved as 'received_images.zip'")
        conn.close()

        # Extract the received zip file to a new folder
        # adjust path
        extract_folder = 'Server_Client_NoneF/traindata/images/train'
        with zipfile.ZipFile(f'received_images{number_clients}.zip', 'r') as zip_ref:
            zip_ref.extractall(extract_folder)

        print(f"Images extracted to '{extract_folder}' folder")
        #os.remove('received_images.zip')
        os.system("python3 choose_random_val.py")
        #print(conn)
        #client_conn.append(conn)
        if number_clients == 9:
            #return client_conn
            break
        else:
            number_clients += 1


def send_json_file(client_socket, file_path):
    # Read JSON data from file
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    try:
        # Convert JSON data to bytes
        json_bytes = json.dumps(json_data).encode('utf-8')

        # Send the JSON data to the client
        client_socket.sendall(json_bytes)
        print("JSON data sent successfully")
    except Exception as e:
        print("Error occurred while sending JSON data:", e)

def all_subdirs_of(b='.'):
  result = []
  for d in os.listdir(b):
    bd = os.path.join(b, d)
    if os.path.isdir(bd) and 'train' in d.lower(): result.append(bd)
  return result

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(1)
    print("Server listening on port 5555...")

    #for i in range(1, 2):
    print(f"START ITERATION {iteration_number}")

    #send_message(server_socket)
    receive_data(server_socket, iteration_number)

    os.system(f"python3 labels_extraction_server.py")
    os.remove('Server_Client_NoneF/val_images.txt')
    os.remove('Server_Client_NoneF/train_names_txt.txt')
    print("NOW TRAIN")
    os.system(f"python3 yolo_train.py")

    print("_____________________________________")
    print("Bye")
    server_socket.close()
if __name__ == "__main__":
    main()
