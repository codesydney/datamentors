from fasthtml.common import Style

styles = Style("""
    .card-content {
        width: 600px;
        height: auto;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-image {
        background-size: contain; /* Ensure the entire image fits inside */
        background-repeat: no-repeat; /* Prevent repeating of the image */
        background-position: center; /* Center the image */
        width: 600px;
        height: 600px; /* Adjust height to match aspect ratio if needed */
    }
    .card-title {
        margin: 10px 0; /* Explicit margin control */
        padding: 0;
        font-size: 18px;
        text-align: center;
    }
    .card-description {
        margin: 5px 0; /* Space between description lines */
        padding: 0;
        font-size: 16px;
        text-align: center;
    }
    .card-description-small {
        margin: 5px 0; /* Adjust spacing for smaller text */
        padding: 0;
        font-size: 14px; /* Smaller font size for specific lines */
        text-align: center;
    }
    .linkedin-icon {
        width: 25px;
        height: 25px;
    }
    .linkedin-link {
        display: block;
        text-align: center;
        margin: 10px 0; /* Ensure spacing for the LinkedIn icon */
        padding: 0;
    }
    .github-icon {
        width: 25px; /* Same size as the LinkedIn icon */
        height: 25px;
        vertical-align: middle; /* Align vertically similar to LinkedIn icon */
        margin: 10px auto; /* Center and add spacing for the icon */
    }
    .github-link {
        display: block;
        text-align: center;
        margin: 10px 0; /* Ensure spacing for the GitHub icon */
        padding: 0;
    }    
    .booking-button {
        display: inline-block;
        padding: 10px 18px;
        margin: 5px auto; /* Center and add spacing above/below */
        text-align: center;
        background-color: #4c6c8c;
        color: white;
        font-size: 14px;
        text-decoration: none;
        border-radius: 10px;
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

    body, html {
        overflow-x: hidden;
    }

    a {
        text-decoration: none;
    }
""")
