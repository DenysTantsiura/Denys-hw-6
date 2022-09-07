# ...!?
'''У багатьох на робочому столі є папка, яка називається якось ніби "Розібрати"...
    Create Junk sorterer.
    Homework Python Core Hw06.
    Run example:
    python sort.py /user/Desktop/Мотлох/Junk
    Увага!!!!!!!!! 352 строка !!!!!
    '''

from logging import ERROR
import os
import sys
import re
from datetime import datetime  # , date
import shutil


data_base_of_extensions = {'images': ['jpg', 'bmp', 'jepg', 'webp'],
                           'documents': ['doc', 'docx', 'odt', 'rtf', 'xls', 'xlsx', 'txt', 'ods'],
                           'audio': ['mp3', 'wav', 'flac', 'ogg', 'aac'],
                           'video': ['mp4', 'wmv', 'flv', 'ogv', 'webm', 'avi', 'mpeg'],
                           'archives': ['bztar', 'gztar', 'tar', 'xztar', 'zip']}  # rar 7z

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

known_extensions = []
unknown_extensions = []
# dir_struct_list = []


def normalize_filenames(norm_name):

    normalized = ''
    for v_symbol in norm_name:
        normalized += normalization_scheme.get(v_symbol, '_')

    return str(normalized)  # new transliteration name


def checking_the_source_folder(junk_dir):

    if os.path.isdir(junk_dir):
        return True  # it`s a directory

    return False  # is no dirr there


def creating_a_directory_structure(way_in):

    for name_dir, ext_list in data_base_of_extensions.items():
        try:  # os.path.join(way_in, name_dir) # try to rename existing file or directory with
            os.rename(os.path.join(way_in, name_dir),
                      os.path.join(way_in, name_dir + '_' + re.sub(r'(:| )', '-', str(datetime.now()))))  # +str(date.today())
            # old obj to new name with date+time & create a new directory in structure
            os.mkdir(os.path.join(way_in, name_dir))
        except PermissionError:
            print("Operation in source directory is not permitted!")
        # For other errors
        except OSError as error:
            try:  # if no directory with name from directory structure, let`s create a new directory in structure
                os.mkdir(os.path.join(way_in, name_dir))
            except PermissionError:
                print("Operation in source directory is not permitted!")
            # For other errors
            except OSError as error:
                print("Unknown Error, sorry, can't create Dir-structure")


def test_extensions(var_exts):

    flag_ok = 0
    for category, ext_list in data_base_of_extensions.items():
        for it_ext in ext_list:  # run for all known extensions
            if it_ext == var_exts:  # known extension
                known_extensions.append(var_exts)
                flag_ok = 1
    if flag_ok == 0:  # no known extension = unknown extension
        unknown_extensions.append(var_exts)


def rename_for_normalize(src, dst, type_obj, new_counter=-1):  # file_ext = None
    # if src != dst: #####!!!ERROR???!!Yes? where file extension if file?!!!!!!!!!!!!!!!!!!!
    if src == dst:
        #print("dst is ", dst)
        return dst  # return "new" normalized name
    try:
        os.rename(src, dst)
        filesystem_obj_renamed = dst
        #print("filesystem_obj_renamed is ", filesystem_obj_renamed)
    except:
        new_counter += 1
        if type_obj == 'dirr':
            dst = dst + str(new_counter)
        else:  # is file
            dst = ".".join(dst.split(".")[:-1]) + str(new_counter) + '.' + \
                dst.split(".")[len(dst.split("."))-1]  # name file w ext!!!
        if new_counter == 0:  # if name is occupied - try to rename in name with number 0
            filesystem_obj_renamed = rename_for_normalize(
                src, dst, new_counter)
        elif new_counter > 0:
            # remove number from name-candidate to rename if occupied
            # and try with new name with new number
            if type_obj == 'dirr':
                dst = dst[:-len(str(new_counter-1))] + str(new_counter)
            else:  # is file
                dst = (".".join(dst.split(".")[:-1]))[:-len(str(new_counter-1))] + str(
                    new_counter) + '.' + dst.split(".")[len(dst.split("."))-1]  # rechange number in filename
            filesystem_obj_renamed = rename_for_normalize(
                src, dst, new_counter)
        else:
            print('Rename - Error!')

    return filesystem_obj_renamed  # return new normalized name


# Path of Junk #for root, dirs, files in os.walk('python/Lib/email'): but hometask...
def to_delete_free_directories(way_in):

    for filesystem_obj in os.listdir(way_in):
        if os.path.isdir(os.path.join(way_in, filesystem_obj)):
            to_delete_free_directories(os.path.join(way_in, filesystem_obj))
            if not os.listdir(os.path.join(way_in, filesystem_obj)):
                os.rmdir(os.path.join(way_in, filesystem_obj))


def Func_junk_opener(way_in, flag_first_start=0):  # run through directory tree

    if checking_the_source_folder(way_in):  # new obj file or directory?
        # for on all iter in way
        for filesystem_obj in os.listdir(way_in):
            if os.path.isdir(os.path.join(way_in, filesystem_obj)):  # os.path.isdir(file) ?
                # need full path os.path.join(dirname, name)
                # reneme dirr!!!!!!!!!!!!!!!!!!!!!!!
                filesystem_obj_renamed = rename_for_normalize(src=os.path.join(way_in, filesystem_obj),
                                                              dst=os.path.join(way_in, normalize_filenames(filesystem_obj)), type_obj='dirr')
                # os.path.join(way_in, filesystem_obj_renamed))
                # go in new rename normalized name directory
                Func_junk_opener(filesystem_obj_renamed)
            elif os.path.isfile(os.path.join(way_in, filesystem_obj)):  # if catch file
                # if file without a dot
                if len(filesystem_obj.split(".")) == 1:
                    filesystem_obj = rename_for_normalize(src=os.path.join(way_in, filesystem_obj),
                                                          dst=os.path.join(way_in, filesystem_obj + '.noext'), type_obj='file')
                # next
                fsobj_ext = filesystem_obj.split(
                    ".")[len(filesystem_obj.split("."))-1]  # .jepg = get file extension
                file_name_wo_ext = ".".join(filesystem_obj.split(
                    ".")[:-1])  # file name without extension
                # file_name_w_ext = ".".join(filesystem_obj.split(".")[:-1]) + '.' + fsobj_ext  # !!!!!!!!!! to str from []
                test_extensions(fsobj_ext)  # check file extension
                rename_for_normalize(src=os.path.join(way_in, file_name_wo_ext + '.' + fsobj_ext),
                                     dst=os.path.join(way_in, normalize_filenames(file_name_wo_ext) + '.' + fsobj_ext), type_obj='file')
    elif flag_first_start == 1:
        # {'D:\\tests\\'} sys.argv[1]
        print(f"Error. Sorry but there is no directory on the way in D:\\tests")
        vex = input("Entering any key for exit")
        # return False
        exit()  # ?


def check_name_arch(dirr_name_for_arch, new_counter=-1):  # not name - full path with name

    new_counter += 1
    new_name = dirr_name_for_arch
    if os.path.isdir(new_name):  # dirr_name_for_arch is exist?
        if new_counter == 0:
            new_name = dirr_name_for_arch + \
                str(new_counter)  # first new name (full path)
        elif new_counter > 0:  # full path without try-number in name + new namber to full-path with name
            new_name = dirr_name_for_arch[:-
                                          len(str(new_counter-1))] + str(new_counter)
        # try chek new name (and send current number)
        new_name = check_name_arch(new_name, new_counter)

    return new_name


def check_name_file(full_path_file_wo_ext, fsobj_ext, new_counter=-1):

    new_counter += 1
    new_name = full_path_file_wo_ext + str(new_counter) + '.' + fsobj_ext
    if os.path.isfile(new_name):
        #new_name = full_path_file_wo_ext + str(new_counter) + '.' + fsobj_ext
        new_name = check_name_file(
            full_path_file_wo_ext, fsobj_ext, new_counter)

    return new_name


def Func_moving_known_types(way_in):

    for filesystem_obj in os.listdir(way_in):
        if os.path.isdir(os.path.join(way_in, filesystem_obj)):
            Func_moving_known_types(os.path.join(way_in, filesystem_obj))
        elif os.path.isfile(os.path.join(way_in, filesystem_obj)):
            fsobj_ext = filesystem_obj.split(
                ".")[len(filesystem_obj.split("."))-1]  # get extension
            for name_dir, ext_list in data_base_of_extensions.items():
                for curent_ext in ext_list:
                    if curent_ext == fsobj_ext:
                        if name_dir != 'archives':
                            try:
                                shutil.move(os.path.join(
                                    way_in, filesystem_obj), 'D:\\tests' + '\\' + name_dir)  # sys.argv[1]
                            except:  # first if already exist file
                                new_name_file = check_name_file(
                                    'D:\\tests' + '\\' + name_dir + '\\' + ".".join(filesystem_obj.split(".")[:-1]), fsobj_ext)
                                shutil.move(os.path.join(
                                    way_in, filesystem_obj), new_name_file)  # sys.argv[1]
                                #print('Can`t move file ',filesystem_obj)
                        elif name_dir == 'archives':
                            new_name_arch = check_name_arch(
                                'D:\\tests' + '\\' + name_dir + '\\' + ".".join(filesystem_obj.split(".")[:-1]))
                            shutil.unpack_archive(os.path.join(
                                way_in, filesystem_obj), new_name_arch)  # sys.argv[1]


def main():
    try:
        dir_in = sys.argv[1]
    except IndexError:
        dir_in = 'D:\\tests'
    # if os.path.isdir('D:\\tests'):  # (Path of Junk) sys.argv[1]
    if os.path.isdir(dir_in):
        to_delete_free_directories(dir_in)
        # (Path of Junk) sys.argv[1]
        creating_a_directory_structure(dir_in)
    # first_start_ok = Func_junk_opener('D:\\tests', 1)  # (Path of Junk) sys.argv[1]
        Func_junk_opener(dir_in, 1)
        Func_moving_known_types(dir_in)
        to_delete_free_directories(dir_in)
    else:
        print(f"Invalid input start parameter: {dir_in}")

    # time for tests:
    for i in known_extensions:
        print(f"I know: {i}")
    for i in unknown_extensions:
        print(f"Unknow: {i}")
    vex = input("Entering any key for exit")


if __name__ == "__main__":  # entry point
    main()
