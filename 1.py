results = []

def brute_force_recursive(charset, password, max_length):
    if len(password) == max_length:
        results.append(password)
        return

    for char in charset:
        brute_force_recursive(charset, password + char, max_length)

def brute_force_password_generator(charset, min_length, max_length):
    for length in range(min_length, max_length + 1):
        brute_force_recursive(charset, "", length)
    return results

if __name__ == "__main__":
    # import string
    # charset = string.ascii_lowercase
    charset = "abcdefghijklmnopqrstuvwxyz"
    min_length = 1
    max_length = 6

    passwords = brute_force_password_generator(charset, min_length, max_length)
    print(passwords)
