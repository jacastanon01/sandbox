CASE1 = [
    "well it",
    "the whole thing",
    "kill that knight, it",
    "get him!",
    "donkey kong",
    "oh come on, get them",
    "run away from the baddies",
]
CASE2 = [
    "well dang it",
    "dang the whole dang thing",
    "kill that knight, dang it",
    "get him!",
    "donkey kong",
    "oh come on, get them",
    "run away from the dang baddies",
]

def filter_messages(messages):
    filtered_messages = []
    removed_words_count = []

    for message in messages:
        split_words = message.split()
        acceptable_words = []
        counter = 0
        
        for word in split_words:
            if (word == 'dang'):
                counter += 1
            else:
                acceptable_words.append(word)

        non_bad_words = ' '.join(acceptable_words)
        print("LOOP: ", non_bad_words)
        filtered_messages.append(non_bad_words)
        removed_words_count.append(counter)
        
    print(filtered_messages, removed_words_count)

filter_messages(CASE2)