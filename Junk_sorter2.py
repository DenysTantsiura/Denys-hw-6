"""
A simple junk sorter program. Full description will be added later.
look at the line #354 ... "D:\\tests" !!!!!
"""

import sys
import pathlib
import shutil

# {'images', 'documents', 'audio', 'video', 'archives'}

known_extensions = []
unknown_extensions = []
data_base_of_extensions = {'images': ['jpg', 'bmp', 'jepg', 'webp', 'gif', 'png', 'img'],
                           'documents': ['doc', 'docx', 'odt', 'rtf', 'xls', 'xlsx', 'txt', 'ods'],
                           'audio': ['mp3', 'wav', 'flac', 'ogg', 'aac'],
                           'video': ['mp4', 'wmv', 'flv', 'ogv', 'webm', 'avi', 'mpeg'],
                           'archives': ['bztar', 'gztar', 'tar', 'xztar', 'zip']}
main_directories = {i for i in data_base_of_extensions.keys()}

images = []
documents = []
audio = []
video = []
archives = []

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


def test_extensions(var_exts, current_fs_obj):  # extension, current pathlib.Path obj
    '''
    to check file extension and filling file listings
    '''
    global unknown_extensions  # ??? in other program works fine without "global"
    global known_extensions  # ??? in other program works fine without "global"
    flag_ok = 0  # known extension?
    var_exts = var_exts.lower()
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


def junk_scanner(dir_in):  # pathlib.Path
    """
    run recursive listing of directories to check file extension and filling file listings to sort and normalize
    """
    for fs_obj in dir_in.iterdir():  # all obj in dir
        if fs_obj.is_dir():  # if dirr
            if fs_obj.name not in main_directories:
                # all_subdirectories.append(fs_obj)  # no normalized dir to list?
                junk_scanner(fs_obj)
        if fs_obj.is_file():
            if (fs_obj.suffix)[1:]:  # extension
                # str(extension), pathlib.Path(file_obj) to:
                test_extensions((fs_obj.suffix)[1:], fs_obj)


def normalize(norm_name):  # str in
    """
    to normalized string with transliteration
    """
    normalized = ''
    for v_symbol in norm_name:
        # unknown symbols into "_" :
        normalized += normalization_scheme.get(v_symbol, '_')
    return str(normalized)  # new transliteration name (str out)


def new_name(try_new_name, add_cx):  # rechange number(add_cx) in filename(try_new_name)
    return (".".join(try_new_name.split(".")[:-1]))[:-len(str(add_cx-1))] + str(
        add_cx) + '.' + try_new_name.split(".")[len(try_new_name.split("."))-1]


def check_new_names(dir_in, norm_name_obj):  # pathlib.Path, pathlib.Path
    '''checks for the existence of a file in a folder after normalized, 
    and return str(free new_name)'''
    if norm_name_obj.is_dir() or len(norm_name_obj.suffix) == 0:
        norm_name = norm_name_obj.name  # name.ext or name
        norm_name = normalize(norm_name)  # str dir
        obj_candidate = dir_in / norm_name
    # elif norm_name_obj.is_file() and len(norm_name_obj.suffix) > 0:
    else:
        norm_name = norm_name_obj.name[:-len(norm_name_obj.suffix)]
        norm_name = normalize(norm_name)  # str file w/o ext
        obj_candidate = dir_in / "".join([norm_name, norm_name_obj.suffix])
    new_counter = 0
    while True:  # Is it better to use recursion? not now
        if obj_candidate.exists():  # norm_fs_obj.is_file() or norm_fs_obj.is_dir()/// symb link?
            new_counter += 1  # new number for new name
            # rechange number in filename, new name with number:
            norm_name = new_name(norm_name, new_counter)
            if norm_name_obj.is_file() and len(norm_name_obj.suffix) > 0:
                obj_candidate = dir_in / \
                    "".join([norm_name, norm_name_obj.suffix])
            else:  # dir or len(norm_name_obj.suffix) == 0
                # if exist dots in name of directory (false suffix)
                obj_candidate = dir_in / norm_name
        else:
            break
    if norm_name_obj.is_file() and len(norm_name_obj.suffix) > 0:
        return "".join([norm_name, norm_name_obj.suffix])
    else:
        return norm_name


def freeing_the_reserved_name_for_the_sorting_directory(main_directory):
    for item_category in data_base_of_extensions.keys():  # sort all categories
        new_counter = 0
        need_free_name = main_directory / item_category
        if need_free_name.is_file():  # the existing file
            # looking for a new name for the file
            obj_candidate = pathlib.Path(str(need_free_name)+str(new_counter))
            while True:  # Is it better to use recursion? not now
                if obj_candidate.exists():  # norm_fs_obj.is_file() or norm_fs_obj.is_dir()/// symb link?
                    new_counter += 1  # new number for new name
                    # rechange number in dir-name, new name with adding number:
                    norm_name = new_name(obj_candidate.name, new_counter)
                    obj_candidate = main_directory / norm_name
                else:
                    break
            need_free_name.replace(obj_candidate)
    # return True

# pathlib.Path, pathlib.Path, str("images/... etc")


def simple_sorterer(file_to_sort, main_directory, simple_category):
    target_dir = main_directory / simple_category
    # ADD! rename file with "simple_category" name, if exist = def freeing_the_reserved_name_for_the_sorting_directory
    target_dir.mkdir(exist_ok=True)
    # if name for file is non-free? check_new_names...
    # for check and normalize..., # pathlib.Path, pathlib.Path to:
    free_name = check_new_names(target_dir, file_to_sort)
    file_to_sort.replace(target_dir / free_name)


def archives_sorterer(current_arch, main_directory):  # pathlib.Path, pathlib.Path
    target_dir = main_directory / "archives"
    # ADD! rename file with "archives" name, if exist = def freeing_the_reserved_name_for_the_sorting_directory
    target_dir.mkdir(exist_ok=True)
    arch_dir = check_new_names(
        target_dir, current_arch.parent / current_arch.name[:-len(current_arch.suffix)])
    arch_dir = target_dir / arch_dir
    arch_dir.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(current_arch.absolute()),
                              str(arch_dir.absolute()))
    except:
        print('Error while unpacking archive. Wrong archive?')
        arch_dir.rmdir()
        return False
    # when remove archive? now if unpacking is successful:
    current_arch.unlink()
    # return True


def delete_empty_dir(dir_in):  # pathlib.Path
    """
    run recursive listing of directories to remove empty-dir or normalize, if else
    """
    for fs_obj in dir_in.iterdir():  # all obj in dir
        if fs_obj.is_dir():  # if dirr
            if fs_obj.name not in main_directories:  # such incorrect initial conditions in the task
                delete_empty_dir(fs_obj)
                try:
                    fs_obj.rmdir()  # if empty - silent removal
                except:  # ... else if... what Error? and else?
                    # chek and normalize # pathlib.Path, pathlib.Path -> str: new_name_dir
                    new_name_dir = check_new_names(dir_in, fs_obj)
                    fs_obj.replace(dir_in / new_name_dir)


def start_cleaner(target_directory):  # string - user input at start
    """
    main function 
    (all files and folders are normalized...
     but 
     Files whose extensions are unknown remain unchanged!)
    """
    print('OK, let`s do it')
    directory = pathlib.Path(target_directory)
    if not directory.is_dir():
        print('Sorry, but "target directory" does not exist ',
              target_directory, "\n", directory.is_dir())
        exit()
    # run recursive listing of directories to check file extension and populate file listings to sort and normalize
    junk_scanner(directory)  # pathlib.Path

    freeing_the_reserved_name_for_the_sorting_directory(directory)

    for item_category in data_base_of_extensions.keys():  # sort all normal category without archives
        if item_category != "archives":
            # eval is dangerous! Try...: getattr(sys.modules[__name__], item_category)
            for fs_obj in eval(item_category):  # in each list
                # pathlib.Path, pathlib.Path, str("images/... etc") to:
                simple_sorterer(fs_obj, directory, item_category)

    for fs_obj in archives:  # unpack archives
        # pathlib.Path, pathlib.Path
        archives_sorterer(fs_obj, directory)
        # normalize files from the archive???

    # deleting empty directories or normalize
    delete_empty_dir(directory)  # pathlib.Path


def main():
    """
    two options for launching the program
    """
    try:
        start_cleaner(sys.argv[1])  # str
    except:
        print('Sorry, no target directory specified. Checking "D:\\tests"')
        start_cleaner("D:\\tests")  # str


if __name__ == "__main__":
    main()
