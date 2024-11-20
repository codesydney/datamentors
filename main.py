from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get(req):
    return Div(
        H1("DataMentors"),
        P(
            "A Joint Initiative by ", 
            A("Code.Sydney", href="https://www.code.sydney", target="_blank"),
            " and ",
            A("Data Engineering Pilipinas", href="https://dataengineering.ph/", target="_blank")
        ),
        _class="container"
    )

serve()