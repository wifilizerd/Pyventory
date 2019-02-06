# Pyventory
Python based Inventory Assistant.

You MUST have access to export a CSV record from the database you are using.

SETUP:
    1. Download Master-Pyventry.zip and extract all files, pyventory only requiers that python 2.7 (NOT Python 3) is installed.
    2. Copy the export of inventory file into the pyventory folder (Must be a CSV file).
    3. run pyventory.

Current Features:
    1. Enter/Scan barcodes and pyventory will use the inventory file provided to check if the barcode is in the list. 

    2. Items that were not found in the inventory list Will show in Red,

    3. Export a list of all items that have not been scanned, and any items that were not found. 

Changelog:
0.6.4 (coming Soon) - Updating to Python 3.7...

0.6.3 - Fully updated UI and scan featuers, Added the Progress page that will show you the current completion in each room from your inventory. includes room check and included documentation in the Master file.

0.6.1 - Added room feature that allows user to search only barcodes that are located in a specified room, pyventory will if the barcode is found and room is incorrect will shoe current known data and note the new room number for latter update.
0.6 - after months of testing and reworking pyventory is now ready to be posted on GitHub,


Warrenty:
THERE IS NONE, by using this probram you agree that there is no warrenty and that this program is free to use at your own risk.
this is all my personal time, so that means that any bug reports will take some time to get to.

Tested On:
Windows 10 with python 2.7,
Macos X 10.12 with python 2.7

Enjoy!
