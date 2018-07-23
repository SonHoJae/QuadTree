
def binary_direction(left, right, down, up, lat, long, depth=1):
    location = ''
    for idx in range(depth):
        if idx % 2 == 0:
            mid = (left + right)/ 2
            if lat > mid:
                location +='1'
                left = mid
            else:
                location += '0'
                right = mid
        else:
            mid = (down + up) / 2
            if long > mid:
                location += '1'
                down = mid
            else:
                location += '0'
                up = mid
    return location
