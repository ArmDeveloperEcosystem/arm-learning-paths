import os
from better_profanity import profanity

def load_excluded_words(file_path):
    with open(file_path, 'r') as f:
        excluded_words = [word.strip() for word in f.readlines()]
    return excluded_words

def scan_for_profanities(directory, log_file, excluded_words_file=None):
    exclude_words = None
<<<<<<< HEAD
    profanities = None
=======
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
    if excluded_words_file:
        exclude_words = load_excluded_words(excluded_words_file)

    with open(log_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):  # Read only markdown files
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as code_file:
<<<<<<< HEAD
                        profanities = None
=======
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
                        content = code_file.read()
                        if exclude_words:
                            excluded_content = content
                            for word in exclude_words:
                                excluded_content = excluded_content.replace(word, '')
                            if profanity.contains_profanity(excluded_content):
<<<<<<< HEAD
                                profanities = set(word for word in excluded_content.split() if profanity.contains_profanity(word))
                        else:
                            if profanity.contains_profanity(content):
                                profanities = set(word for word in content.split() if profanity.contains_profanity(word))
                        if profanities:
                                    f.write(f"Profanity found in file: {file_path}\n")
                                    f.write("Profanities found: ")
                                    f.write(", ".join(profanities))
                                    f.write("\n\n")

scan_for_profanities("./content/", "./profanity_log.txt", excluded_words_file="./.profanity_ignore.yml")
=======
                                f.write(f"Profanity found in file: {file_path}\n")
                                f.write("Profanities found: ")
                                profanities = set(word for word in excluded_content.split() if profanity.contains_profanity(word))
                                f.write(", ".join(profanities))
                                f.write("\n\n")
                        else:
                            if profanity.contains_profanity(content):
                                f.write(f"Profanity found in file: {file_path}\n")
                                f.write("Profanities found: ")
                                profanities = set(word for word in content.split() if profanity.contains_profanity(word))
                                f.write(", ".join(profanities))
                                f.write("\n\n")

scan_for_profanities("./content/", "./profanity_log.txt", excluded_words_file="./.profanity_ignore.yml")  
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
