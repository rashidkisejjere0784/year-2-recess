

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Example usage
with FileManager('example.txt', 'w') as file:
    file.write('Hello, world!')



import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

# Example usage
with DatabaseManager('example.db') as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)



import threading
import multiprocessing
import time

# Function to execute
def execute_function(name, duration):
    print(f"Executing function {name} for {duration} seconds")
    time.sleep(duration)
    print(f"Function {name} execution complete")

# List of functions with their corresponding durations
function_data = [
    ("Function 1", 2),
    ("Function 2", 4),
    ("Function 3", 1),
    ("Function 4", 3)
]

# Multi-threading algorithm
def run_with_threads():
    threads = []

    for name, duration in function_data:
        thread = threading.Thread(target=execute_function, args=(name, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Multi-processing algorithm
def run_with_processes():
    processes = []

    for name, duration in function_data:
        process = multiprocessing.Process(target=execute_function, args=(name, duration))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# Run the functions using threads
print("Running with threads...")
run_with_threads()

# Run the functions using processes
print("\nRunning with processes...")
run_with_processes()
