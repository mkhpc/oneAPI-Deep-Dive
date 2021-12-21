import sys

fn = sys.argv[1]

with open(fn, 'r') as f:
    contents=f.read()

contents = '\n'.join(('%%writefile '+fn, contents))

get_ipython().set_next_input(contents)
