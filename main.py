from fasthtml.common import *
from fastapi.staticfiles import StaticFiles

app, rt = fast_app()

# Serve files from the "pdf" folder as static files
app.mount("/pdf", StaticFiles(directory="pdf"), name="pdf")

# Define common styles in a dedicated style tag for easier adjustments and reuse
styles = Style("""
    .card-content {
        width: 600px;
        height: auto;  /* Set to auto to allow flexible height */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-image {
        background-size: cover;
        background-position: center;
        width: 600px;
        height: 550px;  /* Adjust this height value to create the desired visual effect */
    }    
    .card-title {
        margin-top: 10px;  /* Add a top margin to create space between the card image and the title */
        margin-bottom: 0;  /* No bottom margin */
        padding: 0;  /* No padding */
        font-size: 18px;
        text-align: center;
    }
    .card-description {
        margin: 0;  /* No margin */
        padding: 0;  /* No padding */
        font-size: 16px;
        text-align: center;
    }
    .linkedin-icon {
        width: 30px;
        height: 30px;
    }
    .linkedin-link {
        display: block;
        text-align: center;
        margin: 0;  /* No margin */
        padding: 0;  /* No padding */
    }
    .booking-button {
        display: inline-block;
        padding: 8px 16px;
        margin: 0 auto;  /* Remove top margin and align centrally */
        text-align: center;
        background-color: #507499;
        color: white;
        text-decoration: none;
        border-radius: 5px;
    }
    .burger-icon {
        cursor: pointer;
        font-size: 24px;
    }
    .menu-content {
        display: none;
        position: absolute;
        top: 40px;
        right: 10px;
        background-color: white;
        border: 1px solid #ccc;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
""")

def generate_linkedin_link(linkedin_link):
    """Generate LinkedIn link with an icon."""
    return A(
        Img(
            src="img/linkedin-icon.svg",
            alt="LinkedIn",
            _class="linkedin-icon"
        ),
        href=linkedin_link,
        target="_blank",
        _class="linkedin-link"
    )

def generate_booking_button(booking_link):
    """Generate a booking button."""
    return A(
        "Book Now",
        href=booking_link,
        target="_blank",
        _class="booking-button"
    )

# Use the updated class for card image styling
def card_3d(title, background, line1, line2, linkedin_link, show_booking=True, booking_link=""):
    """Generate a 3D card component with mentor or portfolio details."""
    card_body = [
        H3(line1, _class="card-title"),
        P(line2, _class="card-description"),
    ]
    if show_booking:
        card_body.append(generate_booking_button(booking_link))
    card_body.append(generate_linkedin_link(linkedin_link))

    return Div(
        Div(
            Div(
                _style=f"""
                    background-image: url('{background}');
                    width: 600px;
                    height: 450px;  /* This matches the height set in the CSS above */
                """,
                _class="card-image"
            ),
            Div(
                *card_body,
                _class="card-content"
            ),
            _class="card-content",
        ),
        _class="card",
        _style="perspective: 1000px; margin: 20px;",
        _data_title=title,
        _data_description=line1  # Used for filtering
    )

# Cards for Mentors and Portfolios
MENTOR_CARDS = [
    card_3d(
        "Mentor 1 | ",
        "img/DM-Engramar.png",
        "Engramar Bollas",
        "Python Mentor ($35 ph)",
        "https://linkedin.com/in/engramarbollas",
        show_booking=False,
        booking_link="https://example.com/booking/engramar-bollas"
    )
]

PORTFOLIO_CARDS = [
    card_3d(
        "Emigrant Data Analysis (1981-2022)",
        "img/DEP4G-Emigration.png",
        "Analysis of emigration trends",
        "Chris Formoso",
        "https://linkedin.com/in/chris-formoso",
        show_booking=False
    ),
    card_3d(
        "Foreign Spouse Exploratory Data Analysis",
        "img/DEP4G-Foreign-Spouse.png",
        "Insights into foreign spouse demographics",
        "Jun Miano",
        "https://linkedin.com/in/junmiano1202",
        show_booking=False
    )
]

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
