def duplicate_count(text):
    text = text.lower()
    count = 0
    while len(text) > 1:
        i = text[0]
        for j in range(1, len(text)):
            if i == text[j]:
                count += 1
                break
        text = text.replace(i, '')
    return count

# OR

def duplicate_count(text):
  return len([c for c in set(text.lower()) if text.lower().count(c)>1])
