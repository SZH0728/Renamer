# -*- coding:utf-8 -*-
# AUTHOR: Sun

from typing import Any, Callable
from queue import Queue, Full, Empty
from random import random
from time import sleep
from logging import getLogger

logger = getLogger(__name__)


class Client(object):
    """
    Represents a client that can send and receive messages through a server.
    表示一个可以通过服务器发送和接收消息的客户端。
    """
    def __init__(self, server: 'Server', token: float):
        """
        Initializes a new instance of the Client class.
        初始化一个新的客户端实例。

        :param server: The server object this client will communicate through.
                       此客户端将通过其进行通信的服务器对象。
        :param token: A unique identifier for this client.
                      该客户端的唯一标识符。
        """
        self._server = server
        self._token = token

    def send(self, message: Any):
        """
        Sends a message to the server.
        向服务器发送一条消息。

        :param message: The message to send.
                        要发送的消息。
        :return: True if the message was successfully sent, otherwise False.
                 如果消息成功发送则返回True，否则返回False。
        """
        return self._server.send(message, self._token)

    def read(self):
        """
        Reads a message from the server.
        从服务器读取一条消息。

        :return: The received message or None if the channel is empty.
                 接收到的消息或如果通道为空则返回None。
        """
        return self._server.get(self._token)

    def is_empty(self):
        """
        Checks if the client's communication channel is empty.
        检查客户端的通信通道是否为空。

        :return: True if the channel is empty, otherwise False.
                 如果通道为空则返回True，否则返回False。
        """
        return self._server.is_empty(self._token)

    def is_full(self):
        """
        Checks if the client's communication channel is full.
        检查客户端的通信通道是否已满。

        :return: True if the channel is full, otherwise False.
                 如果通道已满则返回True，否则返回False。
        """
        return self._server.is_full(self._token)

    def wait_for_message(self, max_wait_time: int = None, stop_flag: Callable = None) -> Any | None:
        """
        Waits for a message to arrive.
        等待一条消息到达。

        :param max_wait_time: Maximum time (in seconds) to wait for a message.
                              最大等待时间（秒）以等待消息。
        :param stop_flag: A function that returns True to stop waiting.
                          一个返回True以停止等待的函数。
        :return: The received message or None if timed out or stopped by the flag.
                 接收到的消息或如果超时或被标志停止则返回None。
        """

        if max_wait_time and stop_flag:
            raise ValueError('max_wait_time and stop_flag cannot be set at the same time')

        while True:
            if not self.is_empty():
                return self.read()

            if max_wait_time:
                max_wait_time -= 0.1
                if max_wait_time <= 0:
                    return None

            if stop_flag and stop_flag():
                return None

            sleep(0.1)


class Server(object):
    """
    Represents a server that manages multiple channels for clients to communicate.
    表示管理多个客户端通信通道的服务器。
    """
    def __init__(self):
        """
        Initializes a new instance of the Server class.
        初始化一个新的服务器实例。
        """
        # Create two random tokens and associate them with two queues.
        # 创建两个随机令牌，并将它们与两个队列关联起来。
        self._channel = {
            random(): Queue(),
            random(): Queue(),
        }

        # Create client objects for each channel.
        # 为每个通道创建客户端对象。
        self._client = tuple(Client(self, key) for key in self._channel.keys())

    def get_client(self) -> tuple[Client]:
        """
        Returns all client objects associated with this server.
        返回所有与该服务器关联的客户端对象。

        :return: A tuple containing all Client instances.
                 包含所有 Client 实例的元组。
        """

        return self._client

    def _get_another_channel(self, token) -> Queue | None:
        """
        Finds the other channel associated with the given token.
        查找与给定令牌相关联的另一个通道。

        :param token: The token of the current channel.
                      当前通道的令牌。
        :return: The other channel or None if the token is invalid.
                 另一个通道或如果令牌无效则返回None。
        """

        if token not in self._channel:
            logger.error(f'token {token} not found')
            return None

        for key, value in self._channel.items():
            if key != token:
                logger.debug(f'found another channel: {key}')
                return value

    def send(self, message: Any, token: float) -> bool:
        """
        Sends a message to the channel associated with the given token.
        将一条消息发送到与给定令牌相关的通道。

        :param message: The message to send.
                        要发送的消息。
        :param token: The token identifying the sender's channel.
                      标识发送者通道的令牌。
        :return: True if the message was successfully sent, otherwise False.
                 如果消息成功发送则返回True，否则返回False。
        """

        logger.debug(f'send message: {message} from {token}')

        if token not in self._channel:
            logger.error(f'token {token} not found, message {message} is dropped')
            return False

        channel = self._get_another_channel(token)

        try:
            channel.put(message)
        except Full:
            logger.error(f'put message {message} to channel {channel} failed: channel is full')
            return False
        else:
            return True

    def get(self, token: float) -> Any:
        """
        Retrieves a message from the channel associated with the given token.
        从与给定令牌相关的通道中获取一条消息。

        :param token: The token identifying the receiver's channel.
                      标识接收者通道的令牌。
        :return: The received message or None if the channel is empty.
                 接收到的消息或如果通道为空则返回None。
        """
        logger.debug(f'get message from {token}')

        if token not in self._channel:
            logger.error(f'token {token} not found')
            return None

        channel = self._get_another_channel(token)

        try:
            message = channel.get()
        except Empty:
            logger.error(f'get message from channel {channel} failed: channel is empty')
            return None
        else:
            return message

    def is_full(self, token: float) -> bool:
        """
        Checks if the channel associated with the given token is full.
        检查与给定令牌相关的通道是否已满。

        :param token: The token identifying the channel.
                      标识通道的令牌。
        :return: True if the channel is full, otherwise False.
                 如果通道已满则返回True，否则返回False。
        """
        logger.debug(f'check channel {token} is full')

        if token not in self._channel:
            logger.error(f'token {token} not found')
            return False

        return self._channel[token].full()

    def is_empty(self, token: float) -> bool:
        """
        Checks if the channel associated with the given token is empty.
        检查与给定令牌相关的通道是否为空。

        :param token: The token identifying the channel.
                      标识通道的令牌。
        :return: True if the channel is empty, otherwise False.
                 如果通道为空则返回True，否则返回False。
        """
        logger.debug(f'check channel {token} is empty')

        if token not in self._channel:
            logger.error(f'token {token} not found')
            return False

        return self._channel[token].empty()


if __name__ == '__main__':
    pass