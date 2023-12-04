"""Provides functions for fetching homework statistics from git and exporting them to md."""
import subprocess  # noqa: S404

from mdutils.mdutils import MdUtils

HW_COUNT = 4
MD_FILENAME = 'README.md'
MD_TITLE = 'Репозиторий для домашних заданий, осень 2023, Колледж Сириус'


REMOTE_PREFIX = 'remotes/origin/'


def _get_branches():
    def _filter(branch: str) -> bool:
        excludes = 'HEAD', 'patch'
        return not any(excluded in branch for excluded in excludes)
    process = subprocess.run(['git', 'branch', '--all'], capture_output=True)  # noqa: S607, S603
    output = process.stdout.decode()
    lines = [line.strip() for line in output.split('\n')]
    return [line for line in lines if line.startswith(REMOTE_PREFIX) and _filter(line)]


def _branch_has_path(branch: str, path: str) -> bool: 
    cmd = ['git', 'cat-file', '-e', f'{branch}:{path}']
    process = subprocess.run(cmd, capture_output=True)  # noqa: S603
    return process.returncode == 0


def _branch_has_hw(branch: str, index: int) -> bool:
    return _branch_has_path(branch, f'hw{index}') or _branch_has_path(branch, f'hw{index}.py')


HomeworkStats = dict[str, dict[int, bool]]


def get_finished_homeworks() -> HomeworkStats:
    """Get homework stats for each branch.

    Returns:
        HomeworkStats: statistics for finished homeworks fetched from git.
    """
    branches = _get_branches()
    stats = {}
    for branch in branches:
        surname = branch.removeprefix(REMOTE_PREFIX)
        stats[surname] = {}
        for hw in range(1, HW_COUNT+1):
            stats[surname][hw] = _branch_has_hw(branch, hw)
    return stats


def write_homework_stats_to_md(stats: HomeworkStats):
    """Write homework stats table to a markdown file.

    Args:
        stats: HomeworkStats for filling the table
    """
    md = MdUtils(file_name=MD_FILENAME, title=MD_TITLE)
    table = ['Branch'] + [f'hw{hw}' for hw in range(1, HW_COUNT+1)]
    # sort stats by branch name to get consistent results
    sorted_stats = sorted(stats.items(), key=lambda elem: elem[0])

    for branch, hws in sorted_stats:
        table.append(branch)
        table += ['+' if hws[hw] else '-' for hw in range(1, HW_COUNT+1)]
  
    if sorted_stats:
        table = [sum([hws[hw] for _, hws in sorted_stats]) for hw in range(1, HW_COUNT+1)] + table
        table.insert(0, 'overall')

    cols, rows = HW_COUNT + 1, len(stats) + 2
    md.new_table(columns=cols, rows=rows, text=table)
    md.create_md_file()


def fetch_stats_and_write_md():
    """Call get_finished_homeworks() and then write_homework_stats_to_md()."""
    stats = get_finished_homeworks()
    write_homework_stats_to_md(stats)


if __name__ == '__main__':
    fetch_stats_and_write_md()
