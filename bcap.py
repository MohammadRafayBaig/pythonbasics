# arr=list(map(int,input("Enter the list").split()))

# target=int(input("Enter the targeted value "))

# found=False

# for i in range(len(arr)):
#     if arr[i]==target:
#         print("Targeted elements is founded=",i)
#         found=True
#         break
    
# if not found:
#     print("Targeted element is not founded")
    



for i in range(1,10):
    if i == 5:
        break
    print(i)
    
for i in range(1,10):
    if i == 5:
        continue
    print(i)