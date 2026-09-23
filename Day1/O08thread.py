"""
Concepts used in this example:
1. Threading: multiple tasks run concurrently in the same process.
2. Thread target: function executed by each thread.
3. Concurrency: threads can run in parallel depending on CPU and OS scheduling.
4. join(): waits for a thread to finish before continuing the main program.
"""

import time
import threading


# Each thread executes its own function independently.
def list_square(lst):
    tid = threading.get_native_id()
    for num in lst:
        time.sleep(1)
        print(f"{num}^2", num ** 2, f"tid = {tid}", sep="\t:\t")


def list_cubed(lst):
    tid = threading.get_native_id()
    for num in lst:
        time.sleep(1)
        print(f"\t\t\t\t{num}^3", num ** 3, f"tid = {tid}", sep="\t:\t")


if __name__ == "__main__":
    tid = threading.get_native_id()
    print(f"\t\tMain thread started : {tid}")
    t1 = threading.Thread(target=list_square, args=([1, 2, 3, 4, 5],))
    t2 = threading.Thread(target=list_cubed, args=([1, 2, 3, 4, 5, 6, 7, 8],))
    t1.start()
    t2.start()
    for n in range(1, 5):
        print(f"\t\tmain thread running with n = {n} : tid = {tid}")
        time.sleep(1)
    t1.join()
    t2.join()
