# Sock Merchant #

# John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
#  Given an array of integers representing the color of each sock, determine how many pairs of socks
#  with matching colors there are.


def sockMerchant(n, ar):
    socks, pairs = set(), 0
    for index in range(n):
        if ar[index] in socks:
            socks.remove(ar[index])
            pairs += 1
        else:
            socks.add(ar[index])
    return pairs


if __name__ == '__main__':
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20, ]), 3)
    print(sockMerchant(9, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]), 4)
