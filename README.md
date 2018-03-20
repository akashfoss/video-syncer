# Video Sharing and Syncing Tool

## Run quickshare.py to share any files between the client/server or peers

Copy paste the quickshare.py file to the folder where your video is located.To run the script, do

> $ python quickshare.py 

It will prompt the user to enter a port number or skip with a default port number - 8000. Once the script is successfully running, it means the server has been created and it will generate a combination of IP address and port number (URL for sharing the files).

Now, the clients in the same local network will have to search for the given URL in their browser and download the necessary videos.

## Run the Video Syncer to sync any video between client/server or peers.

For building and installing syncplay - 

> $ sudo useradd -r syncplay
> $ sudo mkdir /opt/syncplay
> $ sudo chown syncplay /opt/syncplay
> $ cd /opt/syncplay
> $ sudo chmod -R 775 /opt/syncplay


If you have git installed (Replace 9752aad with the id of the latest release tagged commit!)
> $ git clone https://github.com/Syncplay/syncplay.git ./
> $ git reset --hard 9752aad
