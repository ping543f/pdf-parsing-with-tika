# pdf-parsing-with-tika
simple pdf parsing to text using apache tika library
you need to have python and tika installed in your machine.
to install tika library, please follow https://pypi.org/project/tika/  site's instruction

to convert a pdf, open cmd/ windows power shell or terminal
then browse to the scripts folder
type python tika-parsing.py <file_name.pdf> <0/1>

for example to convert test.pdf file just type python tika-parsing.py test.pdf 1

0 is for silent conversion: it will just take the file and convert to text
1 is for viewing the parsed contents on the screen
