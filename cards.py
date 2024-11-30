from fasthtml.common import A, Div, H3, Img, P, Style

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

def generate_portfolio_link(portfolio_link, icon_size=None):
    """Generate portfolio link with a project icon."""
    return A(
        Img(
            src="img/project-icon.png",
            alt="Project",
            _class="portfolio-icon",
            style=f"width: {icon_size}px; height: {icon_size}px;" if icon_size else ""
        ),
        href=portfolio_link,
        target="_blank",
        _class="portfolio-link"
    )

def generate_booking_button(booking_link):
    """Generate a booking button."""
    return A(
        "Book Now",
        href=booking_link,
        target="_blank",
        _class="booking-button",
        style="border: 1px solid #000; padding: 10px;"
    )

def card_3d(title, background, line1, line2, link, show_booking=True, booking_link="", is_portfolio=False, icon_size=None):
    """Generate a 3D card component with mentor or portfolio details."""
    card_body = [
        H3(line1, _class="card-title"),
        P(line2, _class="card-description"),
    ]
    if show_booking and not is_portfolio:
        card_body.append(generate_booking_button(booking_link))
        card_body.append(P(" ", _class="spacer", style="margin: 5px 0;"))  # Adjust margins
    
    if is_portfolio:
        card_body.append(generate_portfolio_link(link, icon_size))
    else:
        card_body.append(generate_linkedin_link(link))

    return Div(
        Div(
            Div(
                _style=f"""
                    background-image: url('{background}');
                    width: 600px;
                    height: 450px;
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
        _data_description=line1
    )

MENTOR_CARDS = [
    card_3d(
        "Mentor 1 | ",
        "img/DM-Engramar.png",
        "Engramar Bollas",
        "Basic Python Mentor ($0 per hour)",
        "https://linkedin.com/in/engramarbollas",
        show_booking=True,
        booking_link="https://koalendar.com/e/meet-with-code-sydney"
    )
]

PORTFOLIO_CARDS = [
    card_3d(
        "Emigrant Data Analysis (1981-2022)",
        "img/DEP4G-Emigration.png",
        "Analysis of emigration trends",
        "Chris Formoso",
        "https://github.com/dataengineeringpilipinas/datahub/blob/main/docs/projects/emigrant-country-dashboard.md",
        show_booking=False,
        is_portfolio=True,
        icon_size=50
    ),
    card_3d(
        "Foreign Spouse Exploratory Data Analysis",
        "img/DEP4G-Foreign-Spouse.png",
        "Insights into foreign spouse demographics",
        "Jun Miano",
        "https://github.com/Junmiano/DEP/tree/main",
        show_booking=False,
        is_portfolio=True,
        icon_size=50
    ),
    card_3d(
        "Stormchaser",
        "img/DEP4G-StormChaser.png",
        "A simulated real-time typhoon visualization system that scrapes and animates tropical storms worldwide.",
        "Noel Adante",
        "https://github.com/TreacherousDev/Stormchaser",
        show_booking=False,
        is_portfolio=True,
        icon_size=50
    )    
]
