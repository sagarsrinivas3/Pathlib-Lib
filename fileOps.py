from pathlib import Path
from datetime import datetime as dt

def addPrefix(dir):
  rootDir = Path(dir)
  filePaths = rootDir.iterdir()
  for path in filePaths:
    newFileName = "new-"+ path.stem + path.suffix
    newFilePath = path.with_name(newFileName)
    path.rename(newFilePath)

def addPrefixMultipleDir(dir):
  rootDir = Path(dir)
  filePaths = rootDir.glob("**/*")
  for path in filePaths:
    if path.is_file():
      parentFolder = path.parts[1]   #path.parts => ("files1", "f1", "fruits.txt") 
      newFileName = parentFolder +"-"+path.name
      newFilePath = path.with_name(newFileName)
      path.rename(newFilePath)

def addPrefixMultipleDirLevels(dir):
  rootDir = Path(dir)
  filePaths = rootDir.glob("**/*")
  for path in filePaths:
    if path.is_file():
      parentFolder = path.parts
      subfolders = parentFolder[:-1]
      newFileName = "-".join(subfolders)+"-"+path.name
      newFilePath = path.with_name(newFileName)
      path.rename(newFilePath)
      
def getCreationDate(filepath):
  stats = filepath.stat()
  #st_atime - most recent timestamp file is accessed
  #st_mtime - timestamp when file is modifed
  #st_ctime - timestamp when file is created
  createdSec = stats.st_ctime
  createdTimestamp = convertSecToTimestamp(createdSec)
  return createdTimestamp

def convertSecToTimestamp(sec):
  timestamp = dt.fromtimestamp(sec)
  return timestamp
  
def getTimeStampOfFile(file):
  rootDir = Path(file)
  createdTimestamp = getCreationDate(rootDir)
  dateCreatedString = createdTimestamp.strftime("%Y-%m-%d-%H-%M-%S")
  return dateCreatedString

def addPrefixAsCreatedTimestampMultipleDirLevels(dir):
  rootDir = Path(dir)
  filePaths = rootDir.glob("**/*")
  for path in filePaths:
    if path.is_file():
      dateCreatedString = getTimeStampOfFile(dir)
      newFileName = dateCreatedString+"-"+path.name
      newFilePath = path.with_name(newFileName)
      path.rename(newFilePath)

# add prefix to all files in dir [ rename ]
#addPrefix('files/')

# add prefix to all files in mutiple dirs of adir [ rename ]
#addPrefixMultipleDir('files1/')

# add prefix to all files in mutiple dirs of a dir [ rename ]
#addPrefixMultipleDirLevels('files2/')

# rename a file with date of creation
#addPrefixAsCreatedTimestampMultipleDirLevels("Months/")