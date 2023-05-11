
# Tracers


======Tracers======

**Setup**

Library:

<code> pip install tracers-spans-python </code>

A global variable must be created with the settings for sending tracers, for example:

<code>

/monitoring/tracers/tracers.py

    from tracers_spans_python import Tracer

    PROJECT_NAME = 'OPS'


    TRACER = Tracer(
        service_name=PROJECT_NAME,
        host='localhost', 
        port='9411/api/v2/spans',
        )
</code>

Tracers must be sent to some host and port with some reciver. By default it is configured to send tracers to zipkin, on port 9411, with the path '/api/v2/spans'.

To create tracers, it must be used as a decorator, first being declared with its settings (if any) as a variable. For example:

<code>

    import xxx
    from fastapi import FastAPI

    app = FastAPI()
    tracer = Tracer(
        service_name='example', host='0.0.0.0', 
        path='api/v2/spans',
        port='9411', ip_application='0.0.0.0'
        )
        
 </code>


**New tracer**

To create a new tracer, call the new_tracer function:

<code>

    @app.get("/create_tracer")
    @tracer.new_tracer()
    def example_endpoint():
        return 'hello world'
        
</code>

This function collects the function name from the endpoint and uses it as the tracer name.
For tracer annotations call the annotate_tracer function, and pass the annotation as a string.

**New async tracer**

To create a new tracer for an endpoint or asyncrona function, the new_async_tracer function must be called:

<code>
    @app.get("/create_tracer")
    @tracer.new_async_tracer()
    async def example_endpoint():
        result = await function()
        return result

</code>

**New child**

Para a cração de um novo tracer deve ser chamado a função new_child:

<code>
    @app.get("/create_tracer")
    @tracer.new_child()
    def example_endpoint():
        return 'hello world'
</code>

This function collects the function name and uses it as the tracer name.
For tracer annotations call the annotate_span function, and pass the annotation as a string.

**New async child**

To create a new child for an asyncronous function, call the new_async_child function:

<code>
    @app.get("/create_tracer")
    @tracer.new_async_child()
    async def example_endpoint():
    result = await function()
        return result

</code>

**Annotates e tags**

The annotations and tags are passed by calling the functions:
annotate_tracer, annotate_spans, tags_tracer and tags_child.
For annotations the only requirement is that the parameter passed is a string.
For tags it is necessary to specify the key and its value, as follows:

    key=value    or     'database'='controler'


**Dependecies**

 aiozipkin


**Setup**

Biblioteca: $ pip install tracers-spans-python

Deve-se ser criado uma variavel global com as configurações para o envio dos tracers, por exemplo:

/monitoring/tracers/tracers.py

    from tracers_spans_python import Tracer

    PROJECT_NAME = 'OPS'


    TRACER = Tracer(
        service_name=PROJECT_NAME,
        host='localhost', 
        port='9411/api/v2/spans',
        )

Os tracers devem ser enviados para algum host e porta com algum reciver. Por padrão esta configurado para enviar os tracers para o zipkin, na porta 9411, com o path '/api/v2/spans'.

Para a criação de tracers, deve ser usado como decorator, sendo antes declarado com suas configuraçoes (caso haja) como uma variavel. Por exemplo:

    import xxx
    from fastapi import FastAPI

    app = FastAPI()
    tracer = Tracer(
        service_name='example', host='0.0.0.0', 
        path='api/v2/spans',
        port='9411', ip_application='0.0.0.0'
        )


**New tracer**

Para a cração de um novo tracer deve ser chamado a função new_tracer:

    @app.get("/create_tracer")
    @tracer.new_tracer()
    def example_endpoint():
        return 'hello world'

Essa função coleta o nome da funcção do endpoint e usa como nome do tracer.
Para anotações do tracer chame a função annotate_tracer, e passe a anotação como string.

**New async tracer**

Para a cração de um novo tracer para um endpoint ou função asyncrona deve ser chamado a função new_async_tracer:

    @app.get("/create_tracer")
    @tracer.new_async_tracer()
    async def example_endpoint():
        result = await function()
        return result


**New child**

Para a cração de um novo tracer deve ser chamado a função new_child:

    @app.get("/create_tracer")
    @tracer.new_child()
    def example_endpoint():
        return 'hello world'

Essa função coleta o nome da função e usa como nome do tracer.
Para anotações do tracer chame a função annotate_span, e passe a anotação como string.

**New async child**

Para a cração de uma nova child para uma função asyncrona deve ser chamado a função new_async_child:

    @app.get("/create_tracer")
    @tracer.new_async_child()
    async def example_endpoint():
    result = await function()
        return result


**Annotates e tags**

As anotações e tags são passadas chamando as funções:
annotate_tracer, annotate_spans ,tags_tracer e tags_child.
Para anotaçoes a unica exigência é que o parametro passado seja uma string.
Para tags é necessário especificar a key e seu valor, da seguinte forma:
    key=value    or     'database'='controler'


**Dependecies**

 aiozipkin
