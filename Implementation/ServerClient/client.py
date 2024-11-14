import shutil
import socket
import os
import time
import zipfile
import threading
import random
import struct
import json
import subprocess
import concurrent.futures

import sys

if len(sys.argv) < 2:
    print("Usage: python client.py <iteration_number>")

iteration_number = sys.argv[1]
print(iteration_number)

def send_data(client_socket, folder_path, zip_file_name, percentage, sent_folder, client_id):
    print("Sending data...")
    #print(f"Percentage: {percentage}")
    # Get the list of files in the folder
    files_to_send = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            files_to_send.append(file_path)

    # Calculate the number of files to send based on the percentage, 100 because we selected 100 to send
    num_files_to_send = int(round(1 - percentage, 2) * 100)

    for file_path in files_to_send[:num_files_to_send]:
        shutil.copy(file_path, sent_folder)

    # Compress selected images into a zip file
    with zipfile.ZipFile(zip_file_name, 'w') as zip_ref:
        for root, dirs, files in os.walk(sent_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, sent_folder))

    # Delete the files from the original folder
    for file_path in files_to_send[:num_files_to_send]:
        os.remove(file_path)

    with open(zip_file_name, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    with open(f'./Server_Client_NoneF/stats/stats_client{client_id}', 'a') as file:
        file.write(f'Client {client_id}, Number of files : {num_files_to_send}, Network Utility: {percentage}\n')
    print(f"{num_files_to_send} files in '{folder_path}' sent to the server as '{zip_file_name}'")
    print("_____________________________________")
    os.remove(zip_file_name)
    client_socket.close()


def network_utility() -> float: # generates random here from client
    return round(random.uniform(0, 1), 2)


def receive_message(client_socket, client_id):
    data = client_socket.recv(1024)
    message = data.decode()
    print(f"Received message from server: {message}. I am Client {client_id}.")
    #client_socket.close()

def receive_json_file(client_socket, save_path):
    try:
        # Receive JSON data from the server
        json_bytes = client_socket.recv(4096)

        # Decode JSON data
        json_data = json.loads(json_bytes.decode('utf-8'))

        print("Received JSON data:")
        print(json_data)

        # Save JSON data to a new file
        with open(save_path, 'w') as file:
            json.dump(json_data, file, indent=4)
            print(f"JSON data saved to '{save_path}'")
    except Exception as e:
        print("Error occurred while receiving and saving JSON data:", e)


def client_process(percentage, client_id, iteration):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))
    #print(client_socket)

    print(f"Client_Id: {client_id}")

    #receive_message(client_socket, client_id)
    receive_json_file(client_socket, f'./Server_Client_NoneF/balance_jsons_client/balancing{iteration}.json')

    os.system(f"python3 runSelection.py {client_id} {iteration}")

    os.system(f"python3 labeled_dataset_extraction_client.py {client_id}")

    folder_path = f'Server_Client_NoneF/client{client_id}_dataset/selected{client_id}'
    zip_file_name = f'Server_Client_NoneF/client{client_id}_send.zip'
    sent_folder = f'./Server_Client_NoneF/client{client_id}_dataset/sent{client_id}'

    #print(f'I am client {client_id} and I use dataset {folder_path}.')
    print(f"Client_Id___: {client_id}")
    send_data(client_socket, folder_path, zip_file_name, percentage,sent_folder, client_id )


def main():
    #for i in range(1, 2):
        print(f"START ITERATION {iteration_number}")

        client0_thread = threading.Thread(target=client_process, args=(0, 0, iteration_number))
        client0_thread.start()
        client0_thread.join()

        client1_thread = threading.Thread(target=client_process, args=(0, 1, iteration_number))
        client1_thread.start()
        client1_thread.join()

        client2_thread = threading.Thread(target=client_process, args=(0, 2, iteration_number))
        client2_thread.start()
        client2_thread.join()

        client3_thread = threading.Thread(target=client_process, args=(0, 3, iteration_number))
        client3_thread.start()
        client3_thread.join()

        client4_thread = threading.Thread(target=client_process, args=(0, 4, iteration_number))
        client4_thread.start()
        client4_thread.join()

        client5_thread = threading.Thread(target=client_process, args=(0, 5, iteration_number))
        client5_thread.start()
        client5_thread.join()

        client6_thread = threading.Thread(target=client_process, args=(0, 6, iteration_number))
        client6_thread.start()
        client6_thread.join()

        client7_thread = threading.Thread(target=client_process, args=(0, 7, iteration_number))
        client7_thread.start()
        client7_thread.join()

        client8_thread = threading.Thread(target=client_process, args=(0, 8, iteration_number))
        client8_thread.start()
        client8_thread.join()

        client9_thread = threading.Thread(target=client_process, args=(0, 9, iteration_number))
        client9_thread.start()
        client9_thread.join()

        print("Done")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


if __name__ == "__main__":
    main()
