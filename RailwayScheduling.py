def min_platforms(arr, dep):
    arr.sort()
    dep.sort()
    i=j=0
    plat=ans=0
    
    while i < len(arr):
        if arr[i] <= dep[j]:
            plat += 1
            ans = max(ans, plat)
            i += 1
        else:
            plat -= 1
            j += 1
    return ans

print(min_platforms([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000]))
