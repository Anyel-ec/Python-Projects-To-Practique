def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Si el elemento no se encuentra en el arreglo

# Ejemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(arr, target)

if result != -1:
    print(f"El elemento {target} fue encontrado en la posición {result}.")
else:
    print(f"El elemento {target} no fue encontrado en el arreglo.")
