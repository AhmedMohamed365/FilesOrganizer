# program flow
# 1- ask user : manage or make files first?
# 2-manage :
# call manage and sort files to default folders
# 2-make files:
# choose the files he wants and make him choose type of files to be put in it
import os
import shutil
import pathlib

Videos = ['.mp4', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.wmv', '.mov', '.wmv',
          '.flv', '.swf', '.webm']
Audio = ['.wav', '.wave', '.aiff', '.pcm', '.au', '.flac', '.m4a', '.caf', '.wma', '.wmv', '.mp3', '.ogg', '.3gp',
         '.aac', '.mp3']
photos = ['.tif', '.jpg', '.png', '.gif']
compressed = ['.rar', '.zip']
Documents = ['.pdf', '.doc', '.txt', '.docx', '.odt', '.html', '.xlsx', '.pptx']
cDir = os.getcwd()       # gets the current folder

# ------------------------------------------------------------------------
extension = ""


def check_audio(audio):
    for item in Audio:
        for item1 in audio:
            if item == item1:
                return item1
            else:
                continue


def check_video(video):
    for item in Videos:
        for item1 in video:
            if item == item1:
                return item1
            else:
                continue


def check_compressed(compressedfile):
    for item in compressed:
        for item1 in compressedfile:
            if item == item1:
                return item1
            else:
                continue


def check_document(document):
    for item in Documents:
        for item1 in document:
            if item == item1:
                return item1
            else:
                continue


def check_photo(photo):
    for item in photos:
        for item1 in photo:
            if item == item1:
                return item1
            else:
                continue


def emptyFolders(dir):
    empty_dirs = []
    for i in dir:
        if os.path.exists(i) and os.path.isdir(i):
            if not os.listdir(i):
                print("Directory {} is empty".format(i))
                empty_dirs.append(i)
    if len(empty_dirs) == 0:
        None
    else:
        return empty_dirs


def manage_empty(emptyFolders):
    if emptyFolders is None:
        return 0
    delete = input("Enter 1 to delete all empty folders or 2 to select what you want or any other key to keep them")
    if delete.casefold() == "1":
        for i in range(len(emptyFolders)):
            try:
                os.removedirs(emptyFolders[i])
            except FileNotFoundError:
                None
    elif delete.casefold() == "2":
        deleted_folders = []
        deleted_folders = input("Type name of folders you want to remove from these:" + "  ".join(emptyFolders)).split()
        for folder in range(len(emptyFolders)):
            os.removedirs(deleted_folders[folder])


def manage():
    autoFolders = ['Audio', 'Videos', 'Photos', 'Compressed', 'others', 'Documents']
    for root, subDirs, files in os.walk(cDir):
        deletedFolders = emptyFolders(subDirs)
        manage_empty(deletedFolders)
        for file in files:
            oldPath = os.path.join(root, file)
            extenstion = pathlib.Path(oldPath).suffix
            try:
                if extenstion in Audio:
                    if not os.path.isdir('Audio'):
                        os.makedirs('Audio')
                    shutil.move(oldPath, cDir + "\\Audio")
                # this to check background images
                if extenstion in Videos:
                    if not os.path.isdir('Videos'):
                        os.makedirs('Videos')
                    shutil.move(oldPath, cDir + "\\Videos")
                # this to check compreessed files
                if extenstion in compressed:
                    if not os.path.isdir('Compressed'):
                        os.makedirs('Compressed')
                    shutil.move(oldPath, cDir + "\\Compressed")
                if extenstion in photos:
                    if not os.path.isdir('Photos'):
                        os.makedirs('Photos')
                    shutil.move(oldPath, str(cDir) + "\\photos")
                if extenstion in Documents:
                    if not os.path.isdir('Documents'):
                        os.makedirs('Documents')
                    shutil.move(oldPath, cDir + "\\Documents")
                else:
                    continue

            except:
                None


newFolders = []

audioFormats = ''
videoFormats = ''
compressedFormats = ''
photoFormats = ''
documentFormats = ''

# path of formats by user

audiopath = ''
photopath = ''
videopath = ''
compressedPath = ''
documentpath = ''


def sort_compressed():
    print(
        "Enter formats for types of compressed files you want to put it like these ---> Formats:" + " ".join(
            compressed))
    print("put it like : .zip,.rar")
    global compressedFormats
    compressedFormats = list(input().split(','))
    if check_compressed(compressedFormats) in compressed:
        compressedFolder = input("Type foldername from these to put these extensions in folder:" + " ".join(newFolders))

    if compressedFolder in newFolders:
        global compressedPath
        compressedPath = cDir + '\\{}'.format(compressedFolder)
        return compressedPath


def sort_photos():
    print("Enter formats for types of audio files you want to put it like these ---> Formats:" + " ".join(photos))
    print("put it like : .jpg,.png")
    global photoFormats
    photoFormats = list(input().split(','))
    if check_photo(photoFormats) in photos:
        photoFolder = input("Type foldername from these to put these extensions in folder:" + " ".join(newFolders))
        if photoFolder in newFolders:
            global photopath
            photoPath = cDir + '\\{}'.format(photoFolder)
            return photoPath


def sort_videos():
    print("Enter formats for types of video files you want to put it like these ---> Formats:" + " ".join(Videos))
    print("put it like : .mp4,.mkv")
    global videoFormats
    videoFormats = list(input().split(','))
    if check_video(videoFormats) in Videos:
        videoFolder = input("Type foldername from these to put these extensions in folder:" + " ".join(newFolders))

        if videoFolder in newFolders:
            global videopath
            videoPath = cDir + '\\{}'.format(videoFolder)
            return videoPath


def sort_audio():
    print("Enter formats for types of audio files you want to put it like these ---> Formats:" + " ".join(Audio))
    print("put it like : .mp3,.3gp")
    global audioFormats
    audioFormats = list(input().split(','))
    if check_audio(audioFormats) in Audio:
        audioFolder = input(
            "Type foldername from these to put these extensions in folder--" + "  ".join(newFolders)).strip()

        if audioFolder in newFolders:
            global audiopath
            audiopath = cDir + '\\{}'.format(audioFolder)
            return audiopath


def sort_documents():
    print(
        "Enter formats for types of documents files you want to put it like these ---> Formats:" + " ".join(Documents))
    print("put it like : .pdf,.XLSX,.docx")
    global documentFormats
    documentFormats = list(input().split(','))
    if check_document(documentFormats) in Documents:
        documentFolder = input("Type foldername from these to put these extensions in folder:" + " ".join(newFolders))

    if documentFolder in newFolders:
        global documentpath
        documentpath = cDir + "\\{}".format(documentFolder)
        return documentpath


def sort_extensions():
    print("choose what you want to arrange:")
    your_choice = input("do you want to arrange audio files?---> answer yes or no: ")
    if your_choice.casefold() == "yes":
        global audiopath
        audiopath = sort_audio()
    elif your_choice.casefold() == "no":
        print("ok")
    else:
        print("wrong entry")
        # ---------------
    your_choice = input("do you want to arrange compressed files?---> answer yes or no: ")
    if your_choice.casefold() == "yes":
        global compressedPath
        compressedPath = sort_compressed()
    elif your_choice.casefold() == "no":
        print("ok")
    else:
        print("wrong entry")
        # -----------
    your_choice = input("do you want to arrange photos files?---> answer yes or no: ")
    if your_choice.casefold() == "yes":
        global photopath
        photopath = sort_photos()
    elif your_choice.casefold() == "no":
        print("ok")
    else:
        print("wrong entry")
        # ---------
        your_choice = input("do you want to arrange video files?---> answer yes or no: ")
        if your_choice.casefold() == "yes":
            global videopath
            videopath = sort_videos()
        elif your_choice.casefold() == "no":
            print("ok")
        else:
            print("wrong entry")
        # ------
    your_choice = input("do you want to arrange document files?---> answer yes or no: ")
    if your_choice.casefold() == "yes":
        global documentpath
        documentpath = sort_documents()
    elif your_choice.casefold() == "no":
        print("ok")
    else:
        print("wrong entry")


def askForFolders():
    global oldPath, newFolders
    add = True
    newFolders = input("what folders do you want to create? ").split()
    while add is True:
        ask = input("do you want to add something else?")
        if ask.casefold() == "no":
            add = False
            print("ok")
        elif ask.casefold() == "yes":
            newFolders += input("type another name here : ").split()
        else:
            print("you entered invalid entry")
        # ----------------------------------------------
        # function to find the files and put it to folders
        for i in range(len(newFolders)):
            try:
                os.makedirs('{}'.format(newFolders[i]))
            except FileExistsError:
                print("some files already exists")
                continue

    print("these are your folders choose type of files to be put in these folders: " + "  ".join(newFolders))
    # this fn choose what type of files and gets their folder address

    sort_extensions()
    # this loop goes for the main folder then files and other subfolders in it
    deletedFolders = []
    ignore_folder = []
    exclude_folder = []
    for root, subDirs, files in os.walk(cDir):
        deletedFolders = emptyFolders(subDirs)
        manage_empty(deletedFolders)
        dirname = os.path.basename(root)
        if dirname in ignore_folder:
            if root == cDir:
                None
            else:
                continue
        else:
            None
        try:
            for file in files:
                oldPath = os.path.join(root, file)
                extenstion = pathlib.Path(oldPath).suffix
                if extenstion in audioFormats:
                    shutil.move(oldPath, audiopath)
                elif extenstion in videoFormats:
                    shutil.move(oldPath, os.path.join(videopath, file))
                elif extenstion in compressedFormats:
                    shutil.move(oldPath, compressedPath)
                elif extenstion in photoFormats:
                    shutil.move(oldPath, photopath)
                elif extenstion in documentFormats:
                    shutil.move(oldPath, documentpath)
                else:
                    None
        except:
            if oldPath == audiopath:
                print("File is aleardy moved to audiopath")
            elif oldPath == videopath:
                print("File is aleardy moved to video path")
            elif oldPath == compressedPath:
                print("File is aleardy moved to compressed path")
            elif oldPath == photopath:
                print("File is aleardy moved to photo path")
            elif oldPath == documentpath:
                print("File is aleardy moved to document path")

            ask_subfolder = input("Do you want to arrange these folders?: " + " ".join(subDirs))
            if ask_subfolder.casefold() == "yes":
                exclude_folder = input("do you want to exclude anyfolders from them?\n")
                if exclude_folder.casefold() == 'yes':
                    exclude_folder = input("Type them here : ").split()
                    ignore_folder.extend(exclude_folder)

            elif ask_subfolder.casefold() == "no":
                ignore_folder.extend(subDirs)
            else:
                print("type yes or no please")
                ask_subfolder = input()


# ask for how many folders and put it in list
print("Hi, This is Files Manager program if you want auto manage\n "
      "type '1' or type '2' for modefied Managment\n "
      "You can create folders then choose any extenstion you want"
      "?")


def askFirst():
    choose = input()
    if choose.__contains__("1"):
        manage()
    elif choose.__contains__("2"):

        askForFolders()
    else:
        print("you entered wrong entry,try again ")
        askFirst()


# program begins
askFirst()