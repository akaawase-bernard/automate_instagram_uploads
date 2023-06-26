import os
from instagrapi import Client

# Instagram account credentials
username = "your_username"
password = "your_password"

# Folder containing videos
video_folder = "/path/to/videos/folder"

# Initialize Instagram client
client = Client()
client.login(username, password)

# Iterate over files in the video folder
for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        # Prepare video path
        video_path = os.path.join(video_folder, filename)

        # Upload video to Instagram
        media = client.video_upload(video_path)
        caption = "Check out this video!"
        client.photo_edit(media.pk, caption=caption)
        client.photo_configure(media.pk, usertags=[{"user_id": client.user_id, "position": [0.5, 0.5]}])
        client.photo_publish(media.pk)
        print(f"Uploaded video: {filename}")

# Logout from Instagram
client.logout()
