#测试文件
import sys
import yaml
import pytest

print(sys.path.append('..'))
from pythoncode.calc import Calculator

#模块级别
# def setup_module():
#     print("模块级别setup")
#
# def teardown_module():
#     print("模块级别teardown")

#函数级别 类外面的使用def 定义为函数，里面为方法
# def setup_function():
#     print("函数级别 setup")
#
# def teardown_function():
#     print("函数级别 teardown")


class TestCalc:

    def setup_class(self):
        self.cal = Calculator()


    # def teardown_class(self):
    #     print("类级别 teardown")

    #方法级别
    # def setup(self):
    #     print("开始计算")
    #
    # def teardown(self):
    #     print("计算结束")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data1.yaml")),ids=['int','minus','bigint','float']
                             )

    def test_add(self,a,b,result,calcu):
        assert result ==self.cal.add(a,b)

    @pytest.mark.sub
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data2.yaml")),ids=['int','minus','bigint','float']
                             )
    def test_sub(self,a,b,result,calcu):
        assert result == self.cal.sub(a,b)

    @pytest.mark.mul
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data3.yaml")),ids=['int','minus','bigint','float']
                             )
    def test_mul(self,a,b,result,calcu):
        assert result == self.cal.mul(a,b)

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("./data4.yaml")),ids=['int','minus','bigint','float']
                             )
    def test_div(self,a,b,result,calcu):
        assert result == self.cal.div(a,b)

