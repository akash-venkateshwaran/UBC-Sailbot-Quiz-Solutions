from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_basic2():
    assert bound_to_180(360) == 0


def test_bound_basic3():
    assert bound_to_180(180) == -180


def test_bound_basic4():
    assert bound_to_180(-180) == -180


def test_bound_basic5():
    assert bound_to_180(90) == 90


def test_bound_basic6():
    assert bound_to_180(-90) == -90


def test_bound_basic7():
    assert bound_to_180(990) == -90


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2) is True


def test_between_basic2():
    assert is_angle_between(10, 10, 2) is True


def test_between_inv1():
    assert is_angle_between(10, 1, -20) is True


def test_between_inv2():
    assert is_angle_between(-20, 1, 10) is True


def test_between_ext1():
    assert is_angle_between(90, 1, -90) is True


def test_between_ext2():
    assert is_angle_between(0, -90, -180) is True


def test_between_ext3():
    assert is_angle_between(0, 90, 180) is False


def test_between_ext4():
    assert is_angle_between(120, 180, -120) is True


def test_between_ext5():
    assert is_angle_between(180, 0, -180) is False
