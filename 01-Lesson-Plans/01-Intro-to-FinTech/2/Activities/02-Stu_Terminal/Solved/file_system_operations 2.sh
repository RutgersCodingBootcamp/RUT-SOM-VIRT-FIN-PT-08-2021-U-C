# This bash shell script performs the following file system operations.

# Check current directory.
pwd

# Navigate to your Desktop.
cd ~/Desktop

# Confirm your current working directory is at the Desktop.
pwd

# Create a folder called `Terminal-Test`.
mkdir Terminal-Test

# Navigate into the folder.
cd Terminal-Test

# Inside `Terminal-Test`, create two folders: `Folder_1` and `Folder_2`.
mkdir Folder_1
mkdir Folder_2

# Navigate into `Folder_1`.
cd Folder_1

# Create an empty file named `terminal.txt`.
touch terminal.txt

# Edit the file `terminal.txt` with VS Code.
code terminal.txt

# Read the file `terminal.txt` and output the results to the console.
cat terminal.txt

# Navigate back one level (to the root of the `Terminal-Test` folder).
cd ..

# Copy the file `terminal.txt` into `Folder_2`.
cp Folder_1/terminal.txt Folder_2/

# Delete the folder `Folder_1` and its contents.
rm -r Folder_1

# Rename the folder `Folder_2` to `Hello_World`.
mv Folder_2 Hello_World

# List the contents of the root of the `Terminal-Test` folder.
ls