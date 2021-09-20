import os
from datetime import datetime


def list_folder(path):
    # list all folders within given path
    folders = [x[0] for x in os.walk(path)]
    return folders


def loop_through_folders(folders):
    for folder in folders:
        rename, pattern = check_name(folder)
        if rename:
            try:
                rename_folder(folder, pattern)
            except FileNotFoundError:
                pass


def check_name(folder):
    # check if path contains one format from given patterns
    # I knew which formats to look for, therefore only 2 are listed
    # patterns can be adjusted as needed
    dirs = folder.split('\\')
    patterns = [
        '%d.%m.%Y',  # DD.MM.YYYY
        '%Y.%m.%d'   # YYYY.MM.DD
    ]

    for d in dirs[::-1]:  # reversed order just for time optimisation
        for pattern in patterns:
            try:
                if bool(datetime.strptime(d, pattern)):
                    return [True, pattern]
            except ValueError:
                pass

    return [False, False]


def rename_folder(folder, pattern):
    # if path contains date format I was looking for, it will adjust it to the correct (ISO) one
    dirs = folder.split('\\')
    new_dirs = []
    for d in dirs:
        try:
            if bool(datetime.strptime(d, pattern)):
                date_elements = datetime.strptime(d, pattern)
                new_date = date_elements.isoformat()[:10]
                new_dirs.append(new_date)
        except ValueError:
            new_dirs.append(d)

    new_path = os.path.join(*new_dirs).replace(':', ':\\')
    os.rename(folder, new_path)


if __name__ == '__main__':
    path = r''  # <-- provide path to the folder you wish to run through
    folders = list_folder(path)
    loop_through_folders(folders)
