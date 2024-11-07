def main():
    with open("github.com/mrskrei/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        word_taller(file_contents)
        char_dict = count_character(file_contents)
        report_sort(char_dict)
        print("--- End report ---")
        

def word_taller(file_contents):

    words = file_contents.split()
    word_count = len(words)
    print(f"Word count: {word_count}")

    
def count_character(text):

    lowered_char = text.lower()
    lowered_dict = {}

    for i in lowered_char:
        if i.isalpha():
            if i in lowered_dict:
                lowered_dict[i] += 1
            else:
                lowered_dict[i] = 1

    return lowered_dict


def report_sort(lowered_dict):
    sorted_list = list(lowered_dict.items())
    sorted_list.sort(key=lambda x: x[1], reverse=True)

    for char, count in sorted_list:
        print(f"The '{char}' character was found {count} times")


    
if __name__ == "__main__":
    main()
