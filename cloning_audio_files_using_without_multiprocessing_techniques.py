import os
import random
import pandas as pd
import soundfile as sf
import time
import shutil

# Imports used through the rest of the notebook.
import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F

import IPython

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

# This will download all the models used by Tortoise from the HF hub.
tts = TextToSpeech()

def clone_audio_files(bonafide_path, corpus_path, n):
    bonafide_files = sorted(os.listdir(bonafide_path))
    #print(bonafide_files)
    print(bonafide_files[0])
    cloned_dir = os.path.join(os.getcwd(), "../", "cloned_audio_files")
    print(cloned_dir)
    os.makedirs(cloned_dir, exist_ok=True)
    mapping = []

    for audio_file in bonafide_files:
        bonafide_file_path = os.path.join(bonafide_path, audio_file)
        cloned_files = []

        for i in range(n):
            selected_sentences = random.sample(read_sentences(corpus_path), 2)

            print(selected_sentences)
            selected_sentences_str = ' '.join(selected_sentences)
            print(selected_sentences_str)

            cloned_file = f"{audio_file.split('.')[0]}_clone_{i+1}.flac"
            cloned_file_path = os.path.join(cloned_dir, cloned_file)
            cloned_files.append(cloned_file_path)

            # Generate cloned audio using Tortoise-TTS
            #text = random.choice(selected_sentences)
            generate_audio(bonafide_file_path, cloned_file_path, selected_sentences_str)

        mapping.append((bonafide_file_path, cloned_files))

    return mapping

def read_sentences(corpus_path):
    with open(corpus_path, 'r', encoding='utf-8') as f:
        sentences = f.readlines()
    return [sentence.strip() for sentence in sentences]

def generate_audio(bonafide_file_path, cloned_file_path, text):

    #tts = TextToSpeech()
    # Load it and send it through Tortoise.
    # Read the FLAC file
    bonafide_file_name = os.path.basename(bonafide_file_path).split('.')[0]        #making a folder name with bonafide audio file name   
    tortoise_voice_dir = os.path.join(os.getcwd(),"tortoise/voices", bonafide_file_name) #new folder in tortoise_voice
    #print(tortoise_voice_dir)
    #print(os.path.basename(bonafide_file_path).split('.')[0])
    os.makedirs(tortoise_voice_dir, exist_ok=True)
    
    convert_flac_to_wav(bonafide_file_path, tortoise_voice_dir) #first one is input directory and second one is destinity directory 

    #shutil.copy2(audio_file_path, tortoise_voice_dir)

    #data, samplerate = sf.read(audio_file_path)
    clone_file_name = os.path.basename(cloned_file_path).split('.')[0]
    # Write the data to a WAV file
    #sf.write(os.path.join(voice_dir, "a.wav"), data, samplerate, format='WAV')
    print(f'Working For Cloning Bonafide Audio -- "{bonafide_file_name}" & Text-- "{text}" Convert to Clone Audio -- "{clone_file_name}"')

    voice_samples, conditioning_latents = load_voice(os.path.basename(bonafide_file_path).split('.')[0])
    preset = "ultra_fast"
    gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, preset=preset)
    torchaudio.save(cloned_file_path, gen.squeeze(0).cpu(), 24000)

def convert_flac_to_wav(file_path, destination_path):
    """
    Converts FLAC audio to WAV format.

    Args:
        file_path (str): Path to the FLAC audio file.

    """
    wav_path = os.path.join(destination_path, "a.wav")
    data, samplerate = sf.read(file_path)
    sf.write(wav_path, data, samplerate, format='WAV')

def clone_audio_files_wrapper(bonafide_audio_path, corpus_path, n):
    if n < 2:
        print("Error: n should be greater than or equal to 2.")
        return

    mapping = clone_audio_files(bonafide_audio_path, corpus_path, n)

    df = pd.DataFrame(mapping, columns=["Bonafide File", "Cloned Files"])
    df.to_csv(os.path.join(os.getcwd(), "../", "cloned_files_mapping.csv"), index=False)

    print("Cloning process completed.")

if __name__ == "__main__":
    
    bonafide_audio_path = input("Enter the path of the bonafide_audio_files folder: ")
    corpus_path = input("Enter the path of the english_sentence_corpus/corpus3.txt file: ")
    n = int(input("Enter the value of n (number of clones, should be >= 2): "))
    """
    bonafide_audio_path = "/home/shamim/Data Science Project Challenge/c/"
    corpus_path = "/home/shamim/Data Science Project Challenge/english_sentence_corpus/corpus3.txt"
    n = 2
    """
    

    start_time = time.time()  # Start the timer
    
    clone_audio_files_wrapper(bonafide_audio_path, corpus_path, n)
    
    end_time = time.time()  # Stop the timer
    execution_time = end_time - start_time
    
    print(f"Execution time: {execution_time} seconds")
