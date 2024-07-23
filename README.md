# Python Parallel Programming: Processes vs. Threads

This project demonstrates the use of threads and processes in Python for handling I/O-bound and CPU-bound tasks. The examples include downloading files and performing CPU-intensive computations to highlight the performance differences between threading and multiprocessing.

## Features
- **Threading for I/O-bound Tasks**: Example of using threads to download files concurrently.
- **Multiprocessing for I/O-bound Tasks**: Example of using processes to download files concurrently.
- **Multiprocessing for CPU-bound Tasks**: Example of using processes to perform CPU-intensive computations.

- ## Introduction
This project evaluates the use of processes and threads in Python for parallel programming. It investigates their performance in both I/O-bound and CPU-bound tasks, providing insights into the Global Interpreter Lock (GIL) and its impact on threading in Python.

## Theoretical Understanding

### Processes and Threads
A process is an independent execution unit that contains its own state information, memory space, and program code. In contrast, a thread is a smaller execution unit that shares the memory space and state information of its parent process.

### Multiprocessing and Threading in Python
Python’s `multiprocessing` module allows for the creation of processes, enabling parallel execution of code. The `threading` module, on the other hand, allows for concurrent execution using threads within a single process.

### Global Interpreter Lock (GIL)
The GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes simultaneously. This means that in a multi-threaded Python program, only one thread can execute Python code at a time, which can be a bottleneck for CPU-bound tasks.

### Advantages and Disadvantages of Processes and Threads

#### Processes:
- **Advantages:** Independent memory space, no GIL impact, better for CPU-bound tasks.
- **Disadvantages:** Higher memory consumption, slower inter-process communication.

#### Threads:
- **Advantages:** Lower memory consumption, faster inter-thread communication, better for I/O-bound tasks.
- **Disadvantages:** GIL impact, shared memory space can lead to synchronization issues.

Performance Analysis
The project includes a basic performance analysis of threading and multiprocessing for different types of tasks. Results are printed to the console, showing the time taken for each approach.
