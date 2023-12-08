# Separate Callback Control (SCC) Technique

I was pretty frustrated refracting my messy code the other day. The piles of callback functions make me lightheaded. So I was thinking of a way where I can simply create a bunch of functions, and they can run one after one methodically. So instead of letting methods receive a callback function as parameter, I tried to let them return a holder which is able to wrap a callback function. The ultimate goal of this technique is allowing me to write something like this:

~~~python
# fn0, fn1, and fn2 are all functions
CallbackQueue([fn0, fn1, fn2]).start()
~~~

I am not sure if some great people have studied through these long ago, but I feel a great sense of success making this out on my own. Refer to the source code in `src/core/common/methodical.py` for more details.

## Callback Node

I created a `CallbackNode` class that serves as the callback holder, and it looks like this:

~~~python
class CallbackNode:
    def __init__(self):
        self.callback: Callable[[], None] | None = None

    def invoke(self) -> None:
        """
        Invokes the callback function.
        """
        if self.callback is not None:
            self.callback()
            self.callback = None
~~~

A traditional asynchronous function receives a callback function as parameter like this:

~~~python
def fn(callback):
    # The callback function will be invoked at a certain moment
    pass
~~~

Now this function will no longer receive the callback function, instead, it returns a callback node allowing the external to set the callback function later.

~~~python
def fn() -> CallbackNode:
    callback_node = CallbackNode()
    # callback_node will be invoked at a certain moment

    return callback_node
~~~

The callback node wraps nothing when the function ends. But soon after the callback queue, which we will be covering in no time, will assign the next function to it.

## Callback Queue

A callback queue stores a sequence of **progressive functions
** (渐进函数), which return callback nodes. To make it clearer, A function that returns a callback node or None is called a
**half-progressive function**; a function that always return None is called an **inserted function
** (嵌函数). Collectively, progressive function, half-progressive function and inserted function are called
**waiting functions** (候函数), or simply function, in the callback queue.

~~~python
class CallbackQueue:
    def __init__(self, progressive_fn_list: List[Callable[[], CallbackNode | None]] = None):
        # A queue of progressive function
        self._queue: List[Callable[[], CallbackNode | None]] = []

        if progressive_fn_list is not None:
            self.append_list(progressive_fn_list)

    def append(self, fn: Callable[[], CallbackNode | None]) -> None:
        """
        Appends a progressive function.
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
~~~

Before revealing the `invoke_next` function, let me explain how this machine works to arrange given functions to run one after one. When it starts, the first function will be dequeued and called, and the callback node it returns will be loaded by a simple callback function like this:

~~~python
def callback():
    self.invoke_next()
~~~

It looks like a recursion, but what makes it different is that it is put in a callback function, which will be called later. I call this
**delay recursion
**. There is a situation where the waiting function returns None. In this case, the recursion will no longer be delayed, that is to say, the `invoke_next` method will be called immediately. The recursion ends when the queue is empty.

## Example