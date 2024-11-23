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
        background-size: cover;
        background-position: center;
        width: 600px;
        height: 550px;
    }
    .card-title {
        margin-top: 10px;
        margin-bottom: 0;
        padding: 0;
        font-size: 18px;
        text-align: center;
    }
    .card-description {
        margin: 0;
        padding: 0;
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
        margin: 0;
        padding: 0;
    }
    .booking-button {
        display: inline-block;
        padding: 5px 16px;
        margin: 0 auto;
        text-align: center;
        background-color: #ffffff;
        color: black;
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
