from solution import solution_1, solution_2, solution_3, solution_4, solution_5


class TestSolutions:

    def setup(self):
        self.res_1 = solution_1(50)
        self.res_2 = solution_2(50)
        self.res_3 = solution_3(50)
        self.res_4 = solution_4(50)
        self.res_5 = solution_5(50)

    def test_out_uniq_1(self):
        assert len(self.res_1) == len(set(self.res_1))

    def test_out_uniq_2(self):
        assert len(self.res_2) == len(set(self.res_2))

    def test_out_uniq_3(self):
        assert len(self.res_3) == len(set(self.res_3))

    def test_out_uniq_4(self):
        assert len(self.res_4) == len(set(self.res_4))

    def test_out_uniq_5(self):
        assert len(self.res_5) == len(set(self.res_5))

    def test_out_len_eq(self):
        assert len(self.res_1) == len(self.res_2) == \
               len(self.res_3) == len(self.res_4) == len(self.res_5)

    def test_out_equals(self):
        set_1 = set(self.res_1)
        set_2 = set(self.res_2)
        set_3 = set(self.res_3)
        set_4 = set(self.res_4)
        set_5 = set(self.res_5)
        assert len(set_1 ^ set_2) == len(set_1 ^ set_3) == \
               len(set_1 ^ set_4) == len(set_1 ^ set_5) == 0
