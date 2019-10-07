def LetterCapitalize(str):
  array_words = str.split()
  capWord = []
  for word in array_words:
    capWord.append(word.capitalize())
    phrase = " ".join(capWord)
  # code goes here
  return phrase

# keep this function call here 
print LetterCapitalize(raw_input())