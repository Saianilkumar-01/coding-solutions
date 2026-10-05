def search_insert_position(arr, n, k):
    # Write your code here
    l = 0
    h = n - 1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            l = mid+ 1
        else:
            h = mid - 1
    else:
        return l