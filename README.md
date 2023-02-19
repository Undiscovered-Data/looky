# looky
Peek into a file, even an extremly large one. Safer than dd, you won't accidentally destroy your filesystem. It can hadle files that are too big for your browser, text editor, vim, etc.

Type "looky -h" for help.
Type "looky -v" for version number.
Type "looky number file" to print number of bytes to stdout, starting from begining of file.
E.G. "looky 50 myfile.txt" will print the first 50 bytes of file myfile.txt.
Type "looky number1 number2 file" to print bytes starting at number1 and ending at number2.
E.G. "looky 50 100 myfile.txt" will print bytes 50-100 of myfile.txt
