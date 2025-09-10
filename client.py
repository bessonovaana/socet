import socet

client_socet=socet.socet(socet.AF_INET, socet.SOCK_STREAM)

client_socet.connect(('localhost',12345))

client_socket.sendall(b'Hello, server!')

client_socket.close()