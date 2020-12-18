# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api import api_pb2 as api_dot_api__pb2
from schema import sth_pb2 as schema_dot_sth__pb2


class TrustixLogAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSTH = channel.unary_unary(
            "/trustix.TrustixLogAPI/GetSTH",
            request_serializer=api_dot_api__pb2.STHRequest.SerializeToString,
            response_deserializer=schema_dot_sth__pb2.STH.FromString,
        )
        self.Submit = channel.unary_unary(
            "/trustix.TrustixLogAPI/Submit",
            request_serializer=api_dot_api__pb2.SubmitRequest.SerializeToString,
            response_deserializer=api_dot_api__pb2.SubmitResponse.FromString,
        )
        self.Flush = channel.unary_unary(
            "/trustix.TrustixLogAPI/Flush",
            request_serializer=api_dot_api__pb2.FlushRequest.SerializeToString,
            response_deserializer=api_dot_api__pb2.FlushResponse.FromString,
        )
        self.GetLogConsistencyProof = channel.unary_unary(
            "/trustix.TrustixLogAPI/GetLogConsistencyProof",
            request_serializer=api_dot_api__pb2.GetLogConsistencyProofRequest.SerializeToString,
            response_deserializer=api_dot_api__pb2.ProofResponse.FromString,
        )
        self.GetLogAuditProof = channel.unary_unary(
            "/trustix.TrustixLogAPI/GetLogAuditProof",
            request_serializer=api_dot_api__pb2.GetLogAuditProofRequest.SerializeToString,
            response_deserializer=api_dot_api__pb2.ProofResponse.FromString,
        )
        self.GetLogEntries = channel.unary_unary(
            "/trustix.TrustixLogAPI/GetLogEntries",
            request_serializer=api_dot_api__pb2.GetLogEntriesRequest.SerializeToString,
            response_deserializer=api_dot_api__pb2.LogEntriesResponse.FromString,
        )
        self.GetMapValue = channel.unary_unary(
            "/trustix.TrustixLogAPI/GetMapValue",
            request_serializer=api_dot_api__pb2.GetMapValueRequest.SerializeToString,
            response_deserializer=api_dot_api__pb2.MapValueResponse.FromString,
        )
        self.GetMHLogConsistencyProof = channel.unary_unary(
            "/trustix.TrustixLogAPI/GetMHLogConsistencyProof",
            request_serializer=api_dot_api__pb2.GetLogConsistencyProofRequest.SerializeToString,
            response_deserializer=api_dot_api__pb2.ProofResponse.FromString,
        )
        self.GetMHLogAuditProof = channel.unary_unary(
            "/trustix.TrustixLogAPI/GetMHLogAuditProof",
            request_serializer=api_dot_api__pb2.GetLogAuditProofRequest.SerializeToString,
            response_deserializer=api_dot_api__pb2.ProofResponse.FromString,
        )
        self.GetMHLogEntries = channel.unary_unary(
            "/trustix.TrustixLogAPI/GetMHLogEntries",
            request_serializer=api_dot_api__pb2.GetLogEntriesRequest.SerializeToString,
            response_deserializer=api_dot_api__pb2.LogEntriesResponse.FromString,
        )


class TrustixLogAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSTH(self, request, context):
        """Aggregate"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Submit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Flush(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetLogConsistencyProof(self, request, context):
        """Log"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetLogAuditProof(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetLogEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetMapValue(self, request, context):
        """Map"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetMHLogConsistencyProof(self, request, context):
        """Maphead log"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetMHLogAuditProof(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetMHLogEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TrustixLogAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetSTH": grpc.unary_unary_rpc_method_handler(
            servicer.GetSTH,
            request_deserializer=api_dot_api__pb2.STHRequest.FromString,
            response_serializer=schema_dot_sth__pb2.STH.SerializeToString,
        ),
        "Submit": grpc.unary_unary_rpc_method_handler(
            servicer.Submit,
            request_deserializer=api_dot_api__pb2.SubmitRequest.FromString,
            response_serializer=api_dot_api__pb2.SubmitResponse.SerializeToString,
        ),
        "Flush": grpc.unary_unary_rpc_method_handler(
            servicer.Flush,
            request_deserializer=api_dot_api__pb2.FlushRequest.FromString,
            response_serializer=api_dot_api__pb2.FlushResponse.SerializeToString,
        ),
        "GetLogConsistencyProof": grpc.unary_unary_rpc_method_handler(
            servicer.GetLogConsistencyProof,
            request_deserializer=api_dot_api__pb2.GetLogConsistencyProofRequest.FromString,
            response_serializer=api_dot_api__pb2.ProofResponse.SerializeToString,
        ),
        "GetLogAuditProof": grpc.unary_unary_rpc_method_handler(
            servicer.GetLogAuditProof,
            request_deserializer=api_dot_api__pb2.GetLogAuditProofRequest.FromString,
            response_serializer=api_dot_api__pb2.ProofResponse.SerializeToString,
        ),
        "GetLogEntries": grpc.unary_unary_rpc_method_handler(
            servicer.GetLogEntries,
            request_deserializer=api_dot_api__pb2.GetLogEntriesRequest.FromString,
            response_serializer=api_dot_api__pb2.LogEntriesResponse.SerializeToString,
        ),
        "GetMapValue": grpc.unary_unary_rpc_method_handler(
            servicer.GetMapValue,
            request_deserializer=api_dot_api__pb2.GetMapValueRequest.FromString,
            response_serializer=api_dot_api__pb2.MapValueResponse.SerializeToString,
        ),
        "GetMHLogConsistencyProof": grpc.unary_unary_rpc_method_handler(
            servicer.GetMHLogConsistencyProof,
            request_deserializer=api_dot_api__pb2.GetLogConsistencyProofRequest.FromString,
            response_serializer=api_dot_api__pb2.ProofResponse.SerializeToString,
        ),
        "GetMHLogAuditProof": grpc.unary_unary_rpc_method_handler(
            servicer.GetMHLogAuditProof,
            request_deserializer=api_dot_api__pb2.GetLogAuditProofRequest.FromString,
            response_serializer=api_dot_api__pb2.ProofResponse.SerializeToString,
        ),
        "GetMHLogEntries": grpc.unary_unary_rpc_method_handler(
            servicer.GetMHLogEntries,
            request_deserializer=api_dot_api__pb2.GetLogEntriesRequest.FromString,
            response_serializer=api_dot_api__pb2.LogEntriesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "trustix.TrustixLogAPI", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TrustixLogAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSTH(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/GetSTH",
            api_dot_api__pb2.STHRequest.SerializeToString,
            schema_dot_sth__pb2.STH.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Submit(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/Submit",
            api_dot_api__pb2.SubmitRequest.SerializeToString,
            api_dot_api__pb2.SubmitResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Flush(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/Flush",
            api_dot_api__pb2.FlushRequest.SerializeToString,
            api_dot_api__pb2.FlushResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetLogConsistencyProof(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/GetLogConsistencyProof",
            api_dot_api__pb2.GetLogConsistencyProofRequest.SerializeToString,
            api_dot_api__pb2.ProofResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetLogAuditProof(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/GetLogAuditProof",
            api_dot_api__pb2.GetLogAuditProofRequest.SerializeToString,
            api_dot_api__pb2.ProofResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetLogEntries(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/GetLogEntries",
            api_dot_api__pb2.GetLogEntriesRequest.SerializeToString,
            api_dot_api__pb2.LogEntriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetMapValue(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/GetMapValue",
            api_dot_api__pb2.GetMapValueRequest.SerializeToString,
            api_dot_api__pb2.MapValueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetMHLogConsistencyProof(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/GetMHLogConsistencyProof",
            api_dot_api__pb2.GetLogConsistencyProofRequest.SerializeToString,
            api_dot_api__pb2.ProofResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetMHLogAuditProof(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/GetMHLogAuditProof",
            api_dot_api__pb2.GetLogAuditProofRequest.SerializeToString,
            api_dot_api__pb2.ProofResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetMHLogEntries(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/trustix.TrustixLogAPI/GetMHLogEntries",
            api_dot_api__pb2.GetLogEntriesRequest.SerializeToString,
            api_dot_api__pb2.LogEntriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
