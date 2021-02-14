from blockchain import Blockchain

a = Blockchain()

a.mine("sample.jpg")
a.mine("sample1.jpg")
a.mine("sample2.jpg")


a.traverse()

print("------------------------------------------------------------------------------------------")

print(a.search("sample.jpg"))
print("------------------------------------------------------------------------------------------")
print(a.search("sample1.jpg"))
print("------------------------------------------------------------------------------------------")
print(a.search("sample2.jpg"))