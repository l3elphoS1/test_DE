def sum_of_array(arr, inputs):
    prefix_sum = [0]  # เริ่มต้นด้วย 0 เพื่อคำนวณสะสม
    result = []
    
    # สร้าง prefix sum
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)

    # คำนวณผลบวกในช่วงที่กำหนด
    for a, b in inputs:
        # ใช้ค่าจาก prefix_sum คำนวณผลบวกในช่วง (a-1) ถึง (b)
        result.append(prefix_sum[b] - prefix_sum[a - 1])

    return result


arr = [1, 2, 3, 4, 1]
inputs = [[1, 3], [3, 3], [4, 5]]

output = sum_of_array(arr, inputs)
print(output)