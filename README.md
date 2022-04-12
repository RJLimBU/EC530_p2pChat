# *EC530_p2pChat*

This is a repo for the peer to peer hackathon

## *Architecture*
- One of the programs implements a direct TCP (Transfer Control Protocol) connection with no intermediate server.
- The other program used UDP (User Datagram Protocol) with a routing server to connect two users together, after the
server has been used, it does not participate in the communication anymore.

## *Code*
- `TCP_client.py`: Single file for a TCP client. When two users run the program, 
they can connect to each other and send messages. The sending and receiving of messages
is handles with threads.

## *Screenshots*
- The example below shows the TCP communication between 2 peers
opened in different terminals communicating together. They are assigned
a name upon initialization based on user input.
>![Screenshot](./Images/TCP_CONN.png)

