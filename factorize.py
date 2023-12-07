from multiprocessing import Pool, cpu_count

from time import time, sleep


def factorize(*number):
    total_res = []
    for num in number:
        result = []
        for i in range(1, num + 1):
            if not num % i:
                result.append(i)
        total_res.append(result)
    return total_res


if __name__ == "__main__":
    start = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    sleep(0.5)
    end = time()
    print(f"Час виконання синхронної функції: {end - start} сек.")  # 1.16

    with Pool(cpu_count()) as p:
        start = time()
        p.map_async(factorize, (128, 255, 99999, 10651060))
        sleep(0.5)
        end = time()
        print(f"Час виконання оптимізованого варіанту: {end - start} сек.")  # 0.5003
        p.close()
        p.join()

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]
