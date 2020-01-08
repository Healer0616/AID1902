import unittest
from Cal.Cal import cal
from HTMLTestRunner import HTMLTestRunner


class test_cal(unittest.TestCase):
    def setUp(self):
        print("开始测试")
        self.cal = cal()

    def test_add(self):
        print("加法测试")
        assert self.cal.add(2, 3) == 5

    def test_cheng(self):
        print("乘法测试")
        self.assertEqual(20, self.cal.cheng(4, 5))

    def test_jian(self):
        print("减法测试")
        self.assertEqual(5, self.cal.jian(10, 5))

    def test_chu(self):
        print("除法测试")
        self.assertEqual(4, self.cal.chu(12, 3))

    def tearDown(self):
        print("结束测试")


if __name__ == 'test_cal':
    # unittest.main()
    cs = unittest.TestSuite()
    cs.addTest(test_cal("test_cheng"))
    cs.addTest(test_cal("test_chu"))
    # cs.addTests((test_cal("test_add"), test_cal("test_chu")))
    # runner = unittest.TextTestRunner()
    with open("report.html", "wb") as f:
        runner = HTMLTestRunner(
            stream=f,
            title="计算器测试报告",
            description="测试详情明细"
        )
        runner.run(cs)

