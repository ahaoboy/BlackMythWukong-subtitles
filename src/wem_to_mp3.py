import os
import subprocess
import env

def convert_wem_to_mp3(wem_file_path, mp3_file_path):
    dir_path = os.path.dirname(mp3_file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    command = ["vgmstream-cli", "-o", mp3_file_path, wem_file_path]
    subprocess.run(command, check=True)

def process_directory_recursively(input_directory):
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".wem"):
                wem_file_path = os.path.join(root, file)
                mp3_file_path = (os.path.splitext(wem_file_path)[0] + ".mp3").replace(env.AUDIO_DIR, env.MP3_DIR)
                convert_wem_to_mp3(wem_file_path, mp3_file_path)

if __name__ == "__main__":
    process_directory_recursively(env.AUDIO_DIR)
