import socet

server_socet.bind(('localhost', 12345))
server_socet.listen(1)

print("Сервер запущен и ожидает подключений...")

client_socet, client_address = server_socet.accept()
print(f"Соединение установлено с {client_address}")

data = client_socket.recv(1024)
print(f"Получены данные: {data}")

client_socket.close()
server_socket.close()