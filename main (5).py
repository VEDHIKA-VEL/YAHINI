def LinearSearchProduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate (productList):
    if product==targetProduct:
      indices.append(index)
  return indices
products=["shoes","boot","loafer","shoes","sandel","shoes"]
target="shoes"
result=LinearSearchProduct(products,target)
print(result)