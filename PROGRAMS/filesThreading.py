import threading

def read_file(filename, results, lock):
    with open(filename, 'r') as file:
        content = file.read()
        with lock:
            results.append(content)

def main():
    input_files = ["file.txt", "  file1.txt  ", "file2.txt"]
    results = []
    lock = threading.Lock()
    threads = []

    for filename in input_files:
        thread = threading.Thread(target=read_file, args=(filename, results, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    with open("fileMerged.txt", 'w') as output_file:
        for result in results:
            output_file.write(result)

if __name__ == "__main__":
    main()

