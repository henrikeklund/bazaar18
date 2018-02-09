from ws_assert_try import mean

def test_ints():
    num_list=[1,2,3,4,5]
    abs=mean(num_list)
    exp=3
    assert abs==exp
    
def test_double():
    num_list=[1,2,3,4]
    abs=mean(num_list)
    exp=2.5
    assert abs==exp
    
def test_long():
    big=100000000
    abs=mean(range(1,big))
    exp=big/2.0
    assert abs==exp