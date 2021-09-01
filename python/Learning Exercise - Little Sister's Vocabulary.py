'''
1. Add a prefix to a word
One of the most common prefixes in English is un, meaning "not". In this activity, your sister needs to make negative, or "not" words by adding un to them.

Implement the add_prefix_un() function that takes word as a parameter and returns a new un prefixed word:

>> add_prefix_un("happy")
'unhappy'

>> add_prefix_un("manageable")
'unmanageable'
2. Add prefixes to word groups
There are four more common prefixes that your sister's class is studying: en (meaning to 'put into' or 'cover with'), pre (meaning 'before' or 'forward'), auto (meaning 'self' or 'same'), and inter (meaning 'between' or 'among').

In this exercise, the class is creating groups of vocabulary words using these prefixes, so they can be studied together. Each prefix comes in a list with common words it's used with. The students need to apply the prefix and produce a string that shows the prefix applied to all of the words.

Implement the make_word_groups(<vocab_words>) function that takes a vocab_words as a parameter in the following form: [<prefix>, <word_1>, <word_2> .... <word_n>], and returns a string with the prefix applied to each word that looks like: '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'.

>> make_word_groups(['en', 'close', 'joy', 'lighten'])
'en :: enclose :: enjoy :: enlighten'

>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
'pre :: preserve :: predispose :: preposition'

>> make_word_groups(['auto', 'didactic', 'graph', 'mate'])
'auto :: autodidactic :: autograph :: automate'

>> make_word_groups(['inter', 'twine', 'connected', 'dependant'])
'inter :: intertwine :: interconnected :: interdependent'
3. Remove a suffix from a word
ness is a common suffix that means 'state of being'. In this activity, your sister needs to find the original root word by removing the ness suffix. But of course there are pesky spelling rules: If the root word originally ended in a consonant followed by a 'y', then the 'y' was changed to to 'i'. Removing 'ness' needs to restore the 'y' in those root words. e.g. happiness --> happi --> happy.

Implement the remove_suffix_ness(<word>) function that takes in a word str, and returns the root word without the ness suffix.

>> remove_suffix_ness("heaviness")
'heavy'

>> remove_suffix_ness("sadness")
'sad'
4. Extract and transform a word
Suffixes are often used to change the part of speech a word has. A common practice in English is "verbing" or "verbifying" -- where a adjective becomes a verb by adding an en suffix.

In this task, your sister is going to practice "verbing" words by extracting an adjective from a sentence and turning it into a verb. Fortunately, all the words that need to be transformed here are "regular" - they don't need spelling changes to add the suffix.

Implement the noun_to_verb(<sentence>, <index>) function that takes two parameters. A sentence using the vocabulary word, and the index of the word, once that sentence is split apart. The function should return the extracted adjective as a verb.

>> noun_to_verb('I need to make that bright.', -1 )
'brighten'

>> noun_to_verb('It got dark as the sun set.', 2)
'darken'
'''

'''this is the exercise strings.py'''


def add_prefix_un(word):
    '''

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    '''
    return "un" + word


def make_word_groups(vocab_words):
    '''

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    '''
    prefix = [vocab_words[0] + prefix for prefix in vocab_words if prefix != vocab_words[0]]
    return vocab_words[0] + " :: " + ' :: '.join(prefix)


def remove_suffix_ness(word):
    '''

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    '''
    word = list(word.removesuffix("ness"))
    if word[len(word) - 1] == "i":
        word[len(word) - 1] = "y"
    return "".join(word)


def noun_to_verb(sentence, index):
    '''

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    '''
    return sentence.split()[index].removesuffix(".").lower() + "en"

make_word_groups(['en', 'close', 'joy', 'lighten'])
remove_suffix_ness("heaviness")
remove_suffix_ness("sadness")
noun_to_verb('I need to make that bright.', -1 )
noun_to_verb('It got dark as the sun set.', 2)

