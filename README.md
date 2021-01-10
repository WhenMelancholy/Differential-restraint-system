# 差分约束系统展示

- 20 年秋季学期科学之美课程大作业
- 使用 Manim 生成制作较为直观的动画, 形象的展示差分约束系统

## 制作过程中的问题

- 刚开始时对 Manim 的函数和类不是很熟悉, 花了较多的时间阅读例子和文档, 阅读相关的源代码
- 遇到了 Manim 存在的一些 BUG, 向开发人员反馈之后才了解到问题的原因和解决方法
  - [Support more svg syntaxes · Issue #912 · ManimCommunity/manim (github.com)](https://github.com/ManimCommunity/manim/issues/912)
- 视频中最后的解法介绍依然需要一定的门槛, 需要观众对前面的最短路理解的较为深刻, 不过通过之前的几分钟让观众了解最短路的要求还是蛮高的. 不过较为具体的介绍最短路需要花大量的篇幅, 会显得舍本逐末了, 因此只能舍去.
- 最短路部分可以做的更加直观, 例如可以多增加一些现实中的例子, 像一开始的外卖员的例子. 这样也能更好的体现抽象和直观转换的美感. 但是 Manim 对于非数学动画的支持不是很好, 同时太过具体前后的画风也会很不协调, 因此只有简单的介绍.

## 制作过程中的收获

- 了解了怎么运用 Python 来解决实际的问题, 对 Python 的运用也更加熟练了
- 了解了 Manim 这个工具, 在制作之余测试了一些例子和有趣的小动画, 以后就可以将自己的一些想法轻松的直观的展现出来啦!
- 这次大作业也是一个难得的机会, 给了我动力, 去做一些之前想做但是缺乏实际行动的事情. 这次自己动手制作视频, 我也了解到视频制作是多么的不易. 一开始的学习阶段就花去了不少心思, 之后的素材收集阶段, 虽然我只有几个素材要用, 但是也需要花费功夫去筛选, 假如是自行制作的话, 时间甚至可能要翻倍. 同时从脚本/分镜到开始通过代码一个个的实现场景, 都是对自己的一点挑战, 也更加深刻的意识到一个优秀的视频是多么的来之不易.

----

## 补充内容

- 项目的源码在压缩包里, 包含了用到的素材/虚拟环境的配置文件/代码/开题报告的PPT, 同时项目的主页托管在 GitHub 上, 从中也可以看到项目的历史记录(和代码风格的变化), 也许会对后面想入坑的同学有所帮助
  - 项目的 GitHub 主页: [WhenMelancholy/Differential-restraint-system (github.com)](https://github.com/WhenMelancholy/Differential-restraint-system)
  - 项目的科大内网 GitLab 主页: [Qiu Mufan / Differential restraint system · GitLab (ustc.edu.cn)](https://git.lug.ustc.edu.cn/Melancholy/differential-restraint-system)
- 就我个人而言, 原本我是想做一期视频展现抽象的差分约束不等式和直观的最短路之间有着怎样的联系, 但是在实际的制作过程中, 我还感受到了代码的美. 一个是 Manim 通过抽象而又精巧的模块设计, 完成了通过代码制作动画这一个较为复杂的功能. 一个是在深入了解 Manim 后, 我了解到贝塞尔曲线在生成动画方面的强大, 例如可以通过矩阵对贝塞尔曲线控制点的操作来完成缩放/移动/变形的动画, 以及贝塞尔曲线相关的函数可以用来控制速度, 实现更为流畅的动画, 这些也是我在制作过程中所收获的科学之美. 当然, 这其中美只有亲身制作才能体会到了, 也希望下一次选课的同学们能够有着更多的收获, 感受到更多的科学的美!

## 视频内容安排

- [x] 介绍页面
- [x] 差分约束系统的介绍
  - [x] 变量组的展示
  - [x] 各类差分约束系统
- [x] 差分约束问题如何解决?
  - [x] 图论中的最短路模型
    - [x] 最短路的概念
    - [x] 最短路成立的条件
    - [x] 最短路的算法
  - [x] 转化为最短路问题
- [ ] 差分约束系统的用途(没有找到较为详细的资料, 考虑到内容已经足够, 故略去)

## 目录结构

- `conda/`: 包含使用 Anaconda 创建新的虚拟环境时需要导入的文件

- `video/`

  - `asset/`: 用到的或者备用的素材
  - `script.py`: 生成视频中各个场景的代码, `class Video`为整个视频, 其余场景为各个分镜
  - `manim.cfg`: Manim 的默认配置文件

- `README.md`: 本文档的 Markdown 版本

- `项目报告.pdf`: 本文档的 pdf 版本

- `差分约束系统.pptx`: 开题报告

  

## 素材来源

- 3b1b 的图标: 3b1b 的 video 仓库
  - [3b1b/videos: Code for the manim-generated scenes used in 3blue1brown videos (github.com)](https://github.com/3b1b/videos)
- SVG 素材(自行车/笑脸/...): IconFont
  - [iconfont-阿里巴巴矢量图标库](https://www.iconfont.cn/)
  - [Font Awesome](https://fontawesome.com/)
- 背景音乐: Nocturne in E flat major, Op. 9 no. 2
  - [Chopin 3 Notturni op. 9 - Download free sheet music (musopen.org)](https://musopen.org/music/108-nocturnes-op-9/)