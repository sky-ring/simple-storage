from rift import *
from contracts.storage import Storage


def test_get_method():
    data = Storage.Data(admin=MsgAddress.std(0, 1), value=1).as_cell()
    storage = Storage.instantiate(data)
    res = storage.get_value()
    res.expect_ok()
    (value,) = res.result.stack
    assert value == 1


def test_change_value():
    data = Storage.Data(admin=MsgAddress.std(0, 1), value=1).as_cell()
    storage = Storage.instantiate(data)
    body = Storage.ChangeBody(new_value=2)
    msg = InternalMessage[Storage.ChangeBody].build(
        src=MsgAddress.std(0, 1),
        dest=MsgAddress.std(0, 0),
        body=body,
    )
    res = storage.recv_internal(0, 0, msg.as_cell(), body.as_cell().parse())
    res = storage.get_value()
    res.expect_ok()
    (value,) = res.result.stack
    assert value == 2


def test_change_value_wrong_admin():
    data = Storage.Data(admin=MsgAddress.std(0, 1), value=1).as_cell()
    storage = Storage.instantiate(data)
    body = Storage.ChangeBody(new_value=2)
    msg = InternalMessage[Storage.ChangeBody].build(
        src=MsgAddress.std(0, 2),
        dest=MsgAddress.std(0, 0),
        body=body,
    )
    res = storage.recv_internal(0, 0, msg.as_cell(), body.as_cell().parse())
    res.expect_exit(1001)
