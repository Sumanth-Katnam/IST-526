import string

def remove_punctuation(s):
    return s.translate(str.maketrans("","", string.punctuation))

def get_pairs(sentence, window_size):
    # Removing all punctuations and splitting into words list 
    words = remove_punctuation(sentence).split()
    pairs_list = []
    
    vocab_size = len(words)
    
    for i in range(vocab_size):
        target = words[i]
        
        left_window = window_size - 1
        left_index = i - 1
        while left_window > 0:
            if left_index in range(vocab_size):
                pairs_list.append((target, words[left_index]))
            left_window -= 1
            left_index -= 1

        right_window = window_size - 1
        right_index = i + 1
        while right_window > 0:
            if right_index in range(vocab_size):
                pairs_list.append((target, words[right_index]))
            right_window -= 1
            right_index += 1

    return pairs_list

if __name__ == "__main__":
    print(get_pairs("In Their Last Moments, People Show You Who They Really Are.", 5))