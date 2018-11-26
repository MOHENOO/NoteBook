### tcp_client

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


