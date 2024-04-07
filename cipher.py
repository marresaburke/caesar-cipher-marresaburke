alphabet = {"a":"f", "b":"g", "c":"h", "d":"i", "e":"j", "f":"k", "g":"l", "h":"m", "i":"n" , "j":"o", "k":"p", "l":"q", "m":"r", "n":"s", "o":"t", "p":"u", "q":"v", "r":"w", "s":"x", "t":"y", "u":"z", "v":"a", "w":"b", "x":"c", "y":"d", "z":"e", " ":"$"}
user_input = input("Tell me a secret.")
user_input = user_input.lower()
secret_msg = ""

for letter in user_input: 
  secret_msg += alphabet[letter]
   
print("Your secret message is:",secret_msg)