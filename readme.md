
# Tracers

**Setup**
Os tracers devem ser enviados para algum host e porta com algum reciver. Por padrão esta configurado para enviar os tracers para o zipkin, na porta 9411, com o path '/api/v2/spans'.

Esse projeto usa a biblioteca aiozipkin.

Deve-se ser usado como decorator, sendo antes declarado com suas configuraçoes (caso haja) como uma variavel. Por exemplo:

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

**New child**

Para a cração de um novo tracer deve ser chamado a função new_child:

    @app.get("/create_tracer")
    @tracer.new_child()
    def example_endpoint():
        return 'hello world'

Essa função coleta o nome da função e usa como nome do tracer.
Para anotações do tracer chame a função annotate_span, e passe a anotação como string.

**Annotates e tags**

As anotações e tags são passadas chamando as funções:
annotate_tracer, annotate_spans ,tags_tracer e tags_child.
Para tags é necessário especificar a key e seu valor, da seguinte forma:
    key=value    or     'database'='controler'
