# auto_prefix

git commit 自动携带 prefix，避免每次提交 commit 都手动输入 prefix，防止忘记或输错。

# 工作原理

通过 git diff ，拿到当前所有修改的文件的最上级目录，检查修改了多少个 module
如果发现同时修改多个 module 的文件，会提示报错（因为遵循每次 diff 只需改一个 module 的原则，方便之后回溯历史提交）
如果只修改了一个 module 的文件，会在`commit -m`后自动加上 对应 module 的 prefix（module 的 prefix 通过 .aup_config.json 存放）

以菲律宾为例，目前有三个项目：

| module 名   | commit 提交携带的 prefix |
| ----------- | ------------------------ |
| mabilisCash | [MabCash]                |
| pesoagad    | [PHCash]                 |
| Fincash     | [THCash]                 |
| moneyMall   | [MOMCash]                |

对应 .aup_config.json 如下：

```json
{
    "prefix": {
        "mabilisCash": "MabCash",
        "finCash": "FinCash",
        "moneyMall": "MOMCash"
    },
    "whiteList": [],
    "multiplePrefix": false
}
```

# 使用

假如我本次提交内容，修改了 mabilisCash 下的若干文件，在调用`aup(名字可以自定义，setup中会说道) '修改了xxx'`，你会看到 shell 中出现一下提示：

![image-20230606154307866](https://github.com/gfzy9876/auto_prefix/blob/main/imgs/1.png?raw=true)

同时在你的 commit 已经自动添加 prefix 了

![image-20230606154420088](https://github.com/gfzy9876/auto_prefix/blob/main/imgs/2.png?raw=true)

# 安装

## 1. 克隆项目

```sh
git clone https://github.com/gfzy9876/auto_prefix.git
```

## 2. 调用 setup.sh

```sh
cd auto_prefix
sh setup.sh
```

setup.sh 中的提示比较全面，应该没什么问题
![image-20230606154420088](https://github.com/gfzy9876/auto_prefix/blob/main/imgs/setup.png?raw=true)

## 3. 在项目中创建 .aup_config.json 文件, 配置说明

```json
{
    "prefix": {
        "mabilisCash": "MabCash",
        "finCash": "FinCash",
        "moneyMall": "MOMCash"
    },
    "whiteList": [],
    "multiplePrefix": false
}
```

| **key**        | **含义**                                                                                                   |
| :------------- | :--------------------------------------------------------------------------------------------------------- |
| prefix         | 项目 module 名称以及对应前缀                                                                               |
| whiteList      | 在项目中，有一些 module 之外的文件，例如 settings.gradle，这些文件修改可以随着某一个 module 的修改一同提交 |
| multiplePrefix | 是否允许多项目同时提交， 并携带多 prefix（默认 false）                                                     |
