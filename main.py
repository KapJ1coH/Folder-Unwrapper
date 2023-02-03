import os
import shutil


folder_to_unpack = 'path'


def list_dir(path):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        print(f'FileNotFoundError: [WinError 3] The system cannot find the path specified: {path}')



def go_through_folder(parent_path,  search_depth,  current_depth=0, previous_combined_path='',):
    if previous_combined_path == '':
        previous_combined_path = parent_path
    folder = list_dir(previous_combined_path)

    for path in folder:
        combined_path = combine_path_file(previous_combined_path, path)
        if is_file(combined_path) and current_depth != search_depth:
            print(combined_path)
            print(parent_path)
            copy_file_to_parent(combined_path, parent_path)
        elif is_file(combined_path):
            continue
        elif list_dir(combined_path):
            if current_depth < search_depth:
                go_through_folder(combined_path, search_depth, current_depth + 1, combined_path)
            else:
                go_through_folder(parent_path, search_depth, current_depth + 1, combined_path)
        if not is_file(combined_path) and current_depth == search_depth:
            shutil.rmtree(combined_path)


def combine_path_file(path, file):
    return f'{path}/{file}'


def copy_file_to_parent(source, destination):
    shutil.copy2(source, destination)


def is_file(filename):
    return os.path.isfile(filename)


def make_a_copy(path):
    count = 1
    while True:
        try:
            shutil.copytree(path, f'{path}({count})')
        except FileExistsError:
            count += 1
        except FileNotFoundError:
            print('File not found!')
            exit()
        else:
            break


def main(path, depth, copy):
    if copy:
        make_a_copy(path)
    go_through_folder(path, depth)


main(folder_to_unpack, depth=1, copy=True)


