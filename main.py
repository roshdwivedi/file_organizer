import os   
import shutil

def get_source_dir():
    source = input("Enter path to the target directory: ")
    if not os.path.isdir(source):
        print("Error : The given path is not valid, Please try again with valid path")
        return None
    else:
        return source

def file_organize():
    source = get_source_dir()
    if source is None:
        return

    file_ext = set()

    for name in os.listdir(source):
        if os.path.isfile(os.path.join(source,name)):
            file_ext.add(os.path.splitext(name)[1].lower())
    for ext in file_ext:
        os.makedirs(os.path.join(source,ext.strip('.')),exist_ok=True)
    
    for name in os.listdir(source):
        if os.path.isfile(os.path.join(source,name)):
            file_ex = os.path.splitext(name)[1].lower()
            target = os.path.join(source,file_ex.strip('.'))
            shutil.move(os.path.join(source,name), os.path.join(target, name))


file_organize()