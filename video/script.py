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
    def sub(self, time=None, *args, **kwargs):
        if not time:
            if not self.pretitle:
                time = DEFAULT_WAIT_TIME
            else:
                time = self.pretitle.time
        super().wait(time, *args, **kwargs)
        self.play(FadeOut(self.pretitle), run_time=1.0)
        self.pretitle = None

    def my_play(self, *args, run_time=None, **kwargs):
        if not run_time:
            if self.pretitle:
                run_time = self.pretitle.time
                super().play(*args, run_time=run_time, **kwargs)
            else:
                super().play(*args, **kwargs)
        else:
            super().play(*args, run_time=run_time, **kwargs)

    def subtitle(self, text, time=None, wait=False, per=0.1, **kwargs):
        if self.pretitle:
            self.play(FadeOut(self.pretitle))
        pretitle = Text(text, **kwargs)
        pretitle.scale(0.5)
        if pretitle.get_width() > 0.9 * config.frame_width:
            pretitle.set_width(0.9 * config.frame_width)
        pretitle.to_edge(DOWN)
        if not time:
            time = len(text) * per
        pretitle.time = time
        self.play(FadeIn(pretitle))
        self.pretitle = pretitle
        # if not wait:
        #     time *= 1000
        #     pretitle.time = time
        #
        #     def updater(mob, dt):
        #         if dt > mob.time:
        #             self.play(Uncreate(mob))
        #             self.pretitle = None
        #
        #     pretitle.add_updater(updater)
        #     self.play(Write(pretitle))
        #     self.pretitle = pretitle
        # else:
        #     self.play(Write(pretitle))
        #     self.wait(time)
        #     self.play(Uncreate(pretitle))

    def tear_down(self):
        self.play(*[FadeOut(i) for i in self.get_mobject_family_members()])

    def add_num(self, mob: Line, w: int or str, offset=0.15, scaler=0.7):
        if isinstance(w, int):
            num = Integer(w, num_decimal_places=0)
        elif isinstance(w, str):
            num = MathTex(w)
        else:
            raise Exception("Please given right argument")
        num.set_color(ORANGE)
        num.move_to(mob.get_center() + mob.copy().rotate(PI / 2).get_unit_vector() * offset)
        # angle = mob.get_angle() + PI
        # if angle >= 2 * PI:
        #     angle -= 2 * PI
        # if angle <= -2 * PI:
        #     angle += 2 * PI
        # print(w, angle)
        # angle = 0
        # if angle > PI / 2 or angle < -PI / 2:
        #     angle += PI
        # num.rotate(angle)
        num.scale(scaler)
        return num

    CONFIG = {

    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pretitle = None
        for k, v in self.CONFIG.items():
            self.__setattr__(k, v)

    def construct(self):
        pass


class Begin(PikachuScene):
    """
    展示校徽/课程/姓名
    """
    CONFIG = {
        "svg_name": r"asset\white.svg",
        "author": "B站用户: 凉宫春日的忘却",
        "class_name": "科学之美课程大作业",
        "png_name": r"asset\logo.png",
        "logo_scale": 0.2,
    }

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.svg_name = "white.svg"
    #     self.author = "When"
    #     self.class_name = "科学之美"
    #     self.png_name = "logo.png"
    #     self.logo_scale = 0.25

    def construct(self):
        # 添加对象
        logo = ImageMobject(self.png_name).move_to(ORIGIN).set_width(self.logo_scale * config.frame_width)
        class_name = Text(self.class_name)
        author = Text(self.author)

        # 排版布局
        strings = VGroup(class_name, author).arrange(DOWN, buff=0.5)
        Group(logo, strings).arrange(DOWN, buff=1)

        # 展示对象
        self.play(
            GrowFromCenter(logo),
            Write(strings),
        )

        self.wait(5)
        self.tear_down()


class BeginTitle(PikachuScene):
    """
    展示视频的标题
    """

    def construct(self):
        awesome = Text("日常生活中无处不在的最短路, ")
        extend = Text("在数学中还有这种拓展?!")
        all_obj = VGroup(awesome, extend)
        all_obj.arrange(DOWN)
        all_obj.scale(1.5)

        self.play(Write(awesome))
        self.play(Write(extend))
        self.wait(1)
        self.play(FadeOut(VGroup(awesome, extend)))


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
        "sad_file": r"asset\sad-cry-regular.svg",
        "random_path": r"asset\randompath.svg",
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
        bike = SVGMobject(self.bike_file, stroke_width=0.2 * DEFAULT_STROKE_WIDTH).scale(self.bike_scale)
        person = SVGMobject(self.person_file, stroke_width=0.2 * DEFAULT_STROKE_WIDTH).scale(self.person_scale)
        bike.add_background_rectangle(opacity=0)
        person.add_background_rectangle(opacity=0)
        happy = SVGMobject(self.happy_file, stroke_width=0.2 * DEFAULT_STROKE_WIDTH).scale(self.person_scale).set_width(
            person.get_width())
        sad = SVGMobject(self.sad_file, stroke_width=0.2 * DEFAULT_STROKE_WIDTH).scale(self.person_scale).set_width(
            person.get_width())

        # 布局
        bike.to_edge(UP + LEFT)
        person.to_edge(DOWN + RIGHT)
        # short_line = self.get_short_line([bike.get_right(), person.get_left()])
        short_line = Line(bike.get_center() + 0.05 * (person.get_center() - bike.get_center()),
                          bike.get_center() + 0.95 * (person.get_center() - bike.get_center()), color=WHITE)
        move_line = Line(bike.get_center() + 0.00 * (person.get_center() - bike.get_center()),
                         bike.get_center() + 0.95 * (person.get_center() - bike.get_center()), color=WHITE)
        print(bike.get_center(), person.get_center())
        happy.move_to(person)
        sad.move_to(person)

        points = [
            [5.7, 2.88, 0],
            [5.7, 1.7, 0],
            [-0.5, 1.7, 0],
            [-0.5, 0.5, 0],
            [5.7, 0.5, 0],
            [5.7, -0.5, 0],
            [3.5, -0.5, 0],
            [3.5, -1.2, 0],
            [5.7, -1.2, 0],
            [5.7, -3, 0],
        ]
        random_line = VMobject(color=WHITE).set_points_as_corners([
            short_line.get_start(),
            *points,
            short_line.get_end(),
        ])
        move_random_path = VMobject(color=WHITE).set_points_as_corners([
            bike.get_center(),
            [5.7, 2.88, 0],
            [5.7, 1.7, 0],
            [-0.5, 1.7, 0],
            [-0.5, 0.5, 0],
            [5.7, 0.5, 0],
            [5.7, -0.5, 0],
        ])

        # present
        self.subtitle("生活中的很多地方, 都有最短路的概念")
        self.play(ShowCreation(VGroup(bike, person)),
                  runt_time=1)
        self.sub(0.5)

        self.subtitle("例如, 在送外卖的时候, 地图推荐了最短的路线")
        self.play(GrowArrow(short_line), run_time=2)
        self.play(MoveAlongPath(
            bike,
            move_line,
        ),
            rate_func=there_and_back_with_pause,
            run_time=5)
        self.sub(0.5)

        self.subtitle("饿扁了的孩子就可以开开心心的早点吃上热腾腾的饭菜")
        self.play(Transform(person, happy), run_time=1.5)
        self.sub(0.5)

        self.subtitle("但是假如推荐了一条绕来绕去的路线")
        self.play(ShowCreation(random_line), run_time=3)
        self.sub(0.5)

        self.subtitle("可怜的孩子就只能饥肠辘辘了")
        self.play(MoveAlongPath(
            bike,
            move_random_path,
        ),
            rate_func=linear,
            run_time=6)
        self.play(Transform(person, sad))
        self.sub(0.5)
        self.subtitle("在城市间道路安排, 铁路公路布局, 也有着最短路的身影")
        self.sub(1)
        self.subtitle("最短路在数学中也有着应用")
        self.sub(1)

        self.tear_down()

        # self.wait(2)
        return
        # random_line = self.get_random_line(bike.get_right(), person.get_left())
        # happy.move_to(person)
        # sad.move_to(person)

        # # 显示
        # # 在生活中的很多地方, 都有最短路的概念
        # # 小到送外卖的时候
        # self.subtitle("生活中的很多地方, 都有最短路的概念")
        # self.play(ShowCreation(bike), ShowCreation(person))
        # self.sub(1)
        # self.subtitle("小到送外卖")
        # self.play(ShowCreation(short_line), ShowCreation(random_line))
        # self.sub(1)
        # # 地图为外卖小哥推荐了最短的路线
        # beg_pos = bike.get_center()
        # end_pos = person.get_center()
        # self.subtitle("当地图为外面小哥推荐了最短的路线")
        # self.play(
        #     MoveAlongPath(bike, short_line)
        # )
        # self.sub(1)
        # # 饿扁了的孩子就可以早点吃上饭菜
        # self.subtitle("饿扁了的孩子就可以早点吃上饭菜")
        # self.play(MoveAlongPath(bike, short_line.reverse_points()))
        # self.play(ReplacementTransform(person, happy))
        # self.sub(1)
        #
        # # 假如地图给出了错误的路线
        # self.subtitle("假如地图给出了错误的路线")
        # self.play(MoveAlongPath(bike, self.get_half_random_line(bike.get_center(), person.get_center())))
        # # 孩子就只能饥肠辘辘了
        # self.play(ReplacementTransform(happy, sad))
        # # 大到城市间的道路安排, 铁路公路的布局
        # # 如何布局才能降低修建难度, 维护成本, 提高运营收益
        # # 都有着最短路的身影
        # # 最短路在数学中也有着很多应用
        # # 比如差分约束问题
        # # 等等, 别被吓住了,
        # # 很高兴你回来了

    def get_half_random_line(self, start, end):
        return Polygon([start,
                        np.array([-7, 4, 0]),
                        np.array([7, 3, 0])])

    def get_short_line(self, points: list):
        pre = points.pop(0)
        lines = VGroup()
        for x in points:
            lines.add(Line(pre, x, z_index=-1))
            pre = x
        return lines[0]

    def get_random_line(self, start, end):
        middle = np.array([(start[0] + end[0]) / 3, (start[1] + end[1]) / 3, 0]) + UP
        mid2 = np.array([(start[0] + end[0]) / 3 * 2, (start[1] + end[1]) / 3 * 2, 0]) + UP
        return CubicBezier([start, middle, mid2, end])
        pass
        # middle = np.array([end[0], start[1], 0])
        # return VGroup(
        #     Line(start, middle, z_index=-1),
        #     Line(middle, end, z_index=-1)
        # )

        # points = [
        #     start,
        #     np.array([-7, 3, 0]),
        #     np.array([-5, 0, 0]),
        #     np.array([-3, 2, 0]),
        #     np.array([-1, 0, 0]),
        #     np.array([1, 4, 0]),
        #     np.array([3, 0, 0]),
        #     np.array([5, 1, 0]),
        #     end,
        # ]
        #
        # lines = VGroup()
        # for i in range(0, len(points), 3):
        #     j = min(len(points), i + 4)
        #     lines += CubicBezier(points[i:j])
        # return lines


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
        node2 = Node(self.node_radius, num="2")
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
        self.subtitle("那数学上的抽象的最短路和现实有什么不一样吗?")
        self.play(
            ShowCreation(tall_building1),
            ShowCreation(tall_building2),
            ShowCreation(road),
            run_time=1
        )
        self.sub(1)
        self.subtitle("比如, 现实里面的距离只能是正数,")
        self.play(
            ShowCreation(positive_brace),
            Write(five_km),
            Write(positive_text),
            run_time=1
        )
        self.sub(1)
        # 但是数学中的最短路还可以是负数
        self.subtitle("但是抽象的距离还可以是负数")
        self.play(
            ReplacementTransform(VGroup(tall_building1, tall_building2, road, five_km, positive_text, positive_brace),
                                 VGroup(node1, node2, road2, negative_km, dis, brace2)),
            run_time=1,
        )
        self.sub()
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

        def get_edge(m, x, y, w, offset=0.3, cls=Line, scaler=0.5):
            line = cls(m[x].get_center(), m[y].get_center(), z_index=-1)
            # num = DecimalNumber(
            #     w,
            #     num_decimal_places=1,
            #     show_ellipsis=False,
            #     include_sign=False,
            # )
            line.end_one = m[x]
            line.end_two = m[y]

            line.num = self.add_num(line, w, offset, scaler)

            # line.num = num
            # num.line = line
            # num.offset = offset
            # num.move_to(line.get_center() + line.copy().rotate(PI / 2).get_unit_vector() * offset)
            # num.scale(scaler)
            #
            # angle = line.get_angle()
            # num.rotate(angle + PI)

            # num_text = BraceText(line, str(w), brace_direction=line.copy().rotate(PI / 2).get_unit_vector())
            # line.num = num_text

            def updater(mob: Line):
                mob.set_start_and_end_attrs(line.end_one, line.end_two)
                pass

            def num_updater(mob: DecimalNumber):
                ll = mob.line
                mob.move_to(ll.get_center() + ll.copy().rotate(PI / 2).get_unit_vector() * mob.offset)
                pass

            # line.add_updater(updater)
            # num.add_updater(num_updater)
            return line

        edges = [get_edge(nodes, 0, 5, 3),
                 get_edge(nodes, 0, 4, 5, cls=Arrow),
                 get_edge(nodes, 0, 2, -10),
                 get_edge(nodes, 1, 4, 0, cls=Arrow),
                 get_edge(nodes, 2, 3, -20),
                 get_edge(nodes, 0, 3, 10)]

        # layout

        # present
        # 因此, 让我们将现实中的地图抽象出来, 定义一个新的结构, 图
        self.subtitle("因此, 让我们将现实中的地图抽象出来,")
        ustc_map = ImageMobject(r"asset\map.jpg")
        ustc_map.set_height(0.7 * config.frame_height)
        self.play(FadeIn(ustc_map), run_time=1)
        self.wait()
        self.sub(1)
        self.play(FadeOut(ustc_map))
        self.subtitle("定义一个新的结构, 图")
        self.play(
            *[ShowCreation(m) for m in nodes],
            *[ShowCreation(m) for m in edges],
            *[ShowCreation(i.num) for i in edges],
            run_time=1.5
        )
        self.sub(1)
        # 图里面有着节点, 对应着地图里面的地点
        self.subtitle("图里面有着节点, 对应着地图里面的地点")
        self.play(
            *[Flash(i["circle"], flash_radius=i["circle"].radius * 2) for i in
              filter(lambda m: isinstance(m, Node), self.get_mobject_family_members())],
            run_time=2,
        )
        self.sub(1)
        # 有些节点之间有边, 对应着不同地点之间的道路
        self.subtitle("有些节点之间有边, 就像不同地点之间的道路")
        self.play(
            *[Indicate(i, scale_factor=1) for i in
              filter(lambda m: isinstance(m, (Line, Arrow)), self.get_mobject_family_members())],
            run_time=2,
        )
        self.sub(1)
        # 边可以是有向的,
        self.subtitle("边可以是有向的, 就像单行道")
        self.play(
            *[Indicate(i, scale_factor=1) for i in
              filter(lambda m: isinstance(m, Arrow), self.get_mobject_family_members())],
            run_time=2,
        )
        self.sub(1)
        # 也可以是无向的
        self.subtitle("也可以是无向的")
        self.play(
            *[Indicate(i, scale_factor=1) for i in
              filter(lambda m: isinstance(m, Line) and not isinstance(m, Arrow), self.get_mobject_family_members())],
            run_time=2,
        )
        self.sub(1)
        # 低优先级: 介绍重边和自环
        # 边还有边权, 对应着道路的距离
        self.subtitle("边还有边权, 就像道路的距离")
        self.play(
            *[Indicate(i.num) for i in
              filter(lambda m: isinstance(m, (Line, Arrow)), self.get_mobject_family_members())],
            run_time=2,
        )
        self.sub(1)
        # 低优先级: 介绍负的边权和零的距离
        self.subtitle("但是不同的是, 边权可以为0或者是负数")
        self.play(
            *[Indicate(i.num) for i in
              filter(lambda m: isinstance(m, (Line, Arrow)) and m.num.get_value() <= 0,
                     self.get_mobject_family_members())],
            run_time=2,
        )
        self.sub(1)

        # 有了边权, 就可以引出最短路的定义
        # 两个点之间边权和最短的一条路径就是最短路
        # 例如, 图中从3到0的最短路是0->2->3, 而不是0->3, 因为0->2->3的边权和最小, 为-1200
        def find_edge(x, y, es=edges, ns=nodes):
            for i in es:
                if i.end_one == ns[x] and i.end_two == ns[y]:
                    return i
                if i.end_one == ns[y] and i.end_two == ns[x]:
                    return i

        self.subtitle('有了边权, 就有了数学中最短路的概念')
        self.sub(1)
        self.subtitle("两个点之间边权和最短的一条路径就是最短路")
        self.sub(1)
        self.subtitle("注意不是边数最少的路径哦")
        self.sub(1)
        self.subtitle("例如, 图中从 3 到 0 的最短路是 0->2->3, 而不是 0->3")
        self.play(Indicate(find_edge(0, 2), scale_factor=1), run_time=1)
        self.play(Indicate(find_edge(2, 3), scale_factor=1), run_time=1)
        self.play(Indicate(find_edge(0, 3), scale_factor=1, color=RED), run_time=1)
        self.sub(1)
        dis = -30
        self.subtitle("最小的边权之和为 %d" % dis)
        shortest_num = DecimalNumber(dis, num_decimal_places=0)
        shortest_num.to_edge(RIGHT)
        self.play(
            Transform(VGroup(find_edge(0, 2).num.copy(), find_edge(2, 3).num.copy()),
                      shortest_num)
        )
        # 同时, 从4到1的最短路不存在, 因为1到4之间的边是单向边, 只能从1到4, 不能从4到1
        self.sub(1)
        self.subtitle("同时, 从 4 到 1 的最短路不存在")
        self.sub(1)
        self.subtitle("因为 1 到 4 之间的边是单向边, 只能从 1 到 4, 不能从 4 到 1")
        self.play(Indicate(find_edge(1, 4), scale_factor=1), run_time=2)
        self.sub(1)
        self.play(*[FadeOut(i) for i in self.get_mobject_family_members()])
        # 最短路问题研究的十分广泛, 有着多种快速解法,
        spfa = Text("Bellman-Ford 算法")
        dijkstra = Text("Dijkstra 算法")
        floyd = Text("Floyd 算法")
        VGroup(spfa, dijkstra, floyd).arrange(DOWN)

        self.subtitle("最短路的研究十分广泛, 有着很多快速的解法")
        self.sub(0.5)
        self.subtitle("比如 Bellman-Ford 算法")
        self.play(FadeIn(spfa))
        self.sub(0.5)
        self.subtitle("又比如 Dijkstra 算法")
        self.play(FadeIn(dijkstra))
        self.sub(0.5)
        self.subtitle("再比如代码简洁用途广泛的 Floyd 算法")
        self.play(FadeIn(floyd))
        self.sub(0.5)
        # 很多问题也可以转换为最短路问题来求解,
        # 比如差分约束问题
        self.subtitle("由于最短路问题有着优秀的解法")
        self.sub(1)
        self.subtitle("因此许多问题都可以转换为最短路问题")
        self.sub(1)
        self.play(*[FadeOut(i) for i in self.get_mobject_family_members()])
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
            r"x_{i_1}", r"-", r"x_{j_2}&\leqslant w_1\\",
            r"x_{i_2}", r"-", r"x_{j_2}&\leqslant w_2\\",
            r"\vdots&\\",
            r"x_{i_m}", r"-", r"x_{j_m}&\leqslant w_m\\",
        )
        equations.shift(LEFT)
        eq_brace = Brace(equations, direction=RIGHT)
        eq_text = eq_brace.get_tex(r"m \text{ equations}")

        eq_group = VGroup(equations, eq_brace, eq_text)

        self.subtitle("例如, 差分约束系统")
        self.play(ShowCreation(var))
        self.sub(0.5)
        self.subtitle("等等!!! 不要被这个名词吓到了")
        self.sub(1)
        self.subtitle("他的命名和定义都很直观!!!")
        self.sub(1)
        self.subtitle("差分约束系统由 n 个变量")
        self.play(FadeIn(brace))
        self.play(Write(text))
        self.sub(0.5)

        # 和 m 个不等式组组成
        self.subtitle("和 m 个不等式组成")
        self.play(var_group.animate.next_to(equations, UP))
        self.play(ShowCreation(equations))
        self.play(FadeIn(eq_brace))
        self.play(Write(eq_text))
        self.sub(1)

        # 每个不等都都是对变量间差值的约束,
        self.subtitle("每个不等式都是对变量间差值的约束")
        self.play(
            Indicate(equations[1]),
            Indicate(equations[4]),
            Indicate(equations[8]),
            run_time=2,
        )
        self.sub(0.5)
        # 因此得名差分约束系统
        self.subtitle("因此得名差分约束系统")
        self.sub(1)
        # 差分约束问题就是找出一组合法的解满足差分约束系统
        self.subtitle('差分约束问题就是找出一组合法的解')
        self.play(
            Indicate(var),
            run_time=2,
        )
        self.sub(0.5)
        self.subtitle("满足差分不等式组")
        self.play(
            Indicate(equations),
            run_time=2,
        )
        self.sub(0.5)
        self.subtitle("观众们可以暂停自己写几个例子, 这并不是几个公式就可以求解的问题, 感受到了吗?")
        self.sub(1)
        # 唔, 观众们可以暂停自己写几个例子, 这并不是一个简洁的公式就可以求解的问题, 感受到了吗?
        # 当变量个数很少的时候, 手算便可以轻松得到解答
        self.subtitle("当变量个数很少的时候, 手算就可以解答")
        # var_and_eq = var_group + eq_group
        # self.play(
        #     var_and_eq.animate.shift(UP)
        # )
        # three = Integer(3)
        # six = Integer(6)
        # ten_thousand = Integer(10000)
        # hundred_thousand = Integer(100000)
        three = brace.get_text("3 variables")
        six = eq_brace.get_text("6 equations")
        ten_thousand = brace.get_text("10000 variables")
        hundred_thousand = eq_brace.get_text("1000000 equations")

        # three.move_to(text)
        # six.move_to(eq_text)
        # ten_thousand.move_to(text)
        # hundred_thousand.move_to(eq_text)
        # three.next_to(brace, UP)
        # six.next_to(eq_brace, RIGHT)
        # ten_thousand.next_to(brace, UP)
        # hundred_thousand.next_to(eq_brace, RIGHT)

        self.play(ReplacementTransform(text, three))
        self.play(ReplacementTransform(eq_text, six))
        self.sub(1)

        # n_eq = MathTex("n=")
        # m_eq = MathTex("m=")
        # n_num = Integer(3, num_decimal_places=0)
        # m_num = Integer(5, num_decimal_places=0)
        # n_big_num = Integer(10000, num_decimal_places=0)
        # m_big_num = Integer(100000, num_decimal_places=0)
        # VGroup(n_eq, m_eq, n_num, m_num, n_big_num, m_big_num).scale(1)
        #
        # n_eq.next_to(equations, DOWN)
        # m_eq.next_to(n_eq, DOWN)
        # n_num.next_to(n_eq, RIGHT)
        # m_num.next_to(m_eq, RIGHT)
        #
        # self.play(ShowCreation(VGroup(n_eq, n_num)))
        # self.play(ShowCreation(VGroup(m_eq, m_num)))
        # 但是当变量个数增加的时候, 就需要依靠计算机来求解了
        self.subtitle("但是当变量个数增加的时候, 就需要依靠计算机来解答了")
        self.play(ReplacementTransform(three, ten_thousand))
        self.play(ReplacementTransform(six, hundred_thousand))
        self.sub(1)
        # self.play(
        #     VGroup(n_eq, m_eq, n_num, m_num).animate.shift(LEFT)
        # )
        #
        # n_big_num.next_to(n_eq, RIGHT)
        # m_big_num.next_to(m_eq, RIGHT)
        # self.play(ReplacementTransform(n_num, n_big_num),
        #           ReplacementTransform(m_num, m_big_num))
        # 但是计算机怎么求解呢?
        self.subtitle("但是计算机怎么求解呢?")
        self.sub(1)
        self.play(*[Uncreate(i) for i in self.get_mobject_family_members()])
        pass


class IntroductionToSolutionsOfSystemOfDifferenceConstraints(PikachuScene):
    """
    介绍差分约束系统的解法
    """

    def construct(self):
        # 显示
        # 还记得我们前面提到的最短路吗
        points = list(range(1, 7))
        edges = [(6, 3), (3, 1), (3, 5),
                 (5, 2), (2, 1),
                 (1, 4), (2, 4)]

        point_config = {}
        for p in points:
            point_config[p] = {"fill_color": RED}

        graph = Graph(points, edges, edge_type=Arrow,
                      labels=True, layout="spring",
                      layout_scale=4, vertex_config=point_config)

        ws = [10, 30, 5, 10, 1, 10, 15]
        for w, e in zip(ws, edges):
            edge = graph.edges[e]
            edge.num = self.add_num(edge, w)

        self.subtitle("还记得我们前面提到过的最短路吗")
        self.play(ShowCreation(graph),
                  *[ShowCreation(i.num) for i in graph.edges.values()],
                  run_time=2)
        self.sub(1)
        # 观众们还能选出6到1的最短路吗?
        self.subtitle("观众们还能选的出 6->1 的最短路吗? 暂停试试")
        self.sub(4)
        self.subtitle("6->1 的最短路如图所示↑")
        self.play(
            *[Indicate(i) for i in
              [graph.edges[j] for j in [(6, 3), (3, 5), (5, 2), (2, 1)]]],
            run_time=1,
        )
        self.sub(1)
        # 差分约束问题可以转化为最短路问题!
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
            r"x_{i_1}", r"-", r"x_{j_2}&\leqslant w_1\\",
            r"x_{i_2}", r"-", r"x_{j_2}&\leqslant w_2\\",
            r"\vdots&\\",
            r"x_{i_m}", r"-", r"x_{j_m}&\leqslant w_m\\",
        )
        eq_brace = Brace(equations, direction=RIGHT)
        eq_text = eq_brace.get_tex(r" ")

        eq_group = VGroup(equations, eq_brace, eq_text)
        var_and_eq = var_group + eq_group
        var_group.next_to(equations, UP)
        equal = MathTex(r"\iff{}")

        graph_group = VGroup(graph, *[i.num for i in graph.edges.values()])

        self.subtitle("抽象的差分约束问题却可以转换为直观的最短路问题")
        self.play(graph_group.animate.to_edge(LEFT))

        equal.next_to(graph_group, RIGHT)
        self.play(Write(equal))
        var_and_eq.next_to(equal)
        self.play(ShowCreation(var_and_eq))
        self.sub(1)
        # 先给出一个小小的提示,
        self.subtitle("先给出一个小小的提示")
        self.sub(1)
        # 运用最短路的以下条件(dis[x]代表x到起点的最短路, w[a,b]代表边权)
        self.subtitle("想想最短路为什么是最短路?")
        self.play(*[Uncreate(i) for i in var_and_eq + equal])
        self.play(graph_group.animate.move_to(ORIGIN))
        self.sub(1)
        # 不妨设 dis[x] 代表6号节点到x节点的最短路
        dis1 = MathTex(r'\text{dis}_1=')
        dis1_num = Integer(26)
        dis1.next_to(graph, DOWN).shift(LEFT)
        dis1_num.next_to(dis1, RIGHT)

        self.subtitle("不妨设 dis[x] 代表 6 号节点到 x 节点的最短路, dis[1] 如图所示")
        self.play(ShowCreation(dis1),
                  ReplacementTransform(VGroup(*[graph.edges[j].num.copy() for j in
                                                [(6, 3), (3, 5), (5, 2), (2, 1)]]), dis1_num), run_time=2)
        self.wait()
        self.play(Uncreate(dis1_num))
        self.sub(1)
        # 根据最短路的定义, 最短路显然比其他的路径短
        self.subtitle("根据最短路的定义, 最短路显然比其他的路径短")
        # 因此, dis[1]<=dis[3]+w[3,1]
        dis3 = MathTex(r"\text{dis}_3")
        w31 = MathTex(r"w_{3\to 1}")
        leq = MathTex(r"\leqslant{}")
        plus = MathTex(r"+")
        dis1_new = MathTex(r"\text{dis}_1")
        equ1 = VGroup(dis1_new, leq, dis3, plus, w31)
        equ1.arrange(RIGHT)
        equ1.next_to(graph, DOWN)
        self.play(ReplacementTransform(dis1, dis1_new))
        self.play(Write(leq))
        self.sub(1)
        self.subtitle('因此, dis[1]<=dis[3]+w[3,1]')
        self.play(  # ShowCreation(dis3),
            ReplacementTransform(graph.edges[(6, 3)].num.copy(), dis3),
            run_time=2)
        self.play(Write(plus))
        self.play(  # ShowCreation(w31),
            ReplacementTransform(graph.edges[(3, 1)].num.copy(), w31),
            run_time=2)
        self.sub(1)
        # 观众们可以暂停视频思考一下
        self.subtitle('如何利用这个等式呢? 观众们可以暂停思考一下')
        self.sub(3)
        # 观众们可能已经发现了,
        # 这个等式和差分约束系统的不等式十分相似,
        self.subtitle('观众们可能已经发现了')
        iff = MathTex(r"\iff{}")
        equ2 = MathTex(
            r"\text{dis}_3",
            r"-",
            r"\text{dis}_1",
            r"\leqslant{}",
            r"w_{3\to1}",
        )
        leftrightarrow = MathTex(r"\leftrightarrow{}")
        eq3 = MathTex(
            r"x_3",
            r"-",
            r"x_1",
            r"\leqslant{}",
            r"w_{3\to1}",
        )
        equ1_new = equ1.copy()
        equ4 = VGroup(equ1_new, iff, equ2, leftrightarrow, eq3)
        equ4.arrange(RIGHT)
        equ4.next_to(graph, DOWN)
        self.play(ReplacementTransform(equ1, equ1_new))
        self.play(ShowCreation(VGroup(iff, equ2)))
        self.sub(1)
        self.subtitle("这个不等变形之后, 和差分约束系统的不等式非常像")
        self.play(ShowCreation(VGroup(leftrightarrow, eq3)))
        self.sub(1)
        # 因此我们可以用节点和边权来模拟变量和约束,
        self.subtitle("因此我们可以用节点和边权来模拟变量和约束")
        # 对于每一个约束 x_i-x_j<=w_i
        self.play(Uncreate(equ1_new), Uncreate(iff))
        self.play(Uncreate(graph_group))
        self.sub(0.5)

        eq5 = VGroup(equ2, leftrightarrow, eq3)
        eq5.arrange(RIGHT)
        self.subtitle("对每一个约束 xi-xj<=wi")
        self.play(eq5.animate.move_to(ORIGIN))
        self.play(eq5.animate.shift(2 * UP))

        updownarrow = MathTex(r"\updownarrow{}")
        updownarrow.next_to(eq5, DOWN)
        self.play(Write(updownarrow))
        self.sub(1)
        # 从节点 j 和节点 i 之间连接一条边权为 w_i 的边
        two_node = Graph(["i", "j"], [("j", "i")], labels=True, edge_type=Arrow, layout_scale=1)
        e = two_node.edges[("j", "i")]
        e.num = self.add_num(e, "w")
        two_group = VGroup(two_node, e.num)
        eq6 = MathTex(r"x_i-x_j\leqslant w")

        sol = VGroup(eq6, leftrightarrow.copy(), two_group)
        sol.arrange(RIGHT)
        sol.next_to(updownarrow, DOWN)
        self.subtitle("从节点 j 向节点 i 之间连接一条边权为 wi 的边")
        self.play(ShowCreation(sol), run_time=1)
        self.sub(1)
        # 当然了, 由于差分约束系统存在多解, 因此我们还需要想办法来约束解以便得到一组特解
        # 观众们不妨暂停视频再想一想
        # 我们可以添加一个新的 0 号节点, 并且向每个点连一条权重为 0 的边
        # 这个做法相当于规定差分约束系统中最大的变量的值为 0
        # 接下来用之前提到过的算法求解出最短路, 便可以得到一组特解了, 特解就是 x_i = dis[i]
        self.subtitle("当然了, 由于差分约束系统存在多解, 因此我们还需要想办法来约束解得到一组特解")
        self.sub(1)
        self.subtitle("观众们不妨暂停视频再想一想")
        self.sub(3)
        self.subtitle("想到了吗?")
        self.sub(1)
        self.subtitle("我们可以添加一个新的 0 号节点, 并且向每个点连一条权重为 0 的边")
        self.sub(1)
        self.subtitle("这个做法相当于规定差分约束系统中最大的变量的值为 0")
        self.play(*[Uncreate(i) for i in self.get_mobject_family_members()], run_time=2)
        self.sub(1)
        answer = MathTex(
            r"\text{dis}_1&=x_1\\",
            r"\text{dis}_2&=x_2\\",
            r"\vdots&\\",
            r"\text{dis}_n&=x_n",
        )
        self.subtitle('这样, 用之前提到过的算法求解出最短路, 便可以得到一组特解了')
        self.play(Write(answer))
        self.sub(1)
        # 就这样, 一个数学上的问题转化为了一个图论中的问题, 并且得到了良好的解答
        self.subtitle("这样, 一个数学上的问题就转化为了一个最短路的问题, 并且得到了良好的解答")
        self.sub(1)
        # 当然, 差分约束系统还有一些扩展, 所以最后留一些思考题给大家, 大家可以思考如何讲这些问题转化为差分约束问题
        self.subtitle("当然, 差分约束系统还有一些拓展, 最后留一些思考题给大家\n大家可以思考如何将这些问题转化为差分约束问题")
        # x_a-x_b>=c
        # x_a=x_b
        # x_i/x_j<=c_k
        question = MathTex(
            r"x_a-x_b&\geqslant{}w\\",
            r"x_a&=x_b\\",
            r"{x_i\over x_j}&\leqslant{} w",
        )
        self.play(ReplacementTransform(answer, question))
        self.sub(3)
        self.play(*[Uncreate(i) for i in self.get_mobject_family_members()])
        pass


class Bilibili(PikachuScene):
    """
    求三连的界面
    """
    CONFIG = {
        "favo_svg": r"asset\favo.svg",
        "good_svg": r"asset\good.svg",
        "coin_svg": r"asset\coin.svg",
        "blue_brown_svg": r"asset\3b1b_vector_logo.png",
    }

    def construct(self):
        # object
        favo = SVGMobject(self.favo_svg)
        coin = SVGMobject(self.coin_svg)
        good = SVGMobject(self.good_svg)
        three = VGroup(good, coin, favo)
        three.arrange(RIGHT, buff=1.0)

        banner = ManimBanner().scale(0.3)
        blue_brown = ImageMobject(self.blue_brown_svg)
        blue_brown.set_height(banner.get_height())
        thanks = Group(banner, blue_brown)
        thanks.arrange(RIGHT)

        three.set_height(banner.get_height())
        thanks.scale(2)

        # 显示
        # 假如你觉得我们的视频不错的话,
        # 求点赞求投币求收藏
        self.subtitle("假如你觉得我们的视频不错的话, 求点赞求投币求收藏, 可以一键三连呀!")
        self.play(ShowCreation(three))
        for item in three:
            self.play(
                Indicate(item, color=PINK)
            )
        self.play(
            three.animate.shift(2 * UP),
        )
        self.sub(1)
        self.subtitle("同时, 本视频由 Manim 生成, 感谢 3B1B, Manim 社区对该软件的开发维护!")
        thanks.next_to(three, DOWN)
        self.play(FadeIn(thanks))
        self.play(banner.expand())
        self.sub(0.5)
        self.subtitle("感谢观看!")

        # 感谢观看!
        # 同时展示3Blue1Brown和Manim的Banner
        self.tear_down()
        pass


class Video(Begin, BeginTitle, RealityShortestPath, IntroductionToGraph, IntroudctionToSystemOfDifferenceConstraints,
            IntroductionToSolutionsOfSystemOfDifferenceConstraints, Bilibili):
    CONFIG = {

    }

    def __init__(self, *args, **kwargs):
        self.CONFIG.update(Begin.CONFIG)
        self.CONFIG.update(BeginTitle.CONFIG)
        self.CONFIG.update(RealityShortestPath.CONFIG)
        self.CONFIG.update(IntroductionToGraph.CONFIG)
        self.CONFIG.update(IntroudctionToSystemOfDifferenceConstraints.CONFIG)
        self.CONFIG.update(IntroductionToSolutionsOfSystemOfDifferenceConstraints.CONFIG)
        self.CONFIG.update(Bilibili.CONFIG)
        Begin.__init__(self, *args, **kwargs)
        BeginTitle.__init__(self, *args, **kwargs)
        RealityShortestPath.__init__(self, *args, **kwargs)
        IntroductionToGraph.__init__(self, *args, **kwargs)
        IntroudctionToSystemOfDifferenceConstraints.__init__(self, *args, **kwargs)
        IntroductionToSolutionsOfSystemOfDifferenceConstraints.__init__(self, *args, **kwargs)
        Bilibili.__init__(self, *args, **kwargs)
        Scene.__init__(self, *args, **kwargs)
        self.time = 0

    def construct(self):
        self.add_sound(r"asset/Nocturne in E flat major, Op. 9 no. 2.mp3")
        Begin.construct(self)
        BeginTitle.construct(self)
        RealityShortestPath.construct(self)
        IntroductionToGraph.construct(self)
        IntroudctionToSystemOfDifferenceConstraints.construct(self)
        IntroductionToSolutionsOfSystemOfDifferenceConstraints.construct(self)
        Bilibili.construct(self)
        pass


class LabeledModifiedGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3,
                  labels=True, vertex_config={7: {"fill_color": RED}},
                  edge_config={(1, 7): {"stroke_color": RED},
                               (2, 7): {"stroke_color": RED},
                               (4, 7): {"stroke_color": RED}})
        self.play(*[FadeIn(i) for i in g.edges.values()])
        self.play(*[FadeIn(i) for i in g.vertices.values()])
        self.play(*[FadeOut(i) for i in g.family_members_with_points()])
        # print(g.get_family())


class ArcPolygonExample2(Scene):
    def construct(self):
        arc_conf = {"stroke_width": 3, "stroke_color": BLUE,
                    "fill_opacity": 0.5, "color": GREEN}
        poly_conf = {"color": None}
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        arc2 = ArcBetweenPoints(c, a, radius=2, stroke_color=RED)
        reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, **poly_conf)
        self.play(FadeIn(reuleaux_tri))
        dot = Dot()
        self.play(MoveAlongPath(dot, reuleaux_tri), run_time=5)
        self.wait(2)
