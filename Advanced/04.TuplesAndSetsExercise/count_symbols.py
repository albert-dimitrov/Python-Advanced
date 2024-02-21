symbols = tuple([x for x in input()])
unique_symbols = set(symbols)
symbols_use = {}
for symbol in unique_symbols:
    symbols_use[symbol] = symbols.count(symbol)

sorted_symbol = sorted(symbols_use.items(), key=lambda x: x)
for index in range(len(sorted_symbol)):
    print(f'{sorted_symbol[index][0]}: {sorted_symbol[index][1]} time/s')
