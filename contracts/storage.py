from rift import *


class Storage(Contract):
    """
    Simple Storage Contract.

    # config
    get-methods:
        - value
    """

    class Data(Model):
        admin: MsgAddress
        value: uint64

    class ChangeBody(Payload):
        new_value: uint64

    def internal_receive(self) -> None:
        assert self.message.info.src.is_equal(self.data.admin), 1001
        body = (
            self.body % self.ChangeBody
        )  # This parses body as ChangeBody class
        self.data.value = body.new_value
        self.data.save()
