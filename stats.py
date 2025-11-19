def get_word_count(book_text):
   return len(book_text.split())

def get_char_count(book_text):
   book_text = book_text.lower()
   char_counts = {}
   for char in book_text:
      if char in char_counts:
         char_counts[char] += 1
      else:
         char_counts[char] = 1
   
   return char_counts

def get_char_counts_list(char_counts : dict):
   char_counts_list = []
   alpha_char_keys = [key for key in char_counts.keys() if key.isalpha()]
   for alpha_char_key in alpha_char_keys:
      char_counts_list.append({"char": alpha_char_key, "num": char_counts.get(alpha_char_key)})
   
   return sorted(char_counts_list, key= lambda d: d["num"], reverse=True)
  
   
   

