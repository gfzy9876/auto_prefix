# auto_prefix

git commit自动携带 prefix，避免每次提交commit都手动输入prefix，防止输错。

# 工作原理

通过git diff ，拿到当前所有修改的文件的最上级目录，检查修改了多少个module
如果发现同时修改多个module的文件，会提示报错（因为遵循每次diff只需改一个module的原则，方便之后回溯历史提交）
如果只修改了一个module的文件，会在`commit -m`后自动加上 对应module的prefix（module的prefix通过prefixConfig.json存放）

以菲律宾为例，目前有三个项目：

| module名    | commit提交携带的prefix |
| ----------- | ---------------------- |
| mabilisCash | [MabCash]              |
| pesoagad    | [PHCash]               |
| Fincash     | [FinCash]              |
| moneyMall   | [MOMCash]              |

对应prefixConfig.json如下：

```json
{
  "mabilisCash": "MabCash",
  "finCash": "FinCash",
  "moneyMall": "MOMCash",
  "whiteList": [
  ]
}
```

## 关于白名单：

在项目中，有一些module之外的文件，例如settings.gradle，这些文件修改可以随着某一个module的修改一同提交

# 使用

假如我本次提交内容，修改了mabilisCash下的若干文件，在调用`aup(名字可以自定义，setup中会说道) '修改了xxx'`，你会看到shell中出现一下提示：

![image-20230606154307866](https://github.com/gfzy9876/auto_prefix/blob/main/imgs/1.png?raw=true)

同时在你的commit已经自动添加prefix了

![image-20230606154420088](https://github.com/gfzy9876/auto_prefix/blob/main/imgs/2.png?raw=true)

# 安装

## 1. 克隆项目
推荐 在项目根目录下克隆，并在项目根目录的.gitignore文件添加`auto_prefix`，方便之后维护，以下是在项目根目录下clone auto_prefix的步骤：
### 1.1. 移动到项目根目录，执行git clone
```sh
cd 项目根目录
git clone https://github.com/gfzy9876/auto_prefix.git
```
### 1.2. 项目根目录.gitignore添加auto_prefix
注意:) 如发现auto_prefix已经从工作区添加到暂存区，可调用`git rm --cached -f auto_prefix`从暂存区移除

## 2. 调用setup.sh

```sh
cd auto_prefix
sh setup.sh
```
setup.sh中的提示比较全面，应该没什么问题

## 3. 修改prefixConfig.json文件

以菲律宾为例，key为项目module名，value为git 提交commit的前缀

```json
{
  "mabilisCash": "MabCash",
  "finCash": "FinCash",
  "moneyMall": "MOMCash",
  "whiteList": [
  ]
}
```
