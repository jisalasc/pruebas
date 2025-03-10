#include <stdio.h>
#include <time.h>

int main() {
    long long n = 1000000000; // 1 billion
    long long sum = 0;
    clock_t start, end;
    double cpu_time_used;

    start = clock();
    for (long long i = 1; i <= n; i++) {
        sum += i;
    }
    end = clock();

    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Sum: %lld\n", sum);
    printf("Time taken: %f seconds\n", cpu_time_used);

    return 0;
}