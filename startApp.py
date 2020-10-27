import os, shutil, time

fileTypes = dict()

fileTypes['image'] = ('.bmp', '.jpg', '.jpeg', '.gif', '.png', '.cr2')
fileTypes['audio'] = ('.mp3', '.wav')

def getUserHomeDir():
	return os.path.expanduser("~")

userDesktop = os.path.join(getUserHomeDir(),'Desktop')
userDownloads = os.path.join(getUserHomeDir(),'Downloads')
userImages = os.path.join(getUserHomeDir(),'Pictures')
userAudio = os.path.join(getUserHomeDir(),'Music')
#os.chdir(userDesktop)

def getFileList(iWalkDir):
    """
    

    Parameters
    ----------
    iWalkDir : TYPE
        DESCRIPTION.

    Returns
    -------
    yield the file type.

    """
    for wDir, wSubDirs, wFiles  in os.walk(iWalkDir):
        for wFile in wFiles:
            if os.path.splitext(wFile)[1] in fileTypes['image']:
                yield('image', os.path.join(wDir, wFile), wFile, wDir)
            if os.path.splitext(wFile)[1] in fileTypes['audio']:
                yield('audio', os.path.join(wDir, wFile), wFile, wDir)

def checkFile(iType, iFileTup):
    """
    Checks the type of the file and moves to the correct directory

    Parameters
    ----------
    iType : TYPE
         file type (image or audio).
    iFileTup : TYPE
        Tuple with the File info.

    Returns
    -------
    None.

    """
    if iFileTup[0] == iType:
        print(100*'-')
        print('the image \n\t' + iFileTup[2])
        print('from original directory \n\t'  + iFileTup[3])
        print('was moved to the new directory in \n\t' + userImages)
        if iType == 'image':
            dest = os.path.join(userImages, iFileTup[2])
        elif iType == 'audio':
            dest = os.path.join(userAudio, iFileTup[2])
        shutil.move(iFileTup[1], dest)    

while True:

    for wantFile in getFileList(userDesktop):
        checkFile('image', wantFile)
        checkFile('audio', wantFile)

    for wantFile in getFileList(userDownloads):
        checkFile('image', wantFile)
        checkFile('audio', wantFile)

    time.sleep(10)

