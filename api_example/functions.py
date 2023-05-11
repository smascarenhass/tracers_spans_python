from tracer_global_example.tracers import TRACER
import time

@TRACER.new_child()
def function():
    TRACER.annotate_tracer('annotate in a tracer')
    time.sleep(1)
    return('test1')

@TRACER.new_child()
def function2():
    time.sleep(2)
    # Here add annotate to spans
    TRACER.annotate_span('function 2 end')
    TRACER.tags_tracer('teste', 'of tag')
    function()
    return('foi 2')

@TRACER.new_async_child()
async def async_function():
    TRACER.annotate_tracer('annotate in a tracer')
    time.sleep(1)
    return('test1')