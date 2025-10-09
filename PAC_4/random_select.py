import numpy as np
import argparse

def read_file(filename):
    with open(filename, "r") as f:
        return np.array(list(map(int, f.read().split())))

def random_select():
    parser = argparse.ArgumentParser(description="Смешивание реальных и синтетических данных с вероятностью P.")
    parser.add_argument("file1", type=str, help="Путь к файлу с реальными данными")
    parser.add_argument("file2", type=str, help="Путь к файлу с синтетическими данными")
    parser.add_argument("P", type=float, help="Вероятность выбора синтетического элемента (0 <= P <= 1)")
    args = parser.parse_args()
    
    data_real = read_file(args.file1)
    data_synthetic = read_file(args.file2)
    
    return np.where(np.random.choice([0, 1], size=len(data_real), p=[1 - args.P, args.P]), data_synthetic, data_real)

print(random_select())