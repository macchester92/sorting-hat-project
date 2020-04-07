# Sorting Hat App
---------------
Simple utility that _recursively_ searches for duplicates inside a folder (and a folder inside that folder, and so on. Recursively!). It uses Blake2b hashing algorithm to guickly generate checksums of the files and then asks a user to review or delete duplicates. **NOTE: be careful when deleting files - this action might cause losing data permanently!** Always make sure you reviewed duplicates before deleting.
_______________
Another feature implemented in this app is file system watcher. It automatically tracks changes in assigned directory (adding new files to the directory) and sorts files in new directories, according to their extension. Very handy sorter for people whose machines are a bit messy.