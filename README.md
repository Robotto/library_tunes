library_tunes
=============

A sound installation for Internet Week Denmark.

A Python script uses library transaction data from odaa.dk to play sound samples, and make "the sound of the libraries"

The transaction data is from all 19 of the Aarhus Public Libraries.

Historical data from exactly 1 year ago is used, because redundancy.

A utlity script called toplister.py counts transactions per library and lists them starting with the library with the highest number of transactions. 

A utility script called instancecounter.py scans the input data for the highest number of simultaneous transactions.

A utility script called fileprep.py helps format the data, to ease the load on the Raspberry pie which will run the library_tunes script.


Enjoy
~Robotto
