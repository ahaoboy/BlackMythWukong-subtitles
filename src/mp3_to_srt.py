import os
import whisper
from whisper.utils import get_writer
import env
model = whisper.load_model("large")

def convert_mp3_to_srt(mp3_file_path, srt_file_path):
    try:
        result = model.transcribe(mp3_file_path)
        dir_path = os.path.dirname(os.path.abspath(srt_file_path))
        if not os.path.exists(dir_path):
          os.makedirs(dir_path)
        file_name = os.path.basename(srt_file_path)
        srt_writer = get_writer("srt", dir_path)
        srt_writer(result, file_name)
        print(f"save: {srt_file_path}")
    except Exception as e:
        print(f"error: {e}")

def process_directory_recursively(input_directory):
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".mp3"):
                mp3_file_path = os.path.join(root, file)
                srt_file_path = (os.path.splitext(mp3_file_path)[0] + ".srt").replace(env.MP3_DIR, env.SRT_DIR)
                if os.path.exists(srt_file_path):
                    continue
                convert_mp3_to_srt(mp3_file_path, srt_file_path)

if __name__ == "__main__":
    process_directory_recursively(env.MP3_DIR)
