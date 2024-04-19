def fibo(n):
    # Casos base
    f = [0, 1]
    # Caso general
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f

if __name__ == '__main__':
    n = 5
    f = fibo(n)
    print(f"La secuencia de fibonacci para n = {n} es {f}")
