from fasthtml.common import *

app, rt = fast_app()

def card_3d(text, background, description):
    """Generate a 3D card component with inline styles."""
    return Div(
        Div(
            text,
            Div(description, _class="card-description"),
            _class="card-content",
            _style=f"""
                background-image: url('{background}');
                background-size: cover;
                background-position: center;
                width: 300px;
                height: 200px;
                transform: rotateY(0deg);
                transition: transform 0.5s;
                position: relative;
            """
        ),
        _class="card",
        _style="perspective: 1000px; margin: 20px;",
        _data_title=text,
        _data_description=description
    )

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
        Div(
            Input(_type="text", _placeholder="Search portfolios...", _id="search-input", _style="padding: 10px; width: 300px;"),
            _style="margin: 20px;"
        ),
        Div(
            card_3d("Project 1", "https://via.placeholder.com/300x200", "This is a demo project."),
            card_3d("Project 2", "https://via.placeholder.com/300x200", "An example of a portfolio."),
            card_3d("Project 3", "https://via.placeholder.com/300x200", "Another demo project for testing."),
            _id="portfolio-container",
            _style="display: flex; flex-wrap: wrap; justify-content: center;"
        ),
        Script("""
        document.getElementById('search-input').addEventListener('input', function() {
            const query = this.value.toLowerCase();
            const cards = document.querySelectorAll('.card');
            
            cards.forEach(card => {
                const title = card.getAttribute('data-title').toLowerCase();
                const description = card.getAttribute('data-description').toLowerCase();
                
                // Check if the query matches title or description
                const isMatch = title.includes(query) || description.includes(query);
                
                card.style.display = isMatch ? 'block' : 'none';
            });
        });
        """),
        _style="text-align: center; font-family: Arial, sans-serif;"
    )

serve()