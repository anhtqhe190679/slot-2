def find_nearest_to_average(arr):
    average = sum(arr) / len(arr)
    nearest_element, position = arr[0], 1

    for i in range(1, len(arr)):
        if abs(arr[i] - average) < abs(nearest_element - average):
            nearest_element = arr[i]
            position = i + 1 

    return position

def main():
    input_str = input("Nhập giá trị của dãy: ")
    array = list(map(int, input_str.split()))
    position = find_nearest_to_average(array)
    print(f"Vị trí của phần tử gần trung bình nhất là: {position}")

if __name__ == "__main__":
    main()