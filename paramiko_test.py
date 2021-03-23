from paramiko import SSHClient, AutoAddPolicy

hosts = ('192.168.2.249',
         '192.168.2.199',)
        
# iterate over hosts
for host in hosts:
    # create SSHClient object
    client = SSHClient()

    # load host keys on linux:
    client.load_host_keys('/home/melissali/.ssh/known_hosts')

    # on my mac:
    # client.load_host_keys('/users/melissali/.ssh/known_hosts')    

    client.load_system_host_keys()

    # set policy when connecting to server without known host key
    client.set_missing_host_key_policy(AutoAddPolicy())

    # connect to server and authenticate to it, I'm using ssh-agent
    client.connect(host, username = 'melissali', allow_agent = True, look_for_keys = False)

    # run a command
    stdin, stdout, stderr = client.exec_command('uname -a')

    # if success code (0), print the output of command
    if stdout.channel.recv_exit_status() == 0:
        print(f'{stdout.read().decode("utf8")}')
    # if failed, print error messages
    else:
        print(f'{stderr.read().decode("utf8")}')

    # these are file objects, so close them
    stdin.close()
    stdout.close()
    stderr.close()

    # close the client
    client.close()
