# CTGP Ghost Downloader

## Description
Python script for mass downloading of ghosts from CTGP database. Currently only downloads world records.

## Usage
Ghost dataset specified by command line arguments. Use '200' for 200cc and 'ctgp' for ctgp tracks. Vehicle type can be specified by adding either 'karts' or 'bikes' to the command line arguments, adding 'karts' will ignore the 'bikes' argument. Order of inputs does not affect output.

### Examples
1. `python getghosts.py` gets nintendo 150cc ghosts.
2. `python getghosts.py ctgp` gets ctgp 150cc ghosts.
3. `python getghosts.py ctgp 200` gets ctgp 200cc ghosts.
4. `python getghosts.py ctgp` gets ctgp 150cc ghosts.
5. `python getghosts.py karts` gets nintendo 150cc kart ghosts.
6. `python getghosts.py ctgp 200 bikes` gets ctgp 200cc bike ghosts.

## Potential Errors
1. HTTP Error 504. Caused by connection isses, either your internet connection, the connection at the database, or anything in between.
2. HTTP Error 404. Caused by ghost not being in database.
3. OS Errors. Caused by bad filenames, usually due to mii names containing invalid characters. Some basic handling of invalid characters implemented.
