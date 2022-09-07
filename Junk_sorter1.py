"""
A simple junk sorter program. Full description will be added later.
look at the line #365 ... "D:\\tests" !!!!!
"""
import sys
import pathlib
import shutil
'''!!! ftom where adding 1. to all obj? and when?!!!'''
main_directories = {'images', 'documents', 'audio', 'video', 'archives'}
all_subdirectories = []

normalization_scheme = {'А': 'A',
                        'Б': 'B',
                        'В': 'V',
                        'Г': 'H',
                        'Д': 'D',
                        'Е': 'E',
                        'Ё': 'E',
                        'Ж': 'ZH',
                        'З': 'Z',
                        'И': 'Y',
                        'Й': 'Y',
                        'К': 'K',
                        'Л': 'L',
                        'М': 'M',
                        'Н': 'N',
                        'О': 'O',
                        'П': 'P',
                        'Р': 'R',
                        'С': 'S',
                        'Т': 'T',
                        'У': 'U',
                        'Ф': 'F',
                        'X': 'KH',
                        'Ц': 'TS',
                        'Ч': 'CH',
                        'Ш': 'SH',
                        'Щ': 'SHCH',
                        'Ы': 'I',
                        'Э': 'E',
                        'Ю': 'YU',
                        'Я': 'YA',
                        'Ґ': 'G',
                        'Є': 'IE',
                        'Ї': 'YI',
                        'а': 'a',
                        'б': 'в',
                        'в': 'v',
                        'г': 'h',
                        'д': 'd',
                        'е': 'e',
                        'ё': 'e',
                        'ж': 'zн',
                        'з': 'z',
                        'и': 'y',
                        'й': 'y',
                        'к': 'к',
                        'л': 'l',
                        'м': 'm',
                        'н': 'n',
                        'о': 'o',
                        'п': 'p',
                        'р': 'r',
                        'с': 's',
                        'т': 't',
                        'у': 'u',
                        'ф': 'f',
                        'x': 'kh',
                        'ц': 'ts',
                        'ч': 'ch',
                        'ш': 'sн',
                        'щ': 'shch',
                        'ы': 'i',
                        'э': 'e',
                        'ю': 'yu',
                        'я': 'ya',
                        'ґ': 'g',
                        'є': 'ie',
                        'ї': 'yi',
                        'A': 'A',
                        'B': 'B',
                        'C': 'C',
                        'D': 'D',
                        'E': 'E',
                        'F': 'F',
                        'G': 'G',
                        'H': 'H',
                        'I': 'I',
                        'J': 'J',
                        'K': 'K',
                        'L': 'L',
                        'M': 'M',
                        'N': 'N',
                        'O': 'O',
                        'P': 'P',
                        'Q': 'Q',
                        'R': 'R',
                        'S': 'S',
                        'T': 'T',
                        'U': 'U',
                        'V': 'V',
                        'W': 'W',
                        'X': 'X',
                        'Y': 'Y',
                        'Z': 'Z',
                        'a': 'a',
                        'b': 'b',
                        'c': 'c',
                        'd': 'd',
                        'e': 'e',
                        'f': 'f',
                        'g': 'g',
                        'h': 'h',
                        'i': 'i',
                        'j': 'j',
                        'k': 'k',
                        'l': 'l',
                        'm': 'm',
                        'n': 'n',
                        'o': 'o',
                        'p': 'p',
                        'q': 'q',
                        'r': 'r',
                        's': 's',
                        't': 't',
                        'u': 'u',
                        'v': 'v',
                        'w': 'w',
                        'x': 'x',
                        'y': 'y',
                        'z': 'z',
                        '0': '0',
                        '1': '1',
                        '2': '2',
                        '3': '3',
                        '4': '4',
                        '5': '5',
                        '6': '6',
                        '7': '7',
                        '8': '8',
                        '9': '9'
                        }

data_base_of_extensions = {'images': ['jpg', 'bmp', 'jepg', 'webp'],
                           'documents': ['doc', 'docx', 'odt', 'rtf', 'xls', 'xlsx', 'txt', 'ods'],
                           'audio': ['mp3', 'wav', 'flac', 'ogg', 'aac'],
                           'video': ['mp4', 'wmv', 'flv', 'ogv', 'webm', 'avi', 'mpeg'],
                           'archives': ['bztar', 'gztar', 'tar', 'xztar', 'zip']}

known_extensions = []
unknown_extensions = []

images = []
documents = []
audio = []
video = []
archives = []


def normalize_filenames(norm_name):  # str in

    normalized = ''
    for v_symbol in norm_name:
        normalized += normalization_scheme.get(v_symbol, '_')

    return str(normalized)  # new transliteration name (str out)


def normalized_way(file_to_sort, main_directory):  # pathlib.Path, pathlib.Path

    norm_way = []
    norm_way.append(str(main_directory))
    for iter_part in (str(file_to_sort)[len(str(main_directory))+1:]).split('\\')[:-1]:
        iter_part = normalize_filenames(iter_part)
        norm_way.append(iter_part)
    norm_way.append(str(file_to_sort).split('\\')[-1])

    return pathlib.Path("\\".join(norm_way))  # pathlib.Path


def test_extensions(var_exts, current_fs_obj):  # extension, current pathlib.Path obj

    global unknown_extensions  # ??? in other program works fine without "global"
    global known_extensions  # ??? in other program works fine without "global"
    flag_ok = 0
    for category, ext_list in data_base_of_extensions.items():
        for it_ext in ext_list:  # run for all known extensions
            if it_ext == var_exts:  # known extension
                known_extensions.append(var_exts)
                unknown_extensions = list(set(unknown_extensions))
                # eval is dangerous! Try...:
                eval(category).append(current_fs_obj)
                # getattr(sys.modules[__name__], category).append(current_fs_obj)
                flag_ok = 1
    if flag_ok == 0:  # no known extension = unknown extension
        unknown_extensions.append(var_exts)
        unknown_extensions = list(set(unknown_extensions))


def new_name(try_new_name, add_cx):  # rechange number(add_cx) in filename(try_new_name)
    return (".".join(try_new_name.split(".")[:-1]))[:-len(str(add_cx-1))] + str(
        add_cx) + '.' + try_new_name.split(".")[len(try_new_name.split("."))-1]


def check_new_names(dir_in, norm_name, objs_extension=None):  # pathlib.Path, str, str
    '''checks for the existence of a file in a folder, and returns a new "unused" name: 
    return pathlib.Path(with new name) if set objs_extension,
    else return str(new name)'''
    ret_flag = 0
    if objs_extension == None:
        ret_flag = 1  # call without a third parameter
        if len(norm_name.split(".")) >= 2:  # its a dots in a name
            objs_extension = norm_name.split(
                ".")[len(norm_name.split("."))-1]  # extension
            # name without extension
            norm_name = norm_name[:-1-len(objs_extension)]
        else:  # no dots in a name
            objs_extension = ''  # no extension, no changes in the name
    if objs_extension != '':
        norm_fs_obj = dir_in / ".".join([norm_name, objs_extension])
    else:
        norm_fs_obj = dir_in / norm_name
    new_counter = 0
    while True:  # Is it better to use recursion?
        if norm_fs_obj.exists():  # norm_fs_obj.is_file() or norm_fs_obj.is_dir()/// symb link?
            new_counter += 1  # new number for new name
            # rechange number in filename:
            # new name with number
            norm_name = new_name(norm_name, new_counter)
            if objs_extension != '':
                norm_fs_obj = dir_in / ".".join([norm_name, objs_extension])
            else:
                norm_fs_obj = dir_in / norm_name
        else:
            break
    if ret_flag == 1:
        if objs_extension != '':
            return ".".join([norm_name, objs_extension])
        else:
            return norm_name

    return norm_fs_obj


def sorting_preparation(root_dir):  # pathlib.Path

    for fs_obj in main_directories:
        obj_candidate = root_dir / fs_obj
        if obj_candidate.is_file() or obj_candidate.is_dir():
            obj_candidate.rename(
                root_dir / check_new_names(root_dir, obj_candidate.name))


def junk_scanner(dir_in):  # pathlib.Path

    global all_subdirectories  # ??? in other program works fine without "global"
    for fs_obj in dir_in.iterdir():  # all obj in dir
        if fs_obj.is_dir():  # if dirr
            if fs_obj.name not in main_directories:
                # all_subdirectories.append(fs_obj)  # no normalized dir to list?
                junk_scanner(fs_obj)
        # if file or dir
        if len(fs_obj.name.split(".")) >= 2:
            objs_name = ".".join(fs_obj.name.split(
                ".")[:-1])  # name without extensions
            objs_extension = fs_obj.name.split(
                ".")[len(fs_obj.name.split("."))-1]  # extensions? but if dir = "extension" directory will not be normalized!!!
        else:
            objs_name = fs_obj.name
            objs_extension = ''  # no extension
        if fs_obj.is_file():  # is file
            norm_name = normalize_filenames(objs_name)
            norm_fs_obj = check_new_names(
                dir_in, norm_name, objs_extension)  # = pathlib.Path with name
        else:  # is dir
            norm_name = normalize_filenames(fs_obj.name)
            # =pathlib.Path / str(name)
            norm_fs_obj = dir_in / check_new_names(dir_in, norm_name)
            # !!! rename before?!!!! norm_name
            all_subdirectories.append(norm_fs_obj)
        # !!!!! if already exist file with new name...?
        # norm_fs_obj = dir_in / ".".join([norm_name, objs_extension])
        fs_obj.rename(norm_fs_obj)
        if objs_extension:
            test_extensions(objs_extension, norm_fs_obj)


# pathlib.Path, pathlib.Path, str("images/... etc")
def simple_sorterer(file_to_sort, main_directory, simple_category):

    target_dir = main_directory / simple_category
    target_dir.mkdir(exist_ok=True)
    # if name is non-free? check_new_names...
    free_name = check_new_names(target_dir, file_to_sort.name)
    # / file_to_sort.name !!!if renamed dir?
    file_to_sort = normalized_way(file_to_sort, main_directory)
    file_to_sort.replace(target_dir / free_name)


def archives_sorterer(current_arch, main_directory):  # pathlib.Path, pathlib.Path

    target_dir = main_directory / "archives"
    target_dir.mkdir(exist_ok=True)
    current_arch = normalized_way(current_arch, main_directory)
    # arch_dir = target_dir / (current_arch.name).rsplit(".", 1)[0]
    # if name is non-free? check_new_names...
    arch_dir = check_new_names(
        target_dir, (current_arch.name).rsplit(".", 1)[0])  # !!str, but need pathlib.Path
    arch_dir = target_dir / arch_dir
    arch_dir.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(current_arch.absolute()),
                              str(arch_dir.absolute()))
    except:
        print('Error while unpacking archive. Wrong archive?')
        arch_dir.rmdir()
        return False
    # when remove archive?? now:
    current_arch.unlink()


def delete_free_dir(dir_obj):  # pathlib.Path

    try:
        dir_obj.rmdir()  # if free - silent removal
    except:  # ... else if... what Error? and else?
        pass


def start_cleaner(target_directory):  # string - user input at start

    global all_subdirectories  # ??? in other program works fine without "global"
    print('OK, let`s do it')
    directory = pathlib.Path(target_directory)
    if not directory.is_dir():
        print('Sorry, but "target directory" does not exist ',
              target_directory, "\n", directory.is_dir())
        exit()
    # !!!!! rename file and directory with reserved names!!!
    sorting_preparation(directory)
    junk_scanner(directory)

    for item_category in data_base_of_extensions.keys():  # sort all normal category without archives
        if item_category != "archives":
            # eval is dangerous! Try...: getattr(sys.modules[__name__], item_category)
            for fs_obj in eval(item_category):
                simple_sorterer(fs_obj, directory, item_category)

    for fs_obj in archives:  # unpack archives
        archives_sorterer(fs_obj, directory)

    all_subdirectories = all_subdirectories[::-1]  # from nested to root!
    for fs_obj in all_subdirectories:
        delete_free_dir(fs_obj)

    return True


def main():

    try:
        start_cleaner(sys.argv[1])  # user`s string sys.argv[1]
    except:
        print('Sorry, no target directory specified. Checking "D:\\tests"')
        start_cleaner("D:\\tests")  # !!!!!!!!!!!!!!


if __name__ == "__main__":
    main()
