def all_variants(text):
    for length in range(1, len(text) + 1):
        for j in text:
            current_text = text[text.index(j): text.index(j) + length]
            if len(current_text) < length:
                break
            yield current_text


a = all_variants("abc")
for i in a:
    print(i)
