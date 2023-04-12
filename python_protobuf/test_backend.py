import backend_pb2
import common_pb2

#-------------content_wrapper
content_wrapper = backend_pb2.content_wrapper()
content_wrapper.command_uid = 51351351
content_wrapper.protocol_version = 1

#-------------command-charge_transaction
content_wrapper.charge_transaction == common_pb2.charge_transaction()
content_wrapper.charge_transaction.transaction_id = 123
content_wrapper.charge_transaction.duration_sec = 100

#-------------command-
# content_wrapper.charge_transaction == common_pb2.charge_transaction()
# content_wrapper.charge_transaction.transaction_id = 123
# content_wrapper.charge_transaction.duration_sec = 100

#----------------identity_tree
identity_tree = common_pb2.identity_tree()
identity_tree.device_mac = b'A4E57CC38D34'
identity_tree.identity = b'1.1'
identity_tree.domain = b'2'

#----------------transport_wrapper
transport_wrapper = backend_pb2.transport_wrapper()
transport_wrapper.content_wrapper_stream = content_wrapper.SerializeToString()
transport_wrapper.identity_tree_stream = identity_tree.SerializeToString()


print(transport_wrapper.SerializeToString().hex())