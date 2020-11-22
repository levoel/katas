def growing_plant(upSpeed, downSpeed, desiredHeight):
    if upSpeed >= desiredHeight:
        return 1
    return int(1 + (desiredHeight - upSpeed) / (upSpeed - downSpeed) + bool((desiredHeight - upSpeed) % (upSpeed - downSpeed)))

# OR

def growing_plant(upSpeed, downSpeed, desiredHeight):
    from math import ceil

    return max(ceil((desiredHeight - downSpeed) / (upSpeed - downSpeed)), 1)
