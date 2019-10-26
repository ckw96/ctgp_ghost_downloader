# CTGP Ghost Downloader

## Description
Python script for mass downloading of ghosts from CTGP database. Currently only downloads world records.

## Usage
Ghost dataset specified by command line arguments. Up to two additional command line arguments permitted, one for track type ('nintendo' or 'ctgp'), one for cc ('150' or '200'). Order of inputs does not affect output. Defaults are 'nintendo' and '150'.

### Examples
1. `python getghosts.py` gets nintendo 150cc ghosts.
2. `python getghosts.py ctgp` gets ctgp 150cc ghosts.
3. `python getghosts.py ctgp 200` gets ctgp 200cc ghosts.
4. `python getghosts.py 150 ctgp` gets ctgp 150cc ghosts.

## Potential Errors
1. HTTP Error 504. Caused by connection isses, either your internet connection, the connection at the database, or anything in between.
2. HTTP Error 404. Caused by ghost not being in database.
3. OS Errors. Caused by bad filenames, usually due to mii names containing invalid characters. Some basic handling of invalid characters implemented.

### Known missing  Ghosts
1. GBA Bowser Castle 3 No Shortcut
2. Subspace Factory Shortcut

## Future Features
1. Vehicle search. Return BKTof ghosts using a specific vehicle.
2. GUI for easy selection
