"""
Test methodical.
"""
from src.core.common.methodical import CallbackQueue, CallbackNode


class MessageBox:
    def __init__(self):
        self.callback_node: CallbackNode = CallbackNode()

    def play(self, message: str) -> CallbackNode:
        print(f"message: {message}")
        return self.callback_node

    def hide(self):
        self.callback_node.invoke()


class Curtain:
    def __init__(self):
        self.callback_node: CallbackNode = CallbackNode()

    def fade_in(self, name: str) -> CallbackNode:
        print(f"fading in ({name})...")
        return self.callback_node

    def hide(self):
        self.callback_node.invoke()


message_box = MessageBox()
curtain = Curtain()


def fn0() -> CallbackNode:
    return message_box.play("fn0")


def fn1() -> CallbackNode:
    return curtain.fade_in("fn1")


def fn2() -> CallbackNode:
    return message_box.play("fn2")


def fn3() -> CallbackNode:
    return curtain.fade_in("fn3")


CallbackQueue([fn0, fn1, fn2, fn3]).start()

a = 0
while a < 10:
    a += 1
    message_box.hide()
    curtain.hide()
