n_str = input()
n_int = int(n_str)

mod_num = n_int % 998244353

length = len(n_str)
mod_factor = pow(10, length * n_int, 998244353)

result = (
    mod_num * (mod_factor - 1) * pow(10**length - 1, 998244351, 998244353)
) % 998244353

print(result)
