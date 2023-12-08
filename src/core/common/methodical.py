"""
Methodical module provides a seamless solution for callback sequences.
"""
from typing import Callable, List, Set


class CallbackNode:
    """
    Callback node holds a callback function that will be called in the future.
    """

    def __init__(self):
        # The callback function
        self._callback: Callable[[], None] | None = None

    def invoke(self) -> None:
        """
        Invokes the callback function.
        """
        if self._callback is not None:
            self._callback()

    def set(self, callback: Callable[[], None]) -> None:
        """
        Sets a callback function.
        :param callback: The callback function to set.
        """
        self._callback = callback

    def reset(self) -> None:
        """
        Resets the callback function.
        """
        self._callback = None


class CallbackQueue:
    """
    A callback queue stores a sequence of progressive functions.
    """

    def __init__(self, fn_list: List[Callable[[], CallbackNode | None]] = None):
        # A queue of waiting functions
        self._queue: List[Callable[[], CallbackNode | None]] = []

        # All nodes encountered during the recursion
        self._nodes: Set[CallbackNode] = set()

        # Callback to set
        self.callback = lambda: self.invoke_next()

        if fn_list is not None:
            self.append_list(fn_list)

    def append(self, fn: Callable[[], CallbackNode | None]) -> None:
        """
        Appends a waiting function.
        :param fn: The waiting function to append.
        """
        self._queue.append(fn)

    def append_list(self, fn_list: List[Callable[[], CallbackNode | None]]) -> None:
        """
        Appends a list of waiting functions.
        :param fn_list: A list of waiting functions to append.
        """
        for fn in fn_list:
            self.append(fn)

    def start(self) -> None:
        """
        An alias of invoke_next().
        """
        self.invoke_next()

    def invoke_next(self) -> None:
        """
        Invokes the first waiting function.
        """
        fn = self._get_next()
        if fn is None:
            # Recursion ends; clears the callbacks in all nodes
            return self._reset_nodes()

        # Run the progressive function and get a callback node
        callback_node: CallbackNode | None = fn()
        if callback_node is None:
            if self._queue:
                # Move on to the next function immediately
                self.invoke_next()
        else:
            # Set a callback function for it
            callback_node.set(self.callback)

            # Record the callback node
            self._nodes.add(callback_node)

    def _reset_nodes(self) -> None:
        """
        Resets all nodes that are affected.
        """
        for node in self._nodes:
            node.reset()

    def _get_next(self) -> Callable[[], CallbackNode | None] | None:
        """
        Pops the next waiting function in the queue.
        :return None if the queue is empty.
        """
        return None if not self._queue else self._queue.pop(0)
