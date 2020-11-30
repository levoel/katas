def number(lines):
    x = 1
    for i in range(len(lines)):
        lines[i] = str(x) + ": " + lines[i]
        x+=1
    return lines

# OR

def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
