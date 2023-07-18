matrix = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

num_rows = len(matrix)
num_columns = len(matrix[0])
message = ""

for col in range(num_columns):
    alpha_chars = [matrix[row][col] for row in range(num_rows) if matrix[row][col].isalpha()]
    if alpha_chars:
        message += "".join(alpha_chars)

print("Decrypted message:")
print(message)
