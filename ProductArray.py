def productexceptself(array):
    n = len(array)
    Product = 1
    right = [1] * len(array)
    for i in range(len(array) - 2,-1,-1):
        Product *= array[i+1]
        right[i] = Product
    Product = 1
    for i in range(1,len(array)):
        Product *= array[i-1]
        right[i] *= Product
        
    
    return right



print(productexceptself([1,2,3,4]))
#[24,12,8,6]
