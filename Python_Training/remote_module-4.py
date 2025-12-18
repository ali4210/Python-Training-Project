import paramiko
import os


def download_remote_path(sftp, remote_path, local_path):
    """Recursively download files and directories from remote server"""
    try:
        # Get attributes of the remote path
        attrs = sftp.stat(remote_path)

        # If it's a directory, process its contents
        if attrs.st_mode & 0o40000:  # Directory flag
            print(f"Creating directory: {local_path}")
            os.makedirs(local_path, exist_ok=True)

            # List contents of the directory
            for item in sftp.listdir(remote_path):
                remote_item = os.path.join(remote_path, item).replace('\\', '/')
                local_item = os.path.join(local_path, item)
                download_remote_path(sftp, remote_item, local_item)
        else:
            # It's a file, download it
            print(f"Downloading file: {remote_path} -> {local_path}")
            sftp.get(remote_path, local_path)

    except Exception as e:
        print(f"Error processing {remote_path}: {e}")


# Main execution
hostname = "192.168.0.150"
username = "kali"
password = "kali"

# Create local directory if it doesn't exist
local_dir = "K8s"
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname, username=username, password=password)
    mysftp = client.open_sftp()

    # Remote directory to download
    remote_dir = '/home/kali/Kubernetes-Labs/'

    print("Starting download...")
    download_remote_path(mysftp, remote_dir, local_dir)
    print("Download completed!")

except Exception as e:
    print(f"Connection error: {e}")
finally:
    if 'mysftp' in locals():
        mysftp.close()
    client.close()