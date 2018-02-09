#assert True==True
def mean(num_list):
    if len(num_list)==0:
        raise Exception('Cannot compute with list length = 0')
    else:
        return sum(num_list)/len(num_list)