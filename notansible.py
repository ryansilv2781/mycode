#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH"""

import paramiko

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    credz = [
             {"un": "bender", "ip": "10.10.2.3"}, 
             {"un": "zoidberg", "ip": "10.10.2.5"}, 
             {"un": "fry", "ip": "10.10.2.4"}
            ]

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # loop across the collection credz
    for cred in credz:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("sudo apt install sl -y")

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command('test -f /usr/games/sl && echo "FILE exists" || echo "File does not exist"')

        resp= sessout.read().decode('utf-8')

        if "FILE exists" in resp:
            #appropriate action

            resp == "FILE exists"
            print("file exists")
  
            OR 
            
            resp == "file does not exist"
            print("file does not exist")


        ## display output
        #print(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
        #sshsession.close()

    main()
