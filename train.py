import re

def filter_lines(lines):
    new_lines = []
    for line in lines:
        l = line.lower().strip()
        sentence = re.sub("@\\w+", "", l)
        sentence = re.sub("[ |\t]{2,}", "", sentence)
        #sentence = re.sub("http\\w+", "", sentence)
        sentence = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', sentence, flags=re.MULTILINE)
        #print(line)
        #sentence = re.sub(r"([?.!,])", r" \1 ", l)
        #sentence = re.sub(r'[" "]+', " ", sentence)
        # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
        #sentence = re.sub(r"[^a-zA-Z?.!,]+", " ", sentence)
        #sentence = re.sub(r'^https?:\/\/.*[\r\n]*', '', sentence, flags=re.MULTILINE)
        sentence = sentence.strip()
        new_lines.append(sentence)
    return new_lines

def generate_word_dictionary(text):
    #generate dictionary e.g {'lives': 1, 'nope': 3}
    word_dict ={}
    count = 0 
    for i in text.split():
        if i not in word_dict:
            word_dict[i] = count 
            count+= 1
    return word_dict 


def preprocess_text(file_name):
    # take file name
    # open the file
    # go through and clean text file.
    # remove handles, links, emojis
    f = open(file_name, encoding="utf8")
    lines = f.readlines()
    sentence = filter_lines(lines)
    return sentence

def word_to_int(text_sequence, word_dict):
    return [word_dict[x] for x in text_sequence]
    #convert text sequence to correspoinding number

def int_to_word(num_sequence, word_dict):
    word_list = []
    for val in num_sequence:
        for k,v in word_dict.items:
            if val == v:
                word_list.append(k)
    return word_list

def generate_sequence_target_pairs(text, word_dict,seq_length=20):
    # X = pick out sequence of text
    wordlist = text.split()
    lst = []
    for i in range(0, len(wordlist)//seq_length):
        xy = wordlist[(i*seq_length):(i+1)*seq_length]
        x = word_to_int(xy[0:len(xy)-1], word_dict)
        y = word_to_int(xy[len(xy)-1:], word_dict)
        lst.append((x,y))
    return lst

def train(X, y):
    #train model X and y
    pass

def change_list(sentence):
    one_str = ""
    for i in sentence:
        one_str+=i
    return one_str 

if __name__ == "__main__":
    sentence = preprocess_text("jamtweets.txt")
    print(sentence)
    # one_str = change_list(sentence)
    # word_dict = generate_word_dictionary(one_str)
    # print(generate_sequence_target_pairs(one_str, word_dict))
    


    




