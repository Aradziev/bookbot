file_name = "books/frankenstein.txt"
with open(file_name) as f:
    file_contents = f.read()
    word_count = len(file_contents.split())
    count_dict = {}
    file_contents = file_contents.lower()

    for letter in file_contents:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1

    count_list = list(count_dict.items())

    def num_value(tup):
        return tup[1]

    count_list.sort(key=num_value, reverse=True)

    alpha_count_list = []
    for tt in count_list:
        if tt[0].isalpha():
            alpha_count_list.append(tt)

    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print()
    for tt in alpha_count_list:
        print(f"The '{tt[0]}' character was found \
             {tt[1]} times")
    print("--- End report ---")
