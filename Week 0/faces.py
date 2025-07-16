def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(",  "🙁")

    return emoticon

emoticon = input("")
converted_emoticon = convert(emoticon)
print(converted_emoticon)
