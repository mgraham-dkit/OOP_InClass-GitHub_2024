from abc import ABC
from abc import abstractmethod
import socket
from typing import Any


class ITcpNetworkLayer(ABC):
    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def send(self, message: str) -> None:
        pass

    @abstractmethod
    def receive(self) -> Any | None:
        pass


class TcpNetworkLayer(ITcpNetworkLayer):
    def __init__(self, data_socket=None, host = None, port = -1):
        self.connected = False
        # If we were provided with a data socket, use that
        # and set status to connected
        if data_socket:
            self.data_socket = data_socket
            self.connected = True
            return

        # If we didn't get a socket, check for connection information
        if not host or port == -1:
            raise ValueError("Invalid location information provided.")

        # If we got valid connection information, create socket and set status to connected
        self.data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data_socket.connect((host, port))
        self.connected = True

    def is_connected(self):
        return self.connected

    def disconnect(self) -> None:
        if not self.connected:
            raise ValueError("Socket is not connected")

        # Only attempt to close connection if socket exists AND it is open
        if self.data_socket:
            try:
                # Close socket
                self.data_socket.close()
                # Mark connection as closed (useful for shared connections)
                self.connected = False
            except:
                raise ConnectionError("Exception occurred when closing socket")
        else:
            raise ValueError("No socket available")

    def send(self, message: str) -> None:
        if self.data_socket and self.connected is True:
            try:
                self.data_socket.sendall(bytes(message, "utf-8"))
            except Exception as e:
                print(e)
                raise ConnectionError(f"Exception occurred when sending message")
        else:
            raise ValueError("No socket available")

    def receive(self) -> Any | None:
        if self.data_socket and self.connected is True:
            try:
                return self.data_socket.recv(1024)
            except:
                raise ConnectionError(f"Exception occurred when receiving message")
        else:
            raise ValueError("No socket available")