import datetime
import pytz
from concurrent import futures

import grpc
from protos import timezones_pb2_grpc, timezones_pb2


# Implementing the grpc server
class TimeZones(timezones_pb2_grpc.TimeZonesServicer):

    # Return the time of the given timezone
    def getTime(self, request, context):
        return timezones_pb2.Time(time=datetime.datetime.now(pytz.timezone(request.name))
                                  .strftime("%H:%M:%S"))

    # Return a list of available timezones
    def getTimezones(self, request, context):
        for timezone in pytz.common_timezones:
            # Stream timezone names and offsets in hours
            yield timezones_pb2.TimeZone(name=timezone, offset=pytz.timezone(timezone).utcoffset(
                datetime.datetime.utcnow()).total_seconds() / 3600)

# Starting the server
def serve():
    print("Starting server")
    # From https://grpc.io/docs/languages/python/basics/
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    timezones_pb2_grpc.add_TimeZonesServicer_to_server(
        TimeZones(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
