def enough(cap, on, wait):
    seats = cap - on
    noteenough = wait - seats
    
    if seats >= wait:
        print(f"You can take them all!")
        return 0
    else:
        print(f"You can't take: {noteenough} passangers.")
        return noteenough