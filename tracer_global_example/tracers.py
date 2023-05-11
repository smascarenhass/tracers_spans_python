from tracers_spans_python.tracers_spans import Tracer
import socket

PROJECT_NAME = 'OPS'


# TRACER = Tracer(
#     service_name=PROJECT_NAME,
#     host='sg03.picalike.corpex-kunden.de', 
#     port='9400',
#     )


TRACER = Tracer(
    service_name=PROJECT_NAME, 
    host='localhost', 
    port='9411/api/v2/spans',
    )

# http://sg03.picalike.corpex-kunden.de:9400