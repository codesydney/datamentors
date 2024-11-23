from fasthtml.common import *
from fastapi.staticfiles import StaticFiles
from styles import styles
from cards import MENTOR_CARDS, PORTFOLIO_CARDS

app, rt = fast_app()

# Serve files from the "pdf" folder as static files
app.mount("/pdf", StaticFiles(directory="pdf"), name="pdf")

def render_page(title, heading, placeholder, cards):
    """Render content for both Home and Portfolios tabs with dynamic heading, placeholder, and cards."""
    return Div(
        styles,
        Div(
            Img(
                src="img/DataMentorsLogo.png",
                alt="DataMentors Logo",
                _style="width: 200px; margin-bottom: 10px;"
            ),
            _style="text-align: center;"
        ),
        H1("Data Mentors", _style="text-align: center; margin-bottom: 20px;"),
        H2(heading, _style="text-align: center; margin-bottom: 20px;"),
        P(
            "A Joint Initiative by ",
            A("Code.Sydney", href="https://www.code.sydney", target="_blank"),
            " and ",
            A("Data Engineering Pilipinas", href="https://dataengineering.ph/", target="_blank")
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

def render_navbar():
    """Render the burger menu for navigation."""
    return Div(
        Div(
            Div("☰", _class="burger-icon"),
            Div(
                A("Home", href="/", _class="menu-item", _style="display: block; padding: 10px 20px;"),
                A("Portfolios", href="/portfolios", _class="menu-item", _style="display: block; padding: 10px 20px;"),
                _class="menu-content"
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
        _style="position: fixed; top: 10px; right: 10px; z-index: 1000;"
    )

@rt("/")
def get(req):
    return Div(
        render_navbar(),
        render_page("Home", "", "Search mentors...", MENTOR_CARDS),
        _style="font-family: Arial, sans-serif;"
    )

@rt("/portfolios")
def portfolios(req):
    return Div(
        render_navbar(),
        render_page("Portfolios", "", "Search portfolios...", PORTFOLIO_CARDS),
        _style="font-family: Arial, sans-serif;"
    )

serve()
