import os
DEFAULT_DIRECTORY = r'D:\Desktop\ШАГ\Занятия\first_try_git_project\dir'

files = [os.path.join(DEFAULT_DIRECTORY, f) for f in os.listdir(DEFAULT_DIRECTORY)]
print(files)


def all_items_are_items():
    return all([os.path.isfile(f) for f in files])


def get_first_index():
    for i, f in enumerate(files):
        if os.path.isdir(f):
            return i
    return -1


while True:
    index = get_first_index()
    if index == -1:
        break
    current = files[index]
    if len(os.listdir(current)) == 0:
        files = files[:index] + files [index+1:]
    else:
        files_current = [
            os.path.join(current, f)
            for f in os.listdir(current)
        ]
        files[index:index+1] = files_current
    print(files)