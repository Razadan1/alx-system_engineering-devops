#!/bin/bash

if [ "$#" -lt 4 ];
then
	        echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
		exit 1
fi

FILE_PATH="$1"
IP="$2"
USER="$3"
SSH_PATH="$4"

scp -o StrictHostKeyChecking=no -i "$SSH_PATH" "$FILE_PATH "$USER@$IP:~/"

if [$? -eq 0]; then
	echo "File transfer successful!"
else
	echo "File transfer failed."
fi
