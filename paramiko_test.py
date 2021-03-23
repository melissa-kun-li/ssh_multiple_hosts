from paramiko import SSHClient, AutoAddPolicy

def ssh_connect(hosts):
    try:
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
            client.connect(host, username='melissali', allow_agent=True, look_for_keys=False)

            execute_command(client)
    
    except Exception as e:
        print('SSH connection failed: ', e)

def execute_command(client):
    # run a command
    stdin, stdout, stderr = client.exec_command('uname -a')

    # if success code (0), print the output of command
    if stdout.channel.recv_exit_status() == 0:
        print(stdout.read().decode('utf8'))
    # if failed, print error message
    else:
        print(stderr.read().decode('utf8'))

    # these are file objects, so close them
    stdin.close()
    stdout.close()
    stderr.close()

    # close the client
    client.close()

if __name__ == '__main__':
    hosts = ('192.168.2.249',
             '192.168.2.199',)
    ssh_connect(hosts)