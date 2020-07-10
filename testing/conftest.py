import pytest


@pytest.fixture()
def calcu():
    print("开始计算")
    #yield 激活fixture teardown方法
    yield
    print("计算结束")