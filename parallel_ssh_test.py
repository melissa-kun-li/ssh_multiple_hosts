from pssh.clients import ParallelSSHClient

# client attempts to use keys in an SSH agent and use all keys in ~/.ssh, but can programmatically set this too
client = ParallelSSHClient(['192.168.2.249', '192.168.2.199'])

# run command for each host in parallel
output = client.run_command('uname -a')

for host_out in output:
    for line in host_out.stdout:
        # print output of command for each host
        print(line)
    exit_code = host_out.exit_code