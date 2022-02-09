from random import sample;

WORDS_FILENAME = 'words_alpha.txt';
WORD_LENGTH = 5;
# TODO: change to 4
SEQUENCE_LENGTH = 3;

def read_words():
    words = [];
    with(open(WORDS_FILENAME, 'r')) as fid:
        for word in fid:
            words.append(word.strip());
    return words;

def keep_candidate_words(word: str):
    if(len(word) != WORD_LENGTH):
        return False;
    distinct_words = set(word);
    return len(distinct_words) == WORD_LENGTH;

def get_common_chars(word1: str, word2: str):
    chars1 = set(word1);
    chars2 = set(word2);
    return len(chars1.intersection(chars2));

def create_potential_matches(words):
    num_words = len(words);
    matches = [set() for _ in range(num_words)];
    for i in range(num_words - 1):
        for j in range(i + 1, num_words):
            num_common_chars = get_common_chars(words[i], words[j]);
            if (num_common_chars == 0):
                matches[i].add(j);
    
    return matches;

def find_sequence(words: list, matches: list, idx: int, candidates: set, current_set: list, remaining_words: int):
    if remaining_words == 1:
        print('candidates: ', [words[c] for c in candidates]);
        print([words[i] for i in current_set]);
        return True;
    remaining_candidates = candidates.intersection(matches[idx]);
    if (len(remaining_candidates) == 0):
        return False;
    current_set.append(idx);
    ans = False;
    for c in remaining_candidates:
        ans = ans or find_sequence(words, matches, c, remaining_candidates, current_set, remaining_words-1);
    current_set.pop();
    return ans;

def find_all_sequences(words: list, matches: list):
    ans = False;
    all_candidates = set([i for i in range(len(words))]);
    for i in range(len(words)):
        ans = ans or find_sequence(words, matches, i, all_candidates, [], SEQUENCE_LENGTH);
    return ans;

if __name__ == '__main__':
    print('beginning to find words');
    all_words = read_words();
    words = list(filter(keep_candidate_words, all_words));
    print('Total number of words: ', len(all_words), ', words after filtering: ', len(words));
    # TODO: remove the sampling after verification
    words = sample(words, 2000);
    matches = create_potential_matches(words);
    print([words[i] for i in matches[0]]);
    print('original word: ', words[0]);
    find_all_sequences(words, matches);