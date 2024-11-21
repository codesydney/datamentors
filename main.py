from fasthtml.common import *
from fastapi.staticfiles import StaticFiles

app, rt = fast_app()

# Serve files from the "pdf" folder as static files
app.mount("/pdf", StaticFiles(directory="pdf"), name="pdf")

def card_3d(title, background, description, title_link, description_link):
    """Generate a 3D card component with inline styles and links."""
    return Div(
        Div(
            Div(
                _style=f"""
                    background-image: url('{background}');
                    background-size: cover;
                    background-position: center;
                    width: 600px;
                    height: 400px;
                """
            ),
            Div(
                A(title, href=title_link, target="_blank", _class="card-title"),
                A(description, href=description_link, target="_blank", _class="card-description"),
                _class="card-text",
                _style="padding: 10px; text-align: center; font-size: 14px;"
            ),
            _class="card-content",
            _style="width: 600px; height: 450px; display: flex; flex-direction: column; justify-content: space-between;"
        ),
        _class="card",
        _style="perspective: 1000px; margin: 20px;",
        _data_title=title,
        _data_description=description
    )

@rt("/")
def get(req):
    return Div(
        Div(
            Img(
                src="img/DataMentorsLogo.png",
                alt="DataMentors Logo",
                _style="width: 200px; margin-bottom: 10px;"
            ),
            _style="text-align: center;"
        ),        
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
            card_3d(
                "Emigrant Data Analysis (1981-2022) | ", 
                "img/DEP4G-Emigration.png", 
                " Chris Formoso", 
                "https://emigrant-country-dashboard.streamlit.app/", 
                "https://ca.linkedin.com/in/chris-formoso"
            ),
            card_3d(
                "Foreign Spouse Exploratory Data Analysis | ", 
                "img/DEP4G-Foreign-Spouse.png", 
                " Jun Miano", 
                "https://foreign-spouse.streamlit.app/", 
                "https://ph.linkedin.com/in/junmiano1202"
            ),
            _id="portfolio-container",
            _style="display: flex; flex-wrap: wrap; justify-content: center;"
        ),
        Div(
            Div(
                "Copyright © 2025 Code.Sydney Pty Ltd ABN 37 625 436 151",
                _style="text-align: left; padding-left: 20px;"
            ),
            Div(
                A("Privacy Policy 2025", href="/pdf/Code.Sydney_Client_Terms_2025.pdf", target="_blank", _style="margin-right: 10px;"),
                "|",
                A("Terms 2025", href="/pdf/Code.Sydney_Client_Terms_2025.pdf", target="_blank", _style="margin-left: 10px;"),
                _style="text-align: right; padding-right: 20px;"
            ),
            _class="footer",
            _style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-top: 1px solid #ccc; margin-top: 20px;"
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