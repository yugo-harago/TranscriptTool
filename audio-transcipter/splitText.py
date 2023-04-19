import re
import os
from pathlib import Path

result = []


def split_text(text):
    delimiter_regex = re.compile(r"([。、！？\n\{\}\[\]「」])")
    splitted_text = list(
        filter(lambda chunk: chunk.strip() != "", re.split(delimiter_regex, text))
    )

    return splitted_text


def main():
    input_file = Path("./public/DazaiOsamu_Uso.txt")
    output_file = Path("./public/DazaiOsamu_Uso.html")

    try:
        with input_file.open("r", encoding="utf-8") as file:
            data = file.read()
        
        data = data.replace('\n','<br>')

        splitted = split_text(data)
        for word in splitted:
            result.append(
                f'<span click="wordClick(\'{word}\')">{word}</span>'
            )

        output_content = "".join(result)
        print(output_content)

        with output_file.open("w", encoding="utf-8") as file:
            file.write(output_content)

        print("The file has been saved!")

    except Exception as err:
        print("Error reading or writing file:", err)


if __name__ == "__main__":
    main()
