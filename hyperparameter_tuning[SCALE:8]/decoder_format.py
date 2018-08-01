text=input()
try:
    text.decode(encoding='base64')
except:
    try:
        text.decode(encoding='latin-1')

    except:
        try:
            text.decode(encoding='windows-1252')

        except:
            try:
                print("Unable to entirely decode in latin or utf-8, will replace error characters with '?'")
                text.decode(encoding='utf-8', errors="replace")
            except:
                print(text)
                text = None
