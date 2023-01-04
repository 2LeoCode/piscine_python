from subprocess import run, PIPE, DEVNULL


def test(args: 'list[str]', expected: str):
    res = (
        run(["python", "exec.py"] + args, stdout=PIPE, stderr=DEVNULL)
        .stdout.decode()
    )
    print("[OK]" if res == expected else "[KO]")


test(["Hello World!"], "!DLROw OLLEh\n")
test(["Hello", "my Friend"], "DNEIRf YM OLLEh\n")
test(["!DLROW", "OLLEh"], "Hello world!\n")
test(["Hello", "world!", "aBc", "123"], "321 CbA !DLROW OLLEh\n")
test([], "")
