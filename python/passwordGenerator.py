import os
import shutil
import secrets
import string

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Function to sort files and move them to different folders
def sort_files_in_downloads():
    # Define paths
    downloads_folder = os.path.join(os.path.expanduser("~"), r"C:\Users\moses\Downloads")
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
    pictures_folder = os.path.join(os.path.expanduser("~"), "Pictures")
    videos_folder = os.path.join(os.path.expanduser("~"), "Videos")
    music_folder = os.path.join(os.path.expanduser("~"), "Music")
    other_folder = os.path.join(os.path.expanduser("~"), "Other")

    # List files in the downloads folder
    files = os.listdir(downloads_folder)

    # Tuple to store generated passwords
    generated_passwords = []

    # Iterate through files and move them to appropriate folders based on file type
    for file in files:
        file_path = os.path.join(downloads_folder, file)
        if os.path.isfile(file_path):
            try:
                if file.lower().endswith(('.pdf', '.doc', '.docx', '.txt')):
                    shutil.move(file_path, os.path.join(documents_folder, file))
                elif file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    shutil.move(file_path, os.path.join(pictures_folder, file))
                elif file.lower().endswith(('.mp4', '.avi', '.mov')):
                    shutil.move(file_path, os.path.join(videos_folder, file))
                elif file.lower().endswith(('.mp3', '.wav', '.flac')):
                    shutil.move(file_path, os.path.join(music_folder, file))
                else:
                    shutil.move(file_path, os.path.join(other_folder, file))

                # Generate and store password
                password = generate_password()
                generated_passwords.append((file, password))
            except FileNotFoundError:
                print(f"File '{file}' not found.")
            except Exception as e:
                print(f"Error moving file '{file}': {e}")

    return generated_passwords

# Sort files in the downloads folder and save generated passwords
passwords = sort_files_in_downloads()

# Print generated passwords for future reference
for file, password in passwords:
    print("File: {file}, Password: {password}")

print("Files sorted and moved successfully!")
