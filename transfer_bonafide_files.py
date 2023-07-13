import os
import shutil

# Root directory of the project
root_dir = "/home/shamim/Data Science Project Challenge/"

# Directory containing the protocol files
protocol_dir = os.path.join(root_dir, "LA/ASVspoof2019_LA_cm_protocols")

# Directories containing the audio files
audio_dirs = [
    os.path.join(root_dir, "LA/ASVspoof2019_LA_dev/flac"),
    os.path.join(root_dir, "LA/ASVspoof2019_LA_eval/flac"),
    os.path.join(root_dir, "LA/ASVspoof2019_LA_train/flac")
]

# Create the 'bonafide_audio_files' directory
output_dir = os.path.join(root_dir, "bonafide_audio_files")
os.makedirs(output_dir, exist_ok=True)

# Process each protocol file
protocol_files = [
    "ASVspoof2019.LA.cm.train.trn.txt",
    "ASVspoof2019.LA.cm.dev.trl.txt",
    "ASVspoof2019.LA.cm.eval.trl.txt"
]

for protocol_file in protocol_files:
    file_path = os.path.join(protocol_dir, protocol_file)

    # Read the lines from the protocol file
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Process each line in the protocol file
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            a, audio_file_name, b, c, key = line.split()
            #print(a)
            #print(audio_file_name)
            #print(b)
            #print(c)
            #print(key)
            
            # Copy bonafide audio files to the output directory
            if key == "bonafide":
                for audio_dir in audio_dirs:
                    audio_file_path = os.path.join(audio_dir, audio_file_name + ".flac")
                    #print(audio_file_path)
                    if os.path.exists(audio_file_path):
                        shutil.copy2(audio_file_path, output_dir)
                        break

            
            
            
print("Bonafide audio files copied to 'bonafide_audio_files' folder.")

