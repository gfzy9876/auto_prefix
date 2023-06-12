import subprocess
import json
import sys
import os


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'


def error(msg):
    print(Colors.RED + msg + Colors.RESET)


def warn(msg):
    print(Colors.YELLOW + msg + Colors.RESET)


def info(msg):
    print(Colors.RESET + msg + Colors.RESET)


def active(msg):
    print(Colors.GREEN + msg + Colors.RESET)


if len(sys.argv) <= 1 or len(sys.argv[1].strip()) == 0:
    error('注意: commit 未指定输入内容')
    exit()
else:
    commit_msg = sys.argv[1]
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_name = f"{current_dir}/prefixConfig.json"
prefixConfig = json.load(open(config_file_name))

# git diff --name-only HEAD .
output = subprocess.run(['git', 'diff', '--name-only',
                        'HEAD', '.'], capture_output=True, text=True).stdout
changed_file_dir = list(set([line.split('/')[0]
                        for line in output.splitlines()]))

if len(changed_file_dir) == 0:
    active('无修改内容')
    exit()

ready_commit_prefix_list = []
for changed_file in changed_file_dir:
    if changed_file in prefixConfig:
        info(changed_file + "在prefix配置文件中, prefix为: " +
             prefixConfig[changed_file])
        ready_commit_prefix_list.append(prefixConfig[changed_file])

    else:
        if ('whiteList' in prefixConfig
            and prefixConfig['whiteList'] != None
                and changed_file in prefixConfig['whiteList']):
            warn(changed_file + "在白名单中, prefix由其他改动指定")
        else:
            error(
                f"{changed_file}文件有修改，但不在{config_file_name}配置文件中, 请自行提交, \n例如: git commit -m \"[prefix] xxxx\""
            )
            exit()

if len(ready_commit_prefix_list) == 0:
    # len(ready_commit_prefix_list) == 0 证明修改的文件都是白名单中的文件
    error(f"修改的文件都是白名单中的文件：{changed_file_dir}，请手动提交commit！~")
    exit()
elif (len(ready_commit_prefix_list) == 1 or prefixConfig['multiplePrefix']):
    # git add .
    subprocess.run(["git", "add", "."])

    prefixWithBrackets = ['[' + item + ']' for item in ready_commit_prefix_list]

    prefix = ' '.join(prefixWithBrackets)
    command = ['git', 'commit']
    command.extend(['-m', f"{prefix} {commit_msg}"])

    active("Exe command:    " + ' '.join(command))
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        error("Commit failed: " + result.stderr)
else:
    error("commit涉及到" + str(len(ready_commit_prefix_list)) +
          "个module处改动: " + str(ready_commit_prefix_list) + "请手动指定prefix值")
    exit()
