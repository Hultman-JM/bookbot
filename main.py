def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)

    #report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    sorted_letters = sorted(letter_count.items(), key=lambda x:x[1], reverse=True)
    sorted_letters = dict(sorted_letters)
    for letter in sorted_letters:
        print(f"the {letter} character was found {sorted_letters[letter]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowercase_text = text.lower()
    letters = {}

    for letter in set(lowercase_text):
        if letter.isalpha():
            letters[letter] = lowercase_text.count(letter)
    return letters
main()