from fastapi import FastAPI
from api_example.functions import *
from tracer_global_example.tracers import *
import aiozipkin as az


app = FastAPI()


# function to call a function that send a tracer
@app.get("/create_tracer")
@TRACER.new_tracer()
def example_endpoint():

    # Do some work
    result = function
    result2 = function2
       
    # Do some more work
    return {
        "result": result(), 
        "resul2": result2(),
        'name service': TRACER.service_name,
        'host': TRACER.host 
        }

@app.get("/create_async_tracer")
@TRACER.new_async_tracer()
async def example_async_endpoint():

    # Do some work
    result = async_function
       
    # Do some more work
    return {
        "result": await result(), 
        'name service': TRACER.service_name,
        'host': TRACER.host 
        }

@app.get("/create_sample_tracer")
async def example_sample_endpoint():

    # Here is a conection with zipkin and yours settings.
    zipkin_address = "http://sg03.picalike.corpex-kunden.de:9400"
    # Here is features of endpoint.
    endpoint = az.create_endpoint(f"tests", ipv4="0.0.0.0", port=11880)

    tracer = await az.create(zipkin_address, endpoint, sample_rate=1.0)
     
    with tracer.new_trace(sampled=True) as span:
        span.name('simple trace')
    return 'hello'