from io import TextIOWrapper
from pathlib import Path
import sys


def recursive_search(path:Path, f: TextIOWrapper):
    for p in Path(path).glob("*"):
        if p.is_file() and p.suffix not in exlude_list:
            print(f"{p}")
            f.write(p.absolute().__str__()+"\n")
            global file_counter
            file_counter +=1
        else:
            recursive_search(p,f)


if __name__ == '__main__':
    # command_dict ={cmd.split("=")[0] : cmd.split("=")[1] for cmd in sys.argv[1:]}
    # print(f'command dict -> {command_dict}')
    command_dict = {
        'search_path' : 'c:/',
        'out_path' : 'C:/codebase/pythone-codebase/python-for-dummies/outputs/all-files.txt'
    }
    search_path = command_dict['search_path']  # "C:/Users/a818517"
    output_file_path = command_dict['out_path'] # 'all_file_in_folder.txt'
    exclude = command_dict.get('extn')
    exlude_list = ['']
    if exclude is not None:
        exlude_list.extend(exclude.split(','))
    print('writing start.......')
    file_counter = 0
    with open(output_file_path,'w', encoding='utf-8') as f:  
        for path in Path(search_path).glob("*"):
            if path.is_dir():                            
                recursive_search(path,f)
            else:
                if path.suffix not in exlude_list:
                    f.write(path.absolute().__str__()+"\n")
                    file_counter +=1
    print(f'done....... tatal file write {file_counter}')
