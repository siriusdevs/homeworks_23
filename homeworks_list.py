import subprocess 
import typing
from mdutils.mdutils import MdUtils

HW_COUNT = 10 # TODO: provide as an argument  
MD_FILENAME = 'README.md' 
MD_TITLE = 'Репозиторий для домашних заданий, осень 2023, Колледж Сириус' 

HomeworksInfo = typing.Dict[int, bool]

REMOTE_PREFIX = 'remotes/origin/' 
def get_branches(): 
    output = subprocess.run(['git', 'branch', '--all'], capture_output=True).stdout.decode()
    lines = [line.strip() for line in output.split('\n')] 
    return [line for line in lines if line.startswith(REMOTE_PREFIX) and not 'HEAD' in line] 

def branch_has_file(branch, file) -> bool: 
    result = subprocess.run(['git', 'cat-file', '-e', f'{branch}:{file}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0 

def get_hw_names() -> typing.List[str]: 
    homeworks =[] 
    for hw_index in range(1, HW_COUNT+1): 
        homeworks.append(f'hw{hw_index}.py')
    return homeworks  

def get_finished_homeworks() -> typing.Dict[str, HomeworksInfo]:    
    branches = get_branches() 
    result = {} 
    for branch in branches: 
        surname = branch.removeprefix(REMOTE_PREFIX)
        result[surname] = {} 
        for hw_name in get_hw_names(): 
            result[surname][hw_name] = branch_has_file(branch, hw_name) 
    return result

def write_homework_stats_to_md(stats: typing.Dict[str, HomeworksInfo]): 
    md = MdUtils(file_name=MD_FILENAME, title=MD_TITLE) 
    table = ["Branch"] + get_hw_names() 
    for branch, hws in sorted(stats.items(), key=lambda item: item[0]): 
        table += [branch] + ['+' if hws[hw] else '-' for hw in get_hw_names()]
    md.new_table(columns=len(get_hw_names())+1, rows=len(stats)+1, text=table, text_align='center')
    md.create_md_file() 

def get_stats_and_write_md(): 
    stats = get_finished_homeworks() 
    write_homework_stats_to_md(stats) 

if __name__ == '__main__': 
    get_stats_and_write_md() 
