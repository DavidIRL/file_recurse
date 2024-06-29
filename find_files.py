import os

#root = input('What directory do you wish to search?\n')
#ext = input('What file extension do you wish to find?\n')

def find_files(ext, root):
    if root not in os.listdir():
        raise FileExistsError("Target not in current working directory")
    if not os.path.isdir(root):
        raise FileExistsError("Target is not a folder/directory")
    return list_files(ext, root)
    

def list_files(ext, root):
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
            file_paths.extend(list_files(ext=ext, root=f'{root}/{item}'))

    return file_paths
        
if __name__ == '__main__':
    print(find_files(input("What file extension do you wish to find?\n"),
                     input("What directory do you want to search?\n")))
