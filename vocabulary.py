from talon.engine import engine
add_words = [
    # r'testing word add 1\\pronounced like this',
    # r'testing word add 2\\pronounced like this',
    r'illumina',

]
print(engine.cmd('w.add', words=add_words))