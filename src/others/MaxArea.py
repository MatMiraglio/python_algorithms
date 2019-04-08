def maxArea(height) -> int:
    left, right = 0, len(height) - 1
    max_volume = 0

    while left < right:
        current_volume = min((height[left], height[right])) * (right - left)

        if current_volume > max_volume:
            max_volume = current_volume

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_volume


values = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(maxArea(values))
