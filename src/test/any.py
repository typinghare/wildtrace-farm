from src.world.common.methodical import CallbackQueue, CallbackNode

a = {}

print(bool(a.get("5")))


class MessageBox:
    def __init__(self):
        self.callback_node: CallbackNode = CallbackNode.Dummy

    def play(self, message: str) -> CallbackNode:
        print(message)
        self.callback_node = CallbackNode()

        return self.callback_node

    def hide(self):
        if self.callback_node is not None:
            self.callback_node.invoke()


message_box = MessageBox()


def fn0() -> CallbackNode:
    return message_box.play("fn0")


def fn1() -> CallbackNode:
    return message_box.play("fn1")


def fn2() -> CallbackNode:
    return message_box.play("fn2")


callbackQueue = CallbackQueue()
callbackQueue.append(fn0)
callbackQueue.append(fn1)
callbackQueue.append(fn2)
callbackQueue.invoke_next()


def interval_fn():
    message_box.hide()


a = 0
while a < 10:
    a += 1
    message_box.hide()
