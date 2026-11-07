# test.py
import pytest

# 用例1：简单相等断言
def test_add():
    a = 2
    b = 3
    assert a + b == 4

# 用例2：判断包含
def test_string_contains():
    text = "hello robot & pytest"
    assert "pytest1" in text

# 用例3：预期失败示例（判断数字大于）
def test_number_greater():
    assert 10 > 1
