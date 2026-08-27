

def open_text_and_replace(path, old_str, new_str):
    new_content = ""
    try:
        with open(path, 'r', encoding="utf-8") as f:
            new_content += (f.read()).replace(old_str, new_str)
            print(new_content)
    except IOError as e:
        print(e)
    try:
        with open(path, 'w', encoding="utf-8") as f:
            if new_content != "":
                f.write(new_content)
                print("write ok")
    except IOError as e:
        print(e)
