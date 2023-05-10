from tracers_spans_python.tracers_spans import Tracer


TRACER = Tracer(
    service_name='Mascarenhas_PC',
    host='sg03.picalike.corpex-kunden.de', 
    port='9400',
    )
print(TRACER.zipkin_address)
TRACER_LOCAL = Tracer(
    service_name='Mascarenhas_PC', 
    host='localhost', 
    port='9411',
    )

# http://sg03.picalike.corpex-kunden.de:9400