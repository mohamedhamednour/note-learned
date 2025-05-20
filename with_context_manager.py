class MySocketManager:
    def __init__(self, address):
        self.address = address
        self.connected = False

    def __enter__(self):
        # Here we simulate opening the connection
        print(f"Attempting to connect to address: {self.address}")
        self.connected = False
        print("Connection successful")
        return self  # Return the same object to use it inside the with block

    def send(self, data):
        if not self.connected:
            raise RuntimeError("Connection is not established, cannot send data")
        print(f"Sending data: {data}")

    def __exit__(self, exc_type, exc_value, traceback):
        # Here we simulate closing the connection regardless of what happens inside the with block
        if self.connected:
            print(f"Closing connection to address: {self.address}")
            self.connected = False
        # Print exception details if one occurred
        if exc_type:
            print(f"An exception of type {exc_type} occurred, message: {exc_value}")
        else:
            print("Connection terminated without errors")
        # If we return True here, it suppresses the exception. Keep it False or None to raise the exception if it occurs
        return True

# Example usage:
try:
    with MySocketManager("192.168.1.1") as socket:
        socket.send("Hello, server!")
        # Simulate an error while sending data
        socket.send(None)  # This might cause an issue in a real application
except Exception as e:
    print(f"Caught an exception in the outer code: {e}")

print("\n--- Example without exception ---\n")

with MySocketManager("192.168.1.2") as socket:
    socket.send("This is a message without issues")
