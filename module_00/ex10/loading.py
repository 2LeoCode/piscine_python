from time import perf_counter


def progress_info(iterable):
    start = perf_counter()
    before = start
    for i, item in enumerate(iterable):
        after = perf_counter()
        delta = after - before
        elapsed = after - start
        before = after
        yield (i, item, delta, elapsed)


def ft_progress(iterable):
    for (i, item, delta, elapsed) in progress_info(iterable):
        yield item
        print(
            f"\rETA: {delta * (len(iterable) - i - 1):>5.2f}s"
            f"[{(i + 1) / len(iterable) * 100:>3.0f}%]"
            f"[{'=' * int((i + 1) / len(iterable) * 20)}"
            f"{'>' if i < len(iterable) - 1 else ''}"
            f"{' ' * (19 - int((i + 1) / len(iterable) * 20))}] "
            f"{i + 1:>{len(str(len(iterable)))}} / {len(iterable)} "
            f"| elapsed time {elapsed:.2f}s", end=''
        )
    print()
