import paramiko

print("Connecting to Cloud Server 1\n")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname='xxxx', port=xxxx, username='xxx', password='xxxxxx')
print("Server 1 is online and connected\n")
print("Receiving data\n")
data = []
sftp_client = ssh_client.open_sftp()
remote_file = sftp_client.open('xxxxx')
try:
    for line in remote_file:
        data.append(str(line).split(','))
finally:
    remote_file.close()
    print("Receiving completed!\n")
