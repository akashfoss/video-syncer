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

> $ sudo chown -R syncplay *

> $ sudo make install

Fix missing dependencies by installing the python dependencies via pip (Generic)

> $ sudo apt-get install python python-pip

> $ pip install twisted

> $ pip install PySide

For syncplay service, if you have screen not installed

> $ sudo apt-get install screen

> $ sudo nano -w /etc/init.d/syncplay

```
#!/bin/bash
# Start script for Syncplay server

server_start()
{
    running=`screen -ls | grep syncplay-server`
    if [ "$running" == "" ]; then
        screen -dmS syncplay-server
        screen -S syncplay-server -X screen syncplay-server --password myPassword --port 4567 --salt XXXXXXXX --motd-file /opt/syncplay/motd.txt
        echo "Syncplay sever started"
    else
        echo "Syncplay server already running"
    fi
}

server_stop()
{
    running=`screen -ls | grep syncplay`
    if [ "$running" != "" ]; then
        screen -ls | grep syncplay-server | cut -d. -f1 | awk '{print $1}' | xargs kill
        echo "Syncplay sever stopped"
    else
        echo "Syncplay server not running"
    fi
}


case "$1" in
    start)
        server_start
        ;;

    stop)
        server_stop
        ;;

    restart|reload)
        server_stop
        server_start
        ;;

    status)
        echo "Syncplay servers found (if any):"
        screen -ls | grep syncplay-server
        ;;

    *)
        echo "usage: $0 start|stop|restart|reload|status" >&2
        exit 1
esac

exit 0
```
On to the final step, we only have to make our init script executable now and our server is ready to go! 

> $ sudo chmod +x /etc/init.d/syncplay

Now, try start with a new terminal and run **syncplay**

syncplay command is to create a server initially. Later the client has to join the show by running the syncplayClient.py, and fill the necessary blocks, like - username, default port, etc. And click on "I'm ready to watch" option, on the both side.

Now load the video which you downloaded using the quickshare.py to the client side as well. 

Finally, the video will be synchronized on different screens.

### Developers

* Akash Krishnan (https://github.com/akashfoss)

* Akhileshwar Maurya (https://github.com/akhilesh0070)
