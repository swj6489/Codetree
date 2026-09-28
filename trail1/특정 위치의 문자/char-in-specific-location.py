arr = ['L', 'E', 'B','R', 'O', 'S']

text = input()

for i in range(len(arr)):
    if text == arr[i]:
        print(i)

if text not in arr:
    print(None)