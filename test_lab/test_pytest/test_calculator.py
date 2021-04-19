import pytest
import yaml

from Calculator import Calculator

"""
类里面的（setup/teardown）运行在调用方法的前后，setup_method/teardown_method的简写
方法级（setup_method/teardown_method）运行在调用方法的前后
类级(setup_class/teardown_class) 只在类中前后运行一次
函数级(setup_function/teardown_function) 只对函数用例生效（不在类中）
模块级(setup_module/teardown_module) 模块始末，全局的（优先最高）
"""

def get_datas(name,type='int'):
    with open("./datas/calc.yaml") as f:
        # safe_load 将 yaml 数据流转换为 python 对象
        # safe_dump 将 python 对象转换为 yaml 数据流
        all_datas=yaml.safe_load(f)
    datas = all_datas[name][type]["datas"]
    ids = all_datas[name][type]["ids"]
    return (datas,ids)

class TestCalc:
    # 变量后加:类型提示作用
    # datas:list = get_datas()
    add_int_data = get_datas("add","int")
    add_float_data = get_datas("add", "float")
    div_int_data = get_datas("div","int")
    div_zero_data = get_datas("div", "zero")

    # 前置条件
    def setup(self):
        print("开始计算")
        # 实例变量
        self.calc = Calculator()

    def teardown(self):
        print("结束计算")

    @pytest.mark.add_normal
    # 参数化每一条用例是独立的，某一条失败不影响其他条
    @pytest.mark.parametrize("a,b,result",add_int_data[0],ids=add_int_data[1])
    def test_add(self,a,b,result):
        print(a,b,result)
        assert result==self.calc.add(a,b)

    @pytest.mark.add_float
    @pytest.mark.parametrize("a,b,result",add_float_data[0],ids=add_float_data[1])
    def test_add_float(self,a,b,result):
        assert result == round(self.calc.add(a,b),2)


    @pytest.mark.div
    @pytest.mark.parametrize("a,b,result",div_int_data[0],ids=div_int_data[1])
    def test_div(self,a,b,result):
        assert result==self.calc.div(a,b)

    @pytest.mark.div_zero
    @pytest.mark.parametrize("a,b,result", div_zero_data[0], ids=div_zero_data[1])
    def test_div(self, a, b, result):
        with pytest.raises(ZeroDivisionError):
            result = a / b



