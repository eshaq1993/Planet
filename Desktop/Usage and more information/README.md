This include instruction on how to run the setup.sh and what it does, what to expect as a user.

To run the setup.sh, first we create a file to hold our scipts by using nano. ex: nano name_setup.sh.

Then, we can tell the user what are the commends by using echo. ex: echo "making directory"

We can make as many scripts as possiple inside the setup.sh file which can be processed in the terminal. 

The scripts used in the setup.sh I made are the following:
1) making directory: mkdir HCEPDB

2) downloading file: curl -O http://faculty.washington.edu/dacb/HCEPDB_moldate.zip

3) unzipping file: unzip HCEPDB_moldate.zip 

 
