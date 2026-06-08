lis = [1,2,3,4,5,6,7,8,9] 
batch_size = 2

def batch_generator(batch_size,lis):
    for i in range(0,len(lis),batch_size):
        yield lis[i:i+batch_size]

x = batch_generator(batch_size,lis)
print(list(x))