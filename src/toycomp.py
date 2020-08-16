import sys, os, re


#expected form of c program
source_re = r"int main\s*\(void\)\s*{\s*return\s+(?P<ret>[0-9]+)\s*;\s*}" 

assembly_format = """
    .globl _main
_main:
    movl    ${}, %eax
    ret
"""


source_file = sys.argv[1]
assembly_file = os.path.splitext(source_file)[0] + ".s"

with open(source_file, 'r') as infile, open(assembly_file, 'w') as outfile:
    source = infile.read().strip()
    match = re.match(source_re, source)

    retval = match.group('ret')
    outfile.write(assembly_format.format(retval))
    



