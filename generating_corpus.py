import os
import random
import nltk
import string

nltk.download("punkt")  # Download the Punkt tokenizer

def generate_corpus(num_sentences, min_length, max_length, output_file):
    sentences = []

    # Add your own text sources here
    text_sources = [
        nltk.corpus.brown.sents(),
        nltk.corpus.reuters.sents(),
        nltk.corpus.gutenberg.sents(),
        # Add more text sources as needed
    ]

    # Combine sentences from multiple text sources
    for source in text_sources:
        sentences.extend(source)

    with open(output_file, "w", encoding="utf-8") as file:
        count = 0
        while count < num_sentences:
            sentence = random.choice(sentences)
            tokenized_sentence = nltk.word_tokenize(" ".join(sentence))
            sentence_length = len(tokenized_sentence)
            if sentence_length >= min_length and sentence_length <= max_length:
                sentence_text = " ".join(sentence)
                file.write(sentence_text + "\n")
                count += 1


def main():
    corpus_size = 1000000
    min_sentence_length = 5
    max_sentence_length = 10
    output_directory = "english_sentence_corpus"
    output_file = os.path.join(output_directory, "corpus.txt")

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    generate_corpus(corpus_size, min_sentence_length, max_sentence_length, output_file)


if __name__ == "__main__":
    main()





"""

def generate_corpus(num_sentences, min_length, max_length, output_file):
    corpus = []
    exclude_chars = set(string.punctuation)  # Set of punctuation characters

    while len(corpus) < num_sentences:
        sentence = random.choice(nltk.corpus.gutenberg.sents())
        if min_length <= len(sentence) <= max_length:
            word_count = 0
            filtered_sentence = []
            for word in sentence:
                if any(char in exclude_chars for char in word):
                    filtered_sentence.append(word)
                else:
                    word_count += 1
                    filtered_sentence.append(word)

            if word_count >= min_length and word_count <= max_length:
                corpus.append(" ".join(filtered_sentence))

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(corpus))
"""