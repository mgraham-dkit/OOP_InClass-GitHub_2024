from abc import ABC
from abc import abstractmethod
from typing import Any


class ITcpNetworkLayer(ABC):
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
    def __init__(self, data_socket):
        self.data_socket = data_socket

    def disconnect(self) -> None:
        if self.data_socket:
            try:
                self.data_socket.close()
            except:
                raise ConnectionError("Exception occurred when closing socket")
        else:
            raise ValueError("No socket available")

    def send(self, message: str) -> None:
        if self.data_socket:
            try:
                self.data_socket.sendall(bytes(message, "utf-8"))
            except:
                raise ConnectionError(f"Exception occurred when sending message")
        else:
            raise ValueError("No socket available")

    def receive(self) -> Any | None:
        if self.data_socket:
            try:
                return self.data_socket.recv(1024)
            except:
                raise ConnectionError(f"Exception occurred when receiving message")
        else:
            raise ValueError("No socket available")