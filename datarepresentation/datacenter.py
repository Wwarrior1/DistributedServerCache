class DataCenter:

    def __init__(self, endpoints, movies, servers, connections, requests):
        self.endpoints = endpoints
        self.movies = movies
        self.servers = servers
        self.connections = connections
        self.requests = requests

        for connection in connections:
            connection.server.connections.append(connection)
            connection.endpoint.connections.append(connection)
