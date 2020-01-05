# Horse Hunter

猎马人顶级装备，你手中敲击键盘的光，就是他🐎火化的火星

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
python main.py
```

2. 打开聊天框

Ctrl+V, Enter, Ctrl+V, Enter, Ctrl+V, Enter...

## 进阶使用

```
usage: main.py [-h] [--target {female,male,mix}] [--level {max,min,mix}]

optional arguments:
  -h, --help            show this help message and exit
  --target {female,male,mix}, -t {female,male,mix}
                        设置辱骂对象
  --level {max,min,mix}, -l {max,min,mix}
                        设置辱骂等级
  --interval INTERVAL, -i INTERVAL
                        设置刷新间隔
```

## 致谢

金句资源(`resources-*.txt`)、性别替换(`replaceF2N.py`)内容来源：[直播点吧](https://nmsl.shadiao.app)