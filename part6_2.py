def sum_(cards, result):
    """
    
    sum all the number

    """
    for i in range(5):
        cards.append(input())

    for i in range(5):
        if cards[i] == "A":
            result += 1
        elif cards[i] == "J":
            result += 11
        elif cards[i] == "Q":
            result += 12
        elif cards[i] == "K":
            result += 13
        elif cards[i] == "10":
            result += 10
        else:
            result += eval(cards[i])

    print(result)


if __name__ == "__main__":
    cards = []
    result = 0
    sum_(cards, result)
