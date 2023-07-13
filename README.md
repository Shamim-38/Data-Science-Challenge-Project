# Data-Science-Challenge-Project
Data Science Challenge Project


This repository contains the code and resources for the Data Science Challenge project. The project aims to analyze synthetic datasets that mimic real-world behavior and derive actionable insights from them.
Project Overview

The Data Science Challenge revolves around analyzing synthetic datasets mimicking real-world behavior and deriving actionable insights.
Installation

To use this project on your local machine, you must have an NVIDIA GPU.

1. Install PyTorch by following the instructions provided here. For Windows users, it is highly recommended to use the Conda installation path to avoid potential dependency problems.

2. Install TorToiSe and its dependencies, as well as nltk for generating the corpus:

shell

    git clone https://github.com/neonbjb/tortoise-tts.git
    cd tortoise-tts
    python -m pip install -r ./requirements.txt
    python setup.py install

Cloning Process

Follow these steps to perform the cloning process:

1. Copying the bonafide files:

In the root directory, run the following command:

shell

python3 transfer_bonafide_files.py

2. Corpus generation:

In the root directory, navigate to the "Data Science Project Challenge" folder and run the following command:

shell """

python3 generating_corpus.py
"""

3. Creating cloning audios:

Navigate to the "tortoise-tts" directory.

    Without using multiprocessing techniques:

    shell

python3 cloning_audio_files.py

Using multiprocessing techniques:

shell

        python3 cloning_audio_files_using_multiprocessing_techniques.py

Report

The "Report" directory contains two important files:

    technical_report.pdf: Provides detailed information for data scientists.
    Slides.pdf: Provides a summary of the project and its findings, targeted towards non-data scientists.

Feel free to explore the code and resources in this repository. If you have any questions or feedback, please don't hesitate to reach out.
License

This project is licensed under the MIT License.
