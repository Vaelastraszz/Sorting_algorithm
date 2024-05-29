# Sorting Algorithms Visualizer

Welcome to the Sorting Algorithms Visualizer! This project provides visualizations for three different types of sorting algorithms. You can view the live app [here](https://vaelastraszz-sorting-algorithm-sorting-algorithms-7aawuz.streamlit.app/).

## Table of Contents

- [Introduction](#introduction)
- [Sorting Algorithms](#sorting-algorithms)
  - [Bubble Sort](#bubble-sort)
  - [Quick Sort](#quick-sort)
  - [Insertion Sort](#insertion-sort)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project aims to help users understand how different sorting algorithms work through visualizations. Currently, the project includes the following sorting algorithms:
- Bubble Sort
- Quick Sort
- Insertion Sort

## Sorting Algorithms

### Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name because smaller elements "bubble" to the top of the list.

- **Advantages**: Simple to understand and implement.
- **Disadvantages**: Very slow for large datasets; not practical for real-world use.

![Sorting_bubblesort_anim](https://github.com/Vaelastraszz/Sorting_algorithm/assets/47340421/e0b7c4d4-195c-4bbc-aceb-ac4fe1011963)

### Quick Sort

Quick Sort is a highly efficient sorting algorithm and is based on the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

- **Advantages**: Generally faster than other O(n log n) algorithms; well-suited for large datasets.
- **Disadvantages**: Worst-case performance is O(n^2), but this can be mitigated with good pivot selection strategies.

![Sorting_quicksort_anim](https://github.com/Vaelastraszz/Sorting_algorithm/assets/47340421/581a6714-a3a7-499e-95e7-bfeb19f3d440)

### Insertion Sort

Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

- **Advantages**: Simple to implement; efficient for small datasets or nearly sorted data.
- **Disadvantages**: Inefficient for large datasets; has a time complexity of O(n^2).

![Insertion_sort_animation](https://github.com/Vaelastraszz/Sorting_algorithm/assets/47340421/d9f9e563-3a4f-4c1e-9a84-78d7fc34487b)

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact me at [your-email@example.com].

---

Thank you for visiting my repository! I hope you find these visualizations helpful and educational.

