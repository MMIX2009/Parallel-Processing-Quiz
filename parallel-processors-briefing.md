# Briefing Document: Parallel Processors and Multithreading

## Executive Summary

This briefing document summarizes the key concepts discussed in the provided excerpts from a computer organization and design textbook, focusing on parallel processors and related hardware and software considerations. The main themes revolve around the motivation for parallel processing (increased performance, scalability, availability, power efficiency), the challenges of parallel programming, fundamental laws like Amdahl's Law that limit speedup, different approaches to parallel hardware (multiprocessors, multicore, vector processors, SIMD), and techniques for enhancing parallelism at the instruction level (multithreading, simultaneous multithreading). The document highlights the crucial interplay between hardware and software in achieving effective parallel processing.

## Main Themes and Important Ideas/Facts

### 1. Introduction to Parallel Processing

**Goal:** The primary motivation for using multiple computers or processors is to achieve higher performance. This encompasses various benefits:
- **Scalability:** The ability to increase performance by adding more resources.
- **Availability:** Increased reliability through redundancy.
- **Power Efficiency:** Potential for better performance per watt.
- **Multiprocessors:** Systems containing multiple processors.
- **Task-level (process-level) parallelism:** Executing independent jobs concurrently to achieve high throughput.
- **Parallel processing program:** A single program designed to run on multiple processors simultaneously.
- **Multicore microprocessors:** Single chips containing multiple processor cores.

### 2. Hardware and Software Interplay

The document distinguishes between serial (e.g., Pentium 4) and parallel (e.g., quad-core Xeon e5345) hardware, as well as sequential (e.g., matrix multiplication) and concurrent (e.g., operating system) software.

Sequential software can run on parallel hardware, and vice versa, but the key challenge lies in "making effective use of parallel hardware."

### 3. Parallel Programming Challenges

Creating parallel processing programs is difficult and requires significant performance improvement to justify the added complexity. "Parallel software is the problem."

Key difficulties in parallel programming include:
- **Partitioning:** Dividing the task into subtasks that can be executed in parallel.
- **Coordination:** Managing the dependencies and interactions between these subtasks.
- **Communications overhead:** The time and resources required for communication between processors or cores.

### 4. Amdahl's Law and Limits to Speedup

Amdahl's Law states that the sequential portion of a program can significantly limit the achievable speedup from parallelization.

The formula for speedup is given as:
```
Speedup = 1 / ((1 - Fparallelizable) + (Fparallelizable / Number of Processors))
```

Example: To achieve a 90x speedup with 100 processors, the sequential part of the program needs to be only 0.1% of the original execution time. "Need sequential part to be 0.1% of original time."

### 5. Strong vs Weak Scaling

- **Strong scaling:** Measures how the runtime of a fixed problem size decreases as the number of processors increases. The scaling example with a fixed workload (sum of 10 scalars and a 10x10 matrix) demonstrates strong scaling, showing diminishing returns in speedup as the number of processors increases due to the fixed sequential portion of the workload.

- **Weak scaling:** Measures how the runtime changes as the problem size is increased proportionally to the number of processors. The example with matrix size increasing with the number of processors (10 processors, 10x10 matrix; 100 processors, 32x32 matrix) illustrates weak scaling, aiming to maintain constant performance or efficiency.

### 6. Instruction and Data Streams (Flynn's Taxonomy)

The document introduces Flynn's taxonomy for classifying computer architectures based on the number of instruction streams and data streams:

- **SISD (Single Instruction, Single Data):** Serial processors like Intel Pentium 4.
- **SIMD (Single Instruction, Multiple Data):** Executes the same instruction on multiple data elements in parallel (e.g., SSE instructions in x86).
- **MISD (Multiple Instruction, Single Data):** Less common, no contemporary examples given.
- **MIMD (Multiple Instruction, Multiple Data):** Each processor executes its own instruction stream on its own data stream (e.g., Intel Xeon e5345).
- **SPMD (Single Program Multiple Data):** A parallel programming model on MIMD computers where multiple processors execute the same program but on different data, often with conditional code for different processors. "A parallel program on a MIMD computer".

### 7. Vector Processors

Vector processors are designed for high-performance computation on large arrays of data using vector instructions.

Key characteristics include:
- Highly pipelined function units.
- Streaming data between memory and vector registers.
- Vector registers holding multiple data elements (e.g., 32 x 64-element registers in the MIPS vector extension example).
- Specialized vector instructions like lv (load vector), sv (store vector), addv.d (add vectors of doubles), and addvs.d (add scalar to each element of a vector of doubles).

Vector architectures and compilers simplify data-parallel programming by explicitly stating the absence of loop-carried dependencies, reducing hardware checking, and benefiting from regular memory access patterns. "Explicit statement of absence of loop-carried dependences."

Vector processing is more general and better aligned with compiler technology compared to ad-hoc media extensions.

### 8. SIMD (Single Instruction, Multiple Data)

SIMD operations operate elementwise on vectors of data, as seen in multimedia extensions like MMX and SSE in x86 processors.

All processors execute the same instruction at the same time but on different data addresses.

SIMD simplifies synchronization and reduces instruction control hardware, working best for highly data-parallel applications.

### 9. Vector vs. Multimedia Extensions

- **Variable vs. Fixed Width:** Vector instructions have a variable vector width, while multimedia extensions have a fixed width.
- **Strided Access:** Vector instructions support strided memory access, which is not typically supported by multimedia extensions.
- **Functional Units:** Vector units can be a combination of pipelined and arrayed functional units, offering more flexibility.

### 10. Multithreading

Multithreading involves executing multiple threads of execution in parallel on a single processor core by replicating registers, program counters (PC), etc., and quickly switching between threads.

- **Fine-grain multithreading:** Switches threads after each cycle, interleaving instruction execution. If one thread stalls, others can proceed.
- **Coarse-grain multithreading:** Switches threads only on long stalls, such as L2 cache misses.

Coarse-grain multithreading simplifies hardware but doesn't hide short stalls like data hazards.

### 11. Simultaneous Multithreading (SMT)

SMT is used in multiple-issue, dynamically scheduled processors to schedule instructions from multiple threads concurrently.

Instructions from independent threads can execute whenever function units are available. Dependencies within threads are handled by scheduling and register renaming.

Example: Intel Pentium-4 HT, which supports two threads by duplicating registers while sharing function units and caches.

### 12. Future of Multithreading

The future of multithreading is uncertain but will likely be influenced by power considerations, leading to simpler microarchitectures and forms of multithreading.

Thread switching may be a crucial technique for tolerating cache-miss latency.

The possibility of multiple simple cores sharing resources more effectively is also considered.

## Key Quotes

- "making effective use of parallel hardware"
- "Parallel software is the problem"
- "Need sequential part to be 0.1% of original time" (regarding Amdahl's Law example)
- "A parallel program on a MIMD computer" (definition of SPMD)
- "Explicit statement of absence of loop-carried dependences" (benefit of vector architectures)

## Conclusion

The excerpts provide a foundational understanding of parallel processing, covering its motivations, challenges, hardware architectures, and software considerations. Key takeaways include the limitations imposed by sequential code (Amdahl's Law), the distinction between strong and weak scaling, the various architectural approaches to parallelism (SIMD, vector processors, MIMD), and techniques like multithreading to improve processor utilization. The document underscores the complexity of creating efficient parallel software and the ongoing evolution of parallel processing techniques in response to performance demands and power constraints.
