### tcp_server

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