from fasthtml.common import *
from fastapi.staticfiles import StaticFiles
from styles import styles
from cards import MENTOR_CARDS, PORTFOLIO_CARDS

app, rt = fast_app()

# Serve files from the "img" folder (includes favicon) as static files
app.mount("/img", StaticFiles(directory="img"), name="img")
app.mount("/pdf", StaticFiles(directory="pdf"), name="pdf")  # Serve files from the "pdf" folder as static files

def render_head(title):
    """Render the <head> section, setting the title and favicon explicitly."""
    return Head(
        Title(title),  # Set the tab title dynamically
        Link(rel="icon", href="/img/favicon.ico?v=2"),  # Path to your favicon with cache-busting parameter
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    )

def render_footer():
    """Render the footer section similar to Code.Sydney with Privacy Policy, Terms links, and logos."""
    return Div(
        Div(
            Div(
                P(
                    "A joint Initiative by ",
                    A(
                        Img(
                            src="/img/cslogo.png",
                            alt="Code.Sydney Logo",
                            _style="width: 20px; vertical-align: middle; margin-right: 5px;"
                        ),
                        "Code.Sydney",
                        href="https://www.code.sydney",
                        target="_blank"
                    ),
                    " | ",
                    A(
                        Img(
                            src="/img/deplogo.png",
                            alt="Data Engineering Pilipinas Logo",
                            _style="width: 20px; vertical-align: middle; margin-right: 5px;"
                        ),
                        "Data Engineering Pilipinas",
                        href="https://dataengineering.ph",
                        target="_blank"
                    )
                ),
                _style="text-align: center; margin: 10px 0;"
            ),
            Div(
                P(
                    A("Privacy Policy", href="/pdf/Code.Sydney_Website_Privacy_Policy_2025.pdf", target="_blank"),
                    " | ",
                    A("Terms", href="/pdf/Code.Sydney_Client_Terms_2025.pdf", target="_blank"),
                ),
                _style="text-align: center; margin: 10px 0; font-size: small;"
            ),
            Div(
                P("© 2025 Code.Sydney. All rights reserved."),
                _style="text-align: center; margin: 10px 0; font-size: small; color: gray;"
            ),
            _style="background-color: #f8f9fa; padding: 20px; border-top: 1px solid #ddd;"
        )
    )


def render_page(heading, placeholder, cards):
    """Render content for both Home and Portfolios tabs with dynamic heading, placeholder, and cards."""
    return Body(
        Div(
            styles,
            Div(
                Img(
                    src="/img/DataMentorsLogo.png",
                    alt="DataMentors Logo",
                    _style="width: 200px; margin-bottom: 10px;"
                ),
                _style="text-align: center;"
            ),
            H1("Data Mentors", _style="text-align: center; margin-bottom: 20px;"),
            H2(heading, _style="text-align: center; margin-bottom: 20px;"),
            Div(
                P(
                    "A joint Initiative by ",
                    A(
                        Img(
                            src="/img/cslogo.png",
                            alt="Code.Sydney Logo",
                            _style="width: 20px; vertical-align: middle; margin-right: 5px;"
                        ),
                        "Code.Sydney",
                        href="https://www.code.sydney",
                        target="_blank"
                    ),
                    " | ",
                    A(
                        Img(
                            src="/img/deplogo.png",
                            alt="Data Engineering Pilipinas Logo",
                            _style="width: 20px; vertical-align: middle; margin-right: 5px;"
                        ),
                        "Data Engineering Pilipinas",
                        href="https://dataengineering.ph",
                        target="_blank"
                    )
                ),
                _style="text-align: center; margin: 10px 0;"
            ),            
            Div(
                Input(_type="text", _placeholder=placeholder, _id="search-input", _style="padding: 10px; width: 300px;"),
                _style="margin: 20px;"
            ),
            Div(
                *cards,  # Render cards dynamically
                _id="portfolio-container",
                _style="display: flex; flex-wrap: wrap; justify-content: center;"
            ),
            Script("""
            document.getElementById('search-input').addEventListener('input', function() {
                const query = this.value.toLowerCase(); // Convert query to lowercase
                const cards = document.querySelectorAll('.card'); // Select all cards

                cards.forEach(card => {
                    const title = card.querySelector('.card-title').textContent.toLowerCase(); // Get card-title text
                    const description = card.querySelector('.card-description').textContent.toLowerCase(); // Get card-description text

                    // Check if query matches either title or description
                    const isMatch = title.includes(query) || description.includes(query);

                    card.style.display = isMatch ? 'block' : 'none'; // Show or hide cards based on match
                });
            });
            """),
            _style="text-align: center; font-family: Arial, sans-serif;"
        )
    )

def render_navbar():
    """Render the burger menu for navigation."""
    return Div(
        Div(
            Div("☰", _class="burger-icon"),
            Div(
                A("Home", href="/", _class="menu-item", _style="display: block; padding: 10px 20px;"),
                A("Portfolios", href="/portfolios", _class="menu-item", _style="display: block; padding: 10px 20px;"),
                _class="menu-content",
                _style="display: none; position: absolute; top: 40px; right: 0; background-color: white; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); z-index: 999;"
            ),
            _style="position: relative;"
        ),
        Script("""
        const burgerIcon = document.querySelector('.burger-icon');
        const menuContent = document.querySelector('.menu-content');

        burgerIcon.addEventListener('click', () => {
            menuContent.style.display = menuContent.style.display === 'block' ? 'none' : 'block';
        });

        window.addEventListener('click', (event) => {
            if (!event.target.matches('.burger-icon')) {
                menuContent.style.display = 'none';
            }
        });
        """),
        _style="position: fixed; top: 10px; right: 10px; padding: 10px; background-color: #f8f9fa; border-radius: 5px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); z-index: 1000;"
    )

@rt("/")
def get(req):
    return Html(
        render_head("Data Mentors - Home"),  # Set the title for the Home page
        render_navbar(),
        render_page("", "Search mentors...", MENTOR_CARDS),
        render_footer()
    )

@rt("/portfolios")
def portfolios(req):
    return Html(
        render_head("Data Mentors - Portfolios"),  # Set the title for the Portfolios page
        render_navbar(),
        render_page("", "Search portfolios...", PORTFOLIO_CARDS),
        render_footer()
    )

serve()
