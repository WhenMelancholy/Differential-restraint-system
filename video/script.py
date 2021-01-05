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


class Node(VDict):
    def __init__(self, radius=1.0, num="1", **kwargs):
        super().__init__(**kwargs)

        circle = Circle(radius=radius, fill_color=BLACK, fill_opacity=1)
        text = Text(num)

        text.move_to(circle)

        self["circle"] = circle
        self["text"] = text


class IntroductionToGraph(PikachuScene):
    """
    简单介绍计算机中的图论
    """

    CONFIG = {
        "building_file": r"asset\tallbuilding.svg",
        "building_file2": r"asset\tallbuilding2.svg",
        "node_radius": 0.3,
    }

    def scene_road(self, stroke_width=0.01):
        # object
        tall_building1 = SVGMobject(self.building_file, stroke_width=stroke_width)
        tall_building2 = SVGMobject(self.building_file2, stroke_width=stroke_width)

        five_km = Text("5 km")

        node1 = Node(self.node_radius, num="1")
        node2 = Node(self.node_radius, num="1")
        negative_km = Text("-5")

        # layout
        tall_building1.to_edge(LEFT)
        tall_building2.to_edge(RIGHT)

        road = Line(tall_building1.get_right(), tall_building2.get_left())
        positive_brace = Brace(road, direction=UP)
        positive_text = positive_brace.get_text("distance should be positive")
        five_km.next_to(road, DOWN)

        node1.to_edge(LEFT)
        node2.to_edge(RIGHT)

        negative_km.next_to(road, DOWN)
        road2 = Line(node1.get_right(), node2.get_left())
        brace2 = Brace(road2, direction=UP)
        dis = brace2.get_text("distance would be negative")

        # present
        # 数学上的最短路和现实有什么不一样吗?
        # 比如, 现实里面的距离只能是正数,
        self.play(
            ShowCreation(tall_building1),
            ShowCreation(tall_building2),
            ShowCreation(road),
        )
        self.play(
            ShowCreation(positive_brace),
            Write(five_km),
            Write(positive_text),
        )

        # 但是数学中的最短路还可以是负数
        self.play(
            ReplacementTransform(VGroup(tall_building1, tall_building2, road, five_km, positive_text, positive_brace),
                                 VGroup(node1, node2, road2, negative_km, dis, brace2))
        )

        self.wait()
        self.play(
            *[FadeOut(m) for m in self.get_mobject_family_members()]
        )
        pass

    def graph_scene(self, poly_dis=3):
        # objects
        nodes = []
        for i in range(6):
            node = Node(self.node_radius, str(i))
            theta = i * 2 * np.pi / 6
            x = np.cos(theta)
            y = np.sin(theta)
            x *= poly_dis
            y *= poly_dis
            node.move_to(np.array([x, y, 0]))
            nodes.append(node)

        def get_edge(m, x, y, w, offset=1, cls=Line):
            line = cls(m[x].get_center(), m[y].get_center())
            num = DecimalNumber(
                w,
                num_decimal_places=1,
                show_ellipsis=False,
                include_sign=False,
            )
            line.end_one = m[x]
            line.end_two = m[y]
            line.num = num
            num.line = line
            num.offset = offset

            def updater(mob: Line):
                mob.set_start_and_end_attrs(line.end_one, line.end_two)
                pass

            def num_updater(mob: DecimalNumber):
                ll = mob.line
                mob.move_to(ll.get_center() + ll.copy().rotate(PI / 2).get_unit_vector() * mob.offset)
                pass

            line.add_updater(updater)
            num.add_updater(num_updater)
            return line

        edges = [get_edge(nodes, 0, 5, 3),
                 get_edge(nodes, 0, 4, 5.5, cls=Arrow),
                 get_edge(nodes, 0, 2, -1000),
                 get_edge(nodes, 1, 4, 0, cls=Arrow),
                 get_edge(nodes, 2, 3, -200),
                 get_edge(nodes, 0, 3, 100)]

        # layout

        # present
        # 因此, 让我们将现实中的地图抽象出来, 定义一个新的结构, 图
        self.play(
            *[FadeIn(m) for m in edges],
            *[FadeIn(m) for m in nodes],
            *[FadeIn(i.num) for i in edges],
        )

        # 图里面有着节点, 对应着地图里面的地点
        self.play(
            *[Flash(i["circle"], flash_radius=i["circle"].radius * 2) for i in
              filter(lambda m: isinstance(m, Node), self.get_mobject_family_members())]
        )
        # 有些节点之间有边, 对应着不同地点之间的道路
        self.play(
            *[Indicate(i, scale_factor=1) for i in
              filter(lambda m: isinstance(m, (Line, Arrow)), self.get_mobject_family_members())]
        )
        # 边可以是有向的,
        self.play(
            *[Indicate(i, scale_factor=1) for i in
              filter(lambda m: isinstance(m, Arrow), self.get_mobject_family_members())]
        )
        # 也可以是无向的
        self.play(
            *[Indicate(i, scale_factor=1) for i in
              filter(lambda m: isinstance(m, Line), self.get_mobject_family_members())]
        )
        # 低优先级: 介绍重边和自环
        # 边还有边权, 对应着道路的距离
        self.play(
            *[Indicate(i.num) for i in
              filter(lambda m: isinstance(m, (Line, Arrow)), self.get_mobject_family_members())]
        )
        # 低优先级: 介绍负的边权和零的距离
        self.play(
            *[Indicate(i.num) for i in
              filter(lambda m: isinstance(m, (Line, Arrow)) and m.num.get_value() <= 0,
                     self.get_mobject_family_members())]
        )

        # 有了边权, 就可以引出最短路的定义
        # 两个点之间边权和最短的一条路径就是最短路
        # 例如, 图中从3到0的最短路是0->2->3, 而不是0->3, 因为0->2->3的边权和最小, 为-1200
        def find_edge(x, y, es=edges, ns=nodes):
            for i in es:
                if i.end_one == ns[x] and i.end_two == ns[y]:
                    return i
                if i.end_one == ns[y] and i.end_two == ns[x]:
                    return i

        self.play(Indicate(find_edge(0, 2), scale_factor=1))
        self.play(Indicate(find_edge(2, 3), scale_factor=1))
        self.play(Indicate(find_edge(0, 3), scale_factor=1))
        shortest_num = DecimalNumber(-1200)
        shortest_num.to_edge(DOWN)
        self.play(
            Transform(VGroup(find_edge(0, 2).num.copy(), find_edge(2, 3).num.copy()),
                      shortest_num)
        )
        # 同时, 从4到1的最短路不存在, 因为1到4之间的边是单向边, 只能从1到4, 不能从4到1
        self.play(Indicate(find_edge(1, 4), scale_factor=1))
        self.play(*[FadeOut(i) for i in self.get_mobject_family_members()])
        # 最短路问题研究的十分广泛, 有着多种快速解法,
        spfa = Text("SPFA 算法")
        dijkstra = Text("Dijkstra 算法")
        VGroup(spfa, dijkstra).arrange(DOWN)
        self.play(FadeIn(spfa))
        self.play(FadeIn(dijkstra))
        # 很多问题也可以转换为最短路问题来求解,
        # 比如差分约束问题
        pass

    def construct(self):
        # 显示
        # 数学上的最短路和现实有什么不一样吗?
        # 比如, 现实里面的距离只能是正数,
        # 但是数学中的最短路还可以是负数
        self.scene_road()
        # 现实中, 几个位置之间的距离需要满足三角不等式
        # 低优先级: 介绍三角不等式
        # 但是数学中节点间的距离就不需要
        # TODO
        # 因此, 让我们将现实中的地图抽象出来, 定义一个新的结构, 图
        # 图里面有着节点, 对应着地图里面的地点
        # 有些节点之间有边, 对应着不同地点之间的道路
        # 边可以是有向的, 也可以是无向的
        # 低优先级: 介绍重边和自环
        # 边还有边权, 对应着道路的距离
        # 低优先级: 介绍负的边权和零的距离
        # 有了边权, 就可以引出最短路的定义
        # 两个点之间边权和最短的一条路径就是最短路
        # 最短路问题研究的十分广泛, 有着多种快速解法,
        # 很多问题也可以转换为最短路问题来求解,
        # 比如差分约束问题
        self.graph_scene()
        pass


class IntroudctionToSystemOfDifferenceConstraints(PikachuScene):
    """
    从数学上介绍差分约束系统问题
    """

    def construct(self):
        # 显示
        # 很高兴你能看到这
        # 再重复一下, 不要被这个高大上的名词吓到了, 它的命名可以从定义直观的感受到
        # 差分约束系统由 n 个变量
        var = MathTex(
            "x_1",
            ",",
            "x_2",
            ",",
            r"\dots"
            ",",
            "x_n"
        )
        brace = Brace(var, direction=UP)
        text = brace.get_tex(r"n\text{ variables}")

        var_group = VGroup(var, brace, text)

        equations = MathTex(
            r"x_{i_1}", r"-", r"x_{j_2}\leqslant w_1\\",
            r"x_{i_2}", r"-", r"x_{j_2}\leqslant w_2\\",
            r"\vdots\\",
            r"x_{i_m}", r"-", r"x_{j_m}\leqslant w_m\\",
        )
        eq_brace = Brace(equations, direction=LEFT)
        eq_text = eq_brace.get_tex(r"m \text{ equations}")

        eq_group = VGroup(equations, eq_brace, eq_text)

        self.play(ShowCreation(var))
        self.play(FadeIn(brace))
        self.play(Write(text))

        # 和 m 个不等式组组成
        self.play(var_group.animate.next_to(equations, UP))
        self.play(ShowCreation(equations))
        self.play(FadeIn(eq_brace))
        self.play(Write(eq_text))

        # 每个不等都都是对变量间差值的约束,
        self.play(
            Indicate(equations[1]),
            Indicate(equations[4]),
            Indicate(equations[8]),
        )
        # 因此得名差分约束系统
        # 差分约束问题就是找出一组合法的解满足差分约束系统
        self.play(
            Indicate(var)
        )
        self.play(
            Indicate(equations)
        )
        # 唔, 观众们可以暂停自己写几个例子, 这并不是一个简洁的公式就可以求解的问题, 感受到了吗?
        # 当变量个数很少的时候, 手算便可以轻松得到解答
        var_and_eq = var_group + eq_group
        self.play(
            var_and_eq.animate.shift(2 * LEFT)
        )

        n_eq = MathTex("n=")
        m_eq = MathTex("m=")
        n_num = DecimalNumber(3, num_decimal_places=0)
        m_num = DecimalNumber(5, num_decimal_places=0)
        VGroup(n_eq, m_eq, n_num, m_num).scale(2)

        n_eq.next_to(equations, RIGHT + UP)
        m_eq.next_to(n_eq, DOWN)
        n_num.next_to(n_eq, RIGHT)
        m_num.next_to(m_eq, RIGHT)

        n_num.add_updater(lambda m: m.increment_value() if m.get_value() < 10000 else None)
        m_num.add_updater(lambda m: m.increment_value() if m.get_value() < 100000 else None)
        self.play(ShowCreation(VGroup(n_eq, n_num)))
        self.play(ShowCreation(VGroup(m_eq, m_num)))
        # 但是当变量个数增加的时候, 就需要依靠计算机来求解了

        self.wait(5)
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
