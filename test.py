import socket
import sys
import multiprocessing

# Define the port for communication
PORT = 65000  # Replace with your desired port number


def send_data(prev_ip, next_ip, data):
    # Create a socket for sending data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connect to the next node
            s.connect((next_ip, PORT))

            # Send data to the next node
            s.sendall(data.encode())
            print(f"Data sent to {next_ip}:{PORT}: {data}")
        except Exception as e:
            print(f"Error sending data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <previous_node_ip> <next_node_ip>")
        sys.exit(1)

    prev_node_ip = sys.argv[1]
    next_node_ip = sys.argv[2]

    data_to_send = prev_node_ip + "Hello, Chord!" + next_node_ip

    # Use multiprocessing to set a timeout
    with multiprocessing.Pool(processes=1) as pool:
        result = pool.apply_async(send_data, (prev_node_ip, next_node_ip, data_to_send))
        try:
            # Wait for a maximum of 60 seconds
            result.get(timeout=60)
        except multiprocessing.TimeoutError:
            # Terminate the process if it runs for more than 60 seconds
            print("Process timed out and is being terminated.")
            result.get()  # This will raise a TimeoutError and terminate the process
