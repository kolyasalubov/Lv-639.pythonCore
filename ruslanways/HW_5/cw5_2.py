def enough(cap, on, wait):
    # Your code here
    if on+wait <= cap:
        return 0
    else:
        return wait+on-cap
