#!/bin/bash
rsync tcp-server.py jetson@10.0.111.176:/home/jetson/tcp-server/
rsync tcp-client.py jetson@10.0.111.176:/home/jetson/tcp-server/
ssh -t jetson@10.0.111.176 "cd /home/jetson/tcp-server/ && tmux new -ds chat-server 'python3 tcp-server.py' && tmux new -ds chat-client 'python3 tcp-client.py'"