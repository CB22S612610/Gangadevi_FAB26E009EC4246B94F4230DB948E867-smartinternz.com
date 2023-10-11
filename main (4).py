def linearsearchproduct(product_list,
targetproduct):
  indices=[]
  for index,product in enumerate(product_list):
   if product==targetproduct:
     indices.append(index)
  return indices 
products=["shoes","boot","loafer","shoes","sandal","shoes"]def
target1="shoes"
target2='boot'
result=linearsearchproduct(products,target1)
resut=linearsearchproduct(products,target2)
print(result, resut)