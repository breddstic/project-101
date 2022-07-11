class TransferData:
    from dropbox.client import DropboxClient


access_token, local_directory, dropbox_destination = sys.argv[1:4]
client = DropboxClient(access_token)


for root, dirs, files in os.walk(local_directory):

    for filename in files:
        
        local_path = os.path.join(root, filename)

        relative_path = os.path.relpath(local_path, local_directory)
        dropbox_path = os.path.join(dropbox_destination, relative_path)

        with open(local_path, 'rb') as f:
            client.put_file(dropbox_path, f)