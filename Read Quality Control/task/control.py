# write your code here
import gzip
from collections import Counter


def average(lst, rounds=0):
    mean = sum(lst) / len(lst)
    return round(mean, rounds)


def get_reads(txt):
    txts = txt.split("\n")
    return [txts[i] for i in range(len(txts)) if i % 4 == 1]


def count_repeat(counts):
    repeats = 0
    for i in counts.keys():
        repeats += counts[i] - 1
    return repeats


def get_percentage(N_string, *args):
    counts = Counter(N_string)
    try:
        gct = sum([counts[i] for i in args]) * 100 / len(N_string)
    except:
        gct = 0
    return gct


def exist_num(lst, test):
    num = 0
    for i in lst:
        if test in i:
            num += 1
    return num


class DataFastq():

    def __init__(self, path):
        with gzip.open(path, 'r') as f:
            content = f.read().decode('utf-8')
        self.content = content
        self.reads = get_reads(self.content)
        self.reads_with_N = exist_num(self.reads, 'N')
        self.repeats = count_repeat(Counter(self.reads))
        self.GCs = [get_percentage(i, "G", "C") for i in self.reads]
        self.GC_content = average(self.GCs, 2)
        self.Ns = [get_percentage(i, "N") for i in self.reads]
        self.N_content = average(self.Ns, 2)

    def output(self):
        print(f"Reads in the file = {len(self.reads)}")
        length = [len(i) for i in self.reads]
        print(f"Reads sequence average length = {average(length)}")
        print("\n")
        print(f"Repeats = {self.repeats}")
        print(f"Reads with Ns = {self.reads_with_N}")
        print("\n")
        print(f"GC content average = {self.GC_content}%")
        print(f"Ns per read sequence = {self.N_content}%")


def main():
    data1 = DataFastq(input())
    data2 = DataFastq(input())
    data3 = DataFastq(input())
    lst = [data1, data2, data3]
    target = min(lst,key = lambda x: x.reads_with_N)
    target.output()


if __name__ == "__main__":
    main()
