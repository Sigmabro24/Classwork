import json

line_count = 0
first_letter_words = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
first_letter_dict = {}
three_letter_words = ""


with open("three_letter.txt", "r") as file:
    for line in file:
         text_list = list(line)
         line_count += 1
         if len(line.strip()) == 3 and text_list[1] in alpha and text_list[2] in alpha and text_list[2] in alpha:
            three_letter_words += line.strip() + "\n"
            key = line.strip()[:2]
            if key in first_letter_dict:
                first_letter_dict[key].append(line.strip())
            else:
                first_letter_dict[key] = [line.strip()]
        # print(line.strip())# if line_count == 10000:
        #     break
print(first_letter_dict)
with open("first_letter_dict.json", "w") as file:
    json.dump(first_letter_dict, file, indent=4)