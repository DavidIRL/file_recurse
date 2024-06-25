import os

def find_files(root, ext):
    if root not in os.listdir():
        return FileExistsError("Target not in current working directory")
    if not os.path.isdir(root):
        return FileExistsError("Target is not a folder/directory")
    return list_files(root, ext)
    

def list_files(root, ext):
    if len(os.listdir(root)) == 0:
        return []
    
    current_dir = os.listdir(root)
    file_paths = []
    
    for item in current_dir:
        if item.endswith(ext):
            file_paths.append(f'{root}/{item}')
        elif os.path.isfile(item):
            break
        elif os.path.isdir(f'{root}/{item}'):
            file_paths.extend(list_files(root=f'{root}/{item}', ext=ext))

    if len(file_paths) > 0:
        return file_paths
    else:
        return FileExistsError(f"No files with a {ext} extension was found within the {root} directory tree")



print(find_files(input('What directory do you wish to search: '),
                 input('What file extension do you wish to find: '))
