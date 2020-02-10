def filter_lines(lines):
    new_lines = []
    for line in lines:
        l = line.lower().strip()
        #print(line)
        sentence = re.sub(r"([?.!,])", r" \1 ", l)
        sentence = re.sub(r'[" "]+', " ", sentence)
        # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
        sentence = re.sub(r"[^a-zA-Z?.!,]+", " ", sentence)
        sentence = re.sub(r'^https?:\/\/.*[\r\n]*', '', sentence, flags=re.MULTILINE)
        sentence = sentence.strip()
        new_lines.append(sentence)
    return new_lines

def generate_word_dictionary(text):
    #generate dictionary e.g {'lives': 1, 'nope': 3}
    pass

def preprocess_text(file_name):
    #take file name
    # open the file
    # go through and clean text file.
    # remove handles, links, emojis
    # return
    pass

def word_to_int(text_sequence):
    #convert text sequence to correspoinding number
    pass

def generate_sequence_target_pairs(text):
    # X = pick out sequence of text
    #return X, y
    pass

def train(X, y):
    #train model X and y
    pass