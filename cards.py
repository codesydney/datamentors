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

def generate_booking_button(booking_link):
    """Generate a booking button."""
    return A(
        "Book Now",
        href=booking_link,
        target="_blank",
        _class="booking-button"
    )

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
