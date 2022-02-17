from pathlib import Path

myfile = 'files/new-sample.txt'

#looping a file line by line
with open(myfile, 'r') as f:
  for line in f:
    print(line[:-1])

#looping a file line by line
with open(myfile, 'r') as f:
  print(f.read())

# read a file via pathlib
p1 = Path('files/new-sample.txt')

#check a file exist or not
if p1.exists():
  print("File exists!!")
else :
  print("File not found.")

# extract file name 
print(p1.name)

# extract file stem 
print(p1.stem)

# extract file suffix 
print(p1.suffix)

# get list of files in dir
# iteam is of pathlib.posixpath type
p2 = Path('files/')
for iteam in p2.iterdir():
  print(iteam)