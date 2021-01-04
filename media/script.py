from manim import *


class TestTheScaleOfCanvas(Scene):
    """
    测试画布的大小
    测试发现, 竖直方向为4个单位, 水平方向为8个单位
    """

    def construct(self):
        dot = Dot().move_to(ORIGIN)
        text = Text(str(0)).move_to(RIGHT)

        self.add(dot)
        self.add(text)
        for i in range(10):
            text.generate_target()
            text.target.text = str(i)
            self.play(
                dot.shift, RIGHT,
            )
            self.play(
                MoveToTarget(text),
            )
        self.wait()


class PikachuScene(Scene):
    CONFIG = {

    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for k, v in self.CONFIG.items():
            self.__setattr__(k, v)


class Begin(PikachuScene):
    """
    展示校徽/课程/姓名
    """
    CONFIG = {
        "svg_name": "white.svg",
        "author": "When",
        "class_name": "科学之美",
        "png_name": "logo.png",
        "logo_scale": 0.25,
    }

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.svg_name = "white.svg"
    #     self.author = "When"
    #     self.class_name = "科学之美"
    #     self.png_name = "logo.png"
    #     self.logo_scale = 0.25

    def construct(self):
        super().construct()
        # 添加对象
        logo = ImageMobject(self.png_name).move_to(ORIGIN).set_width(self.logo_scale * config.frame_width)
        class_name = Text(self.class_name)
        author = Text(self.author)

        # 排版布局
        strings = VGroup(class_name, author).arrange(RIGHT)
        Group(logo, strings).arrange(DOWN)

        # 展示对象
        self.play(
            GrowFromCenter(logo),
            ShowCreation(strings),
        )


class Title(PikachuScene):
    """
    展示视频的标题
    """


class RealityShortestPath(PikachuScene):
    """
    展示现实中常见的最短路的场景
    """

    CONFIG = {
        "bike_file": r"asset\bike.svg",
        "bike_scale": 0.3,
        "bike_pos": np.array([-0.5, 0.5, 0]),

        "person_file": r"asset\hungry.svg",
        "person_scale": 0.3,
        "person_pos": np.array([0.5, -0.5, 0]),

        "happy_file": r"asset\happy.svg",
        "sad_file": r"asset\sad.svg",
    }

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.bike_file = "bike.svg"
    #     self.bike_scale = 0.3
    #     self.bike_pos = np.array([-0.5, 0.5, 0])
    #
    #     self.person_file = "hungry.svg"
    #     self.person_scale = 0.3
    #     self.person_pos = np.array([0.5, -0.5, 0])

    def construct(self):
        # 生成
        bike = SVGMobject(self.bike_file, stroke_width=0.5 * DEFAULT_STROKE_WIDTH).scale(self.bike_scale)
        person = SVGMobject(self.person_file, stroke_width=0.5 * DEFAULT_STROKE_WIDTH).scale(self.person_scale)
        happy = SVGMobject(self.happy_file)
        sad = SVGMobject(self.sad_file)

        # 布局
        bike.to_edge(UP + LEFT)
        person.to_edge(DOWN + RIGHT)
        short_line = self.get_short_line([bike.get_right(), person.get_left()])
        random_line = self.get_random_line(bike.get_right(), person.get_left())

        # 显示
        # 在生活中的很多地方, 都有最短路的概念
        # 小到送外卖的时候
        self.play(ShowCreation(bike), ShowCreation(person))
        # 地图为外卖小哥推荐了最短的路线
        self.play(ShowCreation(short_line), ShowCreation(random_line))
        # 饿扁了的孩子就可以早点吃上饭菜
        # 假如地图给出了错误的路线
        # 孩子就只能饥肠辘辘了
        # 大到城市间的道路安排, 铁路公路的布局
        # 如何布局才能降低修建难度, 维护成本, 提高运营收益
        # 都有着最短路的身影
        # 最短路在数学中也有着很多应用
        # 比如差分约束问题
        # 等等, 别被吓住了,
        # 很高兴你回来了

    def get_short_line(self, points: list):
        pre = points.pop(0)
        lines = VGroup()
        for x in points:
            lines.add(Line(pre, x))
            pre = x
        return lines

    def get_random_line(self, start, end):
        points = [
            start,
            np.array([1, 1, 0]),
            np.array([2, 2, 0]),
            end,
        ]
        return CubicBezier(points)


class IntroductionToGraph(PikachuScene):
    """
    简单介绍计算机中的图论
    """

    def construct(self):
        # 显示
        # 数学上的最短路和现实有什么不一样吗?
        # 比如, 现实里面的距离只能是正数,
        # 但是数学中的最短路还可以是负数
        # 现实中, 几个位置之间的距离需要满足三角不等式
        # 低优先级: 介绍三角不等式
        # 但是数学中节点间的距离就不需要
        # 因此, 让我们将现实中的地图抽象出来, 定义一个新的结构, 图
        # 图里面有着节点, 对应着地图里面的地点
        # 有些节点之间有边, 对应着不同地点之间的道路
        # 边可以是有向的, 也可以是无向的
        # 低优先级: 介绍重边和自环
        # 边还有边权, 对应着道路的距离
        # 低优先级: 介绍负的边权和零的距离
        pass


class IntroductionToShortestPath(PikachuScene):
    """
    简单介绍计算机中的最短路及相关性质
    """

    def construct(self):
        # 显示
        # 有了边权, 就可以引出最短路的定义
        # 两个点之间边权和最短的一条路径就是最短路
        # 最短路问题研究的十分广泛, 有着多种快速解法,
        # 很多问题也可以转换为最短路问题来求解,
        # 比如差分约束问题
        pass


class IntroudctionToSystemOfDifferenceConstraints(PikachuScene):
    """
    从数学上介绍差分约束系统问题
    """

    def construct(self):
        # 显示
        # 差分约束系统由 n 个变量
        # 和 m 个不等式组组成
        # 每个不等都都是对变量间差值的约束,
        # 因此得名差分约束系统
        # 当变量个数很少的时候, 手算便可以轻松得到解答
        # 但是当变量个数增加的时候, 就需要依靠计算机来求解了
        # 但是计算机怎么求解呢?
        pass


class IntroductionToSolutionsOfSystemOfDifferenceConstraints(PikachuScene):
    """
    介绍差分约束系统的解法
    """

    def construct(self):
        # 显示
        # 还记得我们前面提到的最短路吗
        # 差分约束问题可以转化为最短路问题!
        # 先给出一个小小的提示,
        # 运用最短路的以下条件(dis[x]代表x到起点的最短路, w[a,b]代表边权)
        # 观众们可以暂停视频思考一下
        # 观众们可能已经发现了,
        # 这个等式和差分约束系统的不等式十分相似,
        # 因此我们可以用节点和边权来模拟变量和约束,
        # 对于每一个约束 x_i-x_j<=w_i
        # 从节点 j 和节点 i 之间连接一条边权为 w_i 的边
        # 当然了, 由于差分约束系统存在多解, 因此我们还需要想办法来约束解以便得到一组特解
        # 观众们不妨暂停视频再想一想
        # 我们可以添加一个新的 0 号节点, 并且向每个点连一条权重为 0 的边
        # 这个做法相当于规定差分约束系统中最大的变量的值为 0
        # 接下来用之前提到过的算法求解出最短路, 便可以得到一组特解了, 特解就是 x_i = dis[i]
        # 就这样, 一个数学上的问题转化为了一个图论中的问题, 并且得到了良好的解答
        # 当然, 差分约束系统还有一些扩展, 所以最后留一些思考题给大家, 大家可以思考如何讲这些问题转化为差分约束问题
        # x_a-x_b>=c
        # x_a=x_b
        # x_i/x_j<=c_k
        pass


class Bilibili(PikachuScene):
    """
    求三连的界面
    """

    def construct(self):
        # 显示
        # 假如你觉得我们的视频不错的话,
        # 求点赞求投币求收藏
        # 感谢观看!
        pass
