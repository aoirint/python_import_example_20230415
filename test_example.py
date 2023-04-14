def test_utility_hoge_execute_hoge():
    import example.utility as utility
    utility.hoge.execute_hoge()

def test_utility_fuga_execute_fuga():
    import example.utility as utility
    utility.fuga.execute_fuga()

def test_hoge_execute_hoge():
    import example.utility.hoge as hoge
    hoge.execute_hoge()

def test_fuga_execute_fuga():
    import example.utility.fuga as fuga
    fuga.execute_fuga()

def test_execute_hoge():
    from example.utility.hoge import execute_hoge
    execute_hoge()

def test_execute_fuga():
    from example.utility.fuga import execute_fuga
    execute_fuga()
