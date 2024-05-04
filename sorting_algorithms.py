import streamlit as st
import time
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr[:]


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        yield arr
        yield from quick_sort(arr, low, pivot_index - 1)
        yield from quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
            yield arr[:]


def generate_random_list(n):
    return np.random.randint(0, 100, n)


def main():
    st.title("Sorting Algorithms Visualization")
    n = st.slider("Select the size of the list", 1, 100)
    arr = generate_random_list(n)

    algorithm_choice = st.selectbox(
        "Select sorting algorithm", ["Bubble sort", "Quick sort", "Insert sort"]
    )
    algorithm_dict = {
        "Bubble sort": bubble_sort,
        "Quick sort": quick_sort,
        "Insert sort": insert_sort,
    }
    algorithm = algorithm_dict[algorithm_choice]

    if st.button("Sort"):
        st.subheader(f"{algorithm_choice} in action...")
        chart = st.empty()
        for arr in algorithm(arr):
            fig = go.Figure(
                data=[
                    go.Bar(
                        x=np.arange(len(arr)),
                        y=arr,
                        marker=dict(color=arr, colorscale="Viridis"),
                    )
                ]
            )
            chart.plotly_chart(fig)
            time.sleep(0.05)


if __name__ == "__main__":
    main()
