import time 

def count():
    print("1")
    time.sleep(1)
    print("2")

def main():
    for _ in range(4):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() -s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")