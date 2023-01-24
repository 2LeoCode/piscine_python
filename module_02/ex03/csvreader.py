from pandas import read_csv
from functools import partial

class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.__dict__.update(x for x in locals().items() if x[0] != 'self')

    def __enter__(self):
        cleanup_values = lambda x: x.strip(' "') if isinstance(x, str) else x
        if self.filename is None:
            raise ValueError("You must specify a filename")
        with open(self.filename, 'r') as file:
            self.csv_data = read_csv(
                file, delimiter=self.sep,
                skiprows=range(1, self.skip_top + 1),
                skipfooter=self.skip_bottom, engine='python'
            ).applymap(cleanup_values).rename(columns=cleanup_values)
            if not self.csv_data.notna().all().all():
                raise ValueError("CSV file is corrupted")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def getdata(self):
        return self.csv_data.values.tolist()

    def getheader(self):
        return self.csv_data.columns.tolist() if self.header else None

print_context = partial(print, "========== ", end=" ==========\n")
print_header = partial(print, "========== HEADER ==========\n")
print_data = partial(print, "========== DATA ==========\n", end="\n\n")
print_exception = partial(print, "EXCEPTION CAUGHT:", end="\n\n")

if __name__ == "__main__":
    print_context("good.csv header=False")
    with CsvReader("good.csv") as file:
        header = file.getheader()
        print_header(header)
        data = file.getdata()
        print_data(data)

    print_context("good.csv header=True, skip_top=8, skip_bottom=9")
    with CsvReader("good.csv", header=True, skip_top=8, skip_bottom=9) as file:
        header = file.getheader()
        print_header(header)
        data = file.getdata()
        print_data(data)

    print_context("bad.csv header=true, skip_top=1")
    try:
        with CsvReader("bad.csv", header=True, skip_top=1) as file:
            header = file.getheader()
            print_header(header)
            data = file.getdata()
            print_data(data)
    except Exception as e:
        print_exception(e)
    
    print_context("notexist.csv")
    try:
        with CsvReader("notexist.csv") as file:
            header = file.getheader()
            print_header(header)
            data = file.getdata()
            print_data(data)
    except Exception as e:
        print_exception(e)
