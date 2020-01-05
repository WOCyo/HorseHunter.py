# Horse Hunter

猎马人顶级装备，我手中敲击键盘的光，就是令堂火化的火星

> 本软件仅限用于自卫反击，向网络暴力说不！！！

## 效果

剪贴板内每 0.1s 刷新一条脏话，帮你在骂战中不被欺负

![preview](imgs/preview.gif)

## 安装

```
pip install -r requirements.txt
```

## 快捷使用

1. 运行脚本

```
python HorseHunter.py
```

2. 打开聊天框

Ctrl+V, Enter, Ctrl+V, Enter, Ctrl+V, Enter...

## 进阶使用

```
usage: HorseHunter.py [-h] [--target {female,male,mix}]
                      [--level {max,min,mix}] [--interval INTERVAL]

自动向剪贴板刷新金句，让你不再饱受欺凌

optional arguments:
  -h, --help            show this help message and exit
  --target {female,male,mix}, -t {female,male,mix}
                        设置辱骂对象, female=令堂, male=令尊, mix=混合. 默认 female
  --level {max,min,mix}, -l {max,min,mix}
                        设置辱骂等级, max=火力全开, min=口吐芬芳, mix=混合. 默认 max
  --interval INTERVAL, -i INTERVAL
                        设置刷新间隔(s). 默认 0.1
```

## 致谢

金句资源(`resources-*.txt`)、性别替换(`replaceF2M.py`)内容来源：[直播点吧](https://nmsl.shadiao.app)