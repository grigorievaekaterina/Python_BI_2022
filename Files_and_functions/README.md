## Description

This is the first task in the course. The program `fastq_filtrator.py` can perfom the following:
1. Filter reads by GC composition
2. Filter reads by quality
3. Filter reads by length
4. Save results to a file

Main function takes the following arguments:
1. `input_fastq` - path to the file that is input to the program (normal uncompressed fastq file)
2. `output_file_prefix` - path prefix to the file where the result will be written
3. `gc_bounds` - GC composition interval (in percent) for filtering (default is (0, 100), i.e. all reads are saved)
4. `length_bounds` - length interval for filtering, everything is similar to gc_bounds, but by default it is (0, 2**32).
5. `quality_threshold` - average read quality threshold for filtering, by default equals 0 (phred33 scale)
6. `save_filtered` - whether to save filtered reads, default is False.

