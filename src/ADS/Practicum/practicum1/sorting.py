class Sorter(object):
    """
    Base class for sorters. Defines the `sort` method.
    """
    def sort(self, elements):
        """
        Sorts the elements in the list.

        :param elements: The list of elements which has to be sorted
        :type elements: list
        :return: The sorted list of elements
        :rtype: list
        """
        raise NotImplementedError()


class InsertionSorter(Sorter):
    """
    Sorter implementation using the insertion sort strategy.
    """
    def sort(self, elements):
        # Replace this with a useful piece of code that actually sorts elements
        # The test assumes that you return a list

        for i in range(1, len(elements)):
            j = i
            while j > 0 and elements[j - 1] > elements[j]:
                elements[j], elements[j - 1] = elements[j - 1], elements[j]
                j -= 1
        return elements


class QuickSorter(Sorter):
    """
    Sorter implementation using the quick sort strategy.
    """
    def sort(self, elements):
        # Replace this with a useful piece of code that actually sorts elements
        # The test assumes that you return a list
        self.quicksort(elements, 0, len(elements) - 1)
        return elements

    def quicksort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quicksort(arr, low, pivot - 1)
            self.quicksort(arr, pivot + 1, high)

    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i
