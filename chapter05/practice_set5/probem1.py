# Write a program to create dictionary of `Nepali words` 
# with the values as their `English translation`. Provide user an option to look it up!

words = {
    "Sahayog" : "help",
    "biralo" : "cat",
    "khushi" : "happy",
    "daro" : "strong",
    "sano" : "small",
    "thulo" : "big"
}

word = input("Enter the word you want the meaning of: ").strip()

print(f"The meaning of {word} in english is {words[word]}")