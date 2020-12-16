from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open("Files/test.txt", mode="r") as my_file:
        # Be carefull, if you open the file just for writting, it will override your content
        text = my_file.read()
        translation = translator.translate(text)
        with open("Files/test-ja.txt", mode="w") as my_ja_file:
            my_ja_file.write(translation)
        print(translation)

except (FileNotFoundError, IOError) as err:
    print(f"Error found: {err}")
