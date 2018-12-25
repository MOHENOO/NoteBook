# tcp_python

## tcp_server

- 1.建立socket

  ```python
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  ```

- 2.绑定ip，端口

  ```python
  s.bind(('127.0.0.1',9999))
  ```

- 3.监听端口

  ```python
  s.listen(5)
  ```

- 4.发送/接收数据

  ```python
  d = s.send(b'Welcome')
  d = s.recv(1024)
  ```

- 6.关闭socket

  ```python
  s.close()
  ```

## tcp_client

- 1.建立socket

  ```python
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  ```

- 2.连接ip，端口

  ```python
  s.connect(('www.sina.com.cn',80))
  ```

- 3.发送请求

  ```python
  s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
  ```

- 4.接收反馈

  ```python
  d = s.recv(1024)
  ```

- 5.关闭socket

  ```python
  s.close()
  ```