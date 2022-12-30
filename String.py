# Mendefinisikan string
string = "Hello World"

# Menghitung jumlah karakter dalam string
num_characters = len(string)

# Mengambil karakter terakhir dari string
last_character = string[len(string) - 1]

# Mengambil karakter pada indeks 2 sampai 4 (termasuk) dari string
substring = string[2:5]

# Menghilangkan spasi dari string
string_no_spaces = string.replace(" ", "")

# Mengubah string menjadi huruf besar
string_uppercase = string.upper()

# Mengubah string menjadi huruf kecil
string_lowercase = string.lower()

# Mengganti karakter 'H' dengan karakter 'J'
string_replaced = string.replace("H", "J")

# Print the results
print("The string '" + string + "' has " + str(num_characters) + " characters.")
print("The last character of the string '" + string + "' is '" + last_character + "'.")
print("The substring '" + substring + "' is the characters at indices 2 through 4 of the string '" + string + "'.")
print("The string '" + string_no_spaces + "' has had all spaces removed.")
print("The string '" + string_uppercase + "' has been converted to uppercase.")
print("The string '" + string_lowercase + "' has been converted to lowercase.")
print("The string '" + string_replaced + "' has had the character 'H' replaced with the character 'J'.")
