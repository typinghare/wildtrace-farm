"""
Methodical module provides a seamless solution for callback sequences.
"""
from typing import Callable, List


class CallbackNode:
    """
    Callback node holds a callback function that will be called in the future.
    """

    Dummy: "CallbackNode" = None

    def __init__(self):
        self.callback: Callable[[], None] | None = None

    def invoke(self) -> None:
        """
        Invokes the callback function.
        """
        if self.callback is not None:
            self.callback()


# Initialize dummy
CallbackNode.Dummy = CallbackNode()


class CallbackQueue:
    """
    A callback queue stores a sequence of progressive functions.
    """

    def __init__(self, progressive_fn_list: List[Callable[[], CallbackNode | None]] = None):
        # A queue of progressive function
        self._queue: List[Callable[[], CallbackNode | None]] = []

        if progressive_fn_list is not None:
            self.append_list(progressive_fn_list)

    def append(self, progressive_fn: Callable[[], CallbackNode | None]) -> None:
        """
        Appends a progressive function.
        :param progressive_fn: The progressive function to append.
        """
        self._queue.append(progressive_fn)

    def append_list(self, progressive_fn_list: List[Callable[[], CallbackNode | None]]) -> None:
        """
        Appends a list of progressive functions.
        :param progressive_fn_list: A list of progressive functions.
        """
        for progressive_fn in progressive_fn_list:
            self.append(progressive_fn)

    def start(self) -> None:
        """
        An alias of invoke_next().
        """
        self.invoke_next()

    def invoke_next(self) -> None:
        """
        Starts the first progressive function.
        """
        progressive_fn = self._get_next()
        if progressive_fn is None:
            return

        # Runs the progressive function and get a callback node
        callback_node: CallbackNode | None = progressive_fn()
        if callback_node is None:
            return

        # Callback node is not none, set the callback function for it
        callback_node.callback = lambda: self.invoke_next()

    def _get_next(self) -> Callable[[], CallbackNode | None] | None:
        """
        Pops the next progressive function in the queue.
        :return None if the queue is empty.
        """
        return None if not self._queue else self._queue.pop(0)
