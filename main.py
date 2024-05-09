def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def word_count(words):
        separate_words = words.split()
        return len(separate_words)
    
    def letters_count(words):
        letter_dict = {}
        for letter in words:
            lower_case_letter = letter.lower()
            if lower_case_letter in letter_dict:
                letter_dict[lower_case_letter] += 1
            elif lower_case_letter.isalpha() == True:
                letter_dict[lower_case_letter] = 1
        return letter_dict
    
    def create_list_of_dict(dict):
        list_of_dictionaries = []
        for key in dict:
            new_dictionary = {"letter" : key, "number_of" : dict[key]}
            list_of_dictionaries.append(new_dictionary)
        return list_of_dictionaries
    
    def sort_on(dict):
        return dict["number_of"]
   
    count = word_count(file_contents)
    print(f"--- Begin report of books/frankenstein.txt ---\n{count} words found in the document\n")
    letters_count(file_contents)
    dictionary = letters_count(file_contents)
    list_of_dict = create_list_of_dict(dictionary)
    list_of_dict.sort(reverse=True, key=sort_on)
    for dict in list_of_dict:
        print(f"The '{dict['letter']}' character was found {dict['number_of']} times")
    print("--- End report ---")
main()