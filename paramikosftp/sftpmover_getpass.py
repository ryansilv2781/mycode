#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords


def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    #Setting the window and packet sizes might affect the transfer speed. 
    #The default settings in the Transport class are the same as in OpenSSH 
    #and should work adequately for both files transfers and interactive sessions.

    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    #This method is primarily provided as a convenience.

    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    ## copy our firstpasswd.py script to bender
    sftp.put("file_to_move.txt", "file_to_move.txt") # move file to target location home directory
    #Copy a local file (localpath) to the SFTP server as remotepath. 
    #Any exception raised by operations will be passed through. 
    #This method is primarily provided as a convenience.

    ## close the connection
    sftp.close() # Close the SFTP session and its underlying channel.
if __name__ == "__main__":
    main()

