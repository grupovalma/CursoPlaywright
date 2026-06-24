# la r, despues del texto lee. y la w despues del texto escribe.
# Esto lo que hace es cambiar el orden del txt., poniendo en sentido contrario al usar reversed.



with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
