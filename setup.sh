current_abs_path=$PWD
echo "当前目录:$current_abs_path"
read -p "请给autoPrefix设置一个快捷指令,方便shell调用(如果为空,默认为aup):" prefix
prefix=${prefix:-aup}

echo "\033[32m你设置的快捷指令为:$prefix\033[0m"
echo "生成的alias为:"
echo "\033[34malias $prefix=\"python $current_abs_path/commitPrefix.py \$1\"\033[0m"
echo "我不知道你用的什么sh工具....."
echo "如果你使用zsh:"
echo "\033[32m1. vi \$HOME/.zshrc\033[0m"
echo "\033[32m2. 把\033[34m上面的蓝色文字\033[0m粘贴到文件中, 然后:wq保存\033[0m"
echo "\033[32m3. source \$HOME/.zshrc\033[0m"

echo "如果你使用bash:"
echo "\033[32m1. vim \$HOME/.bash_rc\033[0m"
echo "\033[32m2. 把\033[34m上面的蓝色文字\033[0m粘贴到文件中, 然后:wq保存\033[0m"
echo "\033[32m3. source \$HOME/.bash_rc\033[0m\n"

cat <<EOF > prefixConfig.json
{
  "module文件名": "提交的prefix",
  "whiteList": [
  ],
  "multiplePrefix": false
}
EOF
echo "已生成prefixConfig.json文件: \033[32m$current_abs_path/prefixConfig.json\033[0m 记得去配置\n"

echo "使用:"
echo "\033[32m$prefix '我是提交的内容'\033[0m"