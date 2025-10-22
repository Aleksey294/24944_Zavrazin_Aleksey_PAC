import numpy as np
import argparse

def read_file(filename):
    with open(filename, "r") as f:
        return np.array(list(map(int, f.read().split())))

#np.random.choice + np.where
def mix_method_1(real, synthetic, P):
    mask = np.random.choice([0, 1], size=len(real), p=[1 - P, P])
    return np.where(mask, synthetic, real)

#генерация массива случайных чисел и сравнение с вероятностью
def mix_method_2(real, synthetic, P):
    mask = np.random.rand(len(real)) < P
    return np.where(mask, synthetic, real)

#биномиальное распределение
def mix_method_3(real, synthetic, P):
    mask = np.random.binomial(1, P, size=len(real))
    result = real.copy()
    result[mask == 1] = synthetic[mask == 1]
    return result


def main():
    parser = argparse.ArgumentParser(description="Смешивание реальных и синтетических данных с вероятностью P.")
    parser.add_argument("file1", type=str, help="Путь к файлу с реальными данными")
    parser.add_argument("file2", type=str, help="Путь к файлу с синтетическими данными")
    parser.add_argument("P", type=float, help="Вероятность выбора синтетических данных (0 <= P <= 1)")
    parser.add_argument("--method", type=int, choices=[1, 2, 3], default=1, help="Номер метода (1, 2 или 3)")
    args = parser.parse_args()

    real = read_file(args.file1)
    synthetic = read_file(args.file2)


    if args.method == 1:
        mixed = mix_method_1(real, synthetic, args.P)
    elif args.method == 2:
        mixed = mix_method_2(real, synthetic, args.P)
    else:
        mixed = mix_method_3(real, synthetic, args.P)

    print("Результат (метод {}):".format(args.method))
    print(" ".join(map(str, mixed)))


# ---------- Точка входа ----------
if __name__ == "__main__":
    main()
