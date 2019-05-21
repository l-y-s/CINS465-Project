Async websocket chat server project. Implemented as a separate project due to Evennia's redirection/denial of all websocket connections other than the inital connection to the Portal backend.

Chat server, redis backend, and NGINX are brought up with the included docker-compose file. Once running, the main Evennai server will link directly to this server to manage chat connections. This will allow us to run async chat without bogging down the game server.
