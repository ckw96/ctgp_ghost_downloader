# CTGP Ghost Downloader

# Description
Python script for mass downloading of ghosts from CTGP database. Currently only downloads world records.

# Potential Errors
1. HTTP Error 504. Caused by connection isses, either your internet connection, the connection at the database, or anything in between.
2. HTTP Error 404. Caused by ghost not being in database.
3. OS Errors. Caused by bad filenames, usually due to mii names. Some basic handling of invalid characters implemented.

# Future Features
1. Vehicle search. Only return ghosts using a specific vehicle.
2. GUI for easy selection
