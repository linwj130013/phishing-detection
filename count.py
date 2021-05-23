count = dict()


def count_freq(url):
    for i in url:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1


def get_freq(symbol):
    if symbol in count:
        return count[symbol]
    else:
        return 0


def main():
    url = "https://www.sciencedirect.com/science/article/pii/S2352340920313202"
    count_freq(url)
    symbols = ['.', '-', '_', '/', '?', '=', '@', '&',
               '!', ' ', '~', ',', '+', '∗', '#', '$', '%']
    for symbol in symbols:
        print(symbol + ": " + str(get_freq(symbol)))


main()
