# SSH to Multiple Hosts

I've written and tested two scripts, one uses Paramiko (a low-level SSH client Python library) and one uses Parallel-SSH (an asynchronous SSH library based on C libraries with a Python API). 

## Function
From my Linux (Centos), I connect via SSH to two hosts: my Mac and to the same Linux host. I then execute the command `uname -a` on those two hosts. Paramiko executes the two commands synchronously while Parallel-SSH executes the commands on the two hosts in parallel. I'm using `ssh-agent` to handle my keys which Parallel-SSH automatically detects and Paramiko can be configured to detect. 

## Set up:
To avoid the need to write my password in plain-text, I created the SSH keys using the `ssh-keygen` command and copied the public key to the remote server (in this case my Mac). I also restricted the permissions in my ssh directory to just myself using `chmod 700 ~/.ssh`. Then, to avoid having to specify the private key file path in the script, I decided to use `ssh-agent`. I started the process with `` eval `ssh-agent` ``, then did `ssh-add` and added the filepaths of the private keys.
ssh-agent doesn't persist across reboots, so I had to manually do ssh-add again each time. Otherwise, I could set up a script for that.

## Outputs:

**Paramiko**:

[![Screen-Shot-2021-03-23-at-3-30-26-PM.png](https://i.postimg.cc/9fd11SHQ/Screen-Shot-2021-03-23-at-3-30-26-PM.png)](https://postimg.cc/3ywgxtws)

**Pssh**: 

[![Screen-Shot-2021-03-23-at-3-27-41-PM.png](https://i.postimg.cc/Hsr2Fj1K/Screen-Shot-2021-03-23-at-3-27-41-PM.png)](https://postimg.cc/jLrP7x5Q)

I haven't directly tested the performance or user experience yet, however the Pssh script outputs visibly faster with just 2 hosts. Pssh seems to offer greater scalability.
