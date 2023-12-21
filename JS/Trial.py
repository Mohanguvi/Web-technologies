N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

is_mirror_image = arr1 == arr2[::-1]

if is_mirror_image:
    print("yes")
else:
    print("no")





