# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import timezones_pb2 as protos_dot_timezones__pb2


class TimeZonesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getTime = channel.unary_unary(
                '/TimeZones/getTime',
                request_serializer=protos_dot_timezones__pb2.TimeZone.SerializeToString,
                response_deserializer=protos_dot_timezones__pb2.Time.FromString,
                )
        self.getTimezones = channel.unary_stream(
                '/TimeZones/getTimezones',
                request_serializer=protos_dot_timezones__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_timezones__pb2.TimeZone.FromString,
                )


class TimeZonesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTimezones(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TimeZonesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getTime': grpc.unary_unary_rpc_method_handler(
                    servicer.getTime,
                    request_deserializer=protos_dot_timezones__pb2.TimeZone.FromString,
                    response_serializer=protos_dot_timezones__pb2.Time.SerializeToString,
            ),
            'getTimezones': grpc.unary_stream_rpc_method_handler(
                    servicer.getTimezones,
                    request_deserializer=protos_dot_timezones__pb2.Empty.FromString,
                    response_serializer=protos_dot_timezones__pb2.TimeZone.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TimeZones', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TimeZones(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TimeZones/getTime',
            protos_dot_timezones__pb2.TimeZone.SerializeToString,
            protos_dot_timezones__pb2.Time.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTimezones(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/TimeZones/getTimezones',
            protos_dot_timezones__pb2.Empty.SerializeToString,
            protos_dot_timezones__pb2.TimeZone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
