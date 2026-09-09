#!/usr/bin/env python3

import os
import sys
import json
from datetime import datetime
from urllib.parse import parse_qs
import html


# ---------- Read POST data ----------

content_length = int(os.environ.get("CONTENT_LENGTH", 0))
post_data = sys.stdin.read(content_length)

form = parse_qs(post_data)


def get_field(name):
    """Get a single form value."""
    return form.get(name, [""])[0].strip()


# ---------- Collect form data ----------

inquiry = {
    "submitted": datetime.now().astimezone().isoformat(),
    "parent_name": get_field("parent-name"),
    "email": get_field("email"),
    "phone": get_field("phone"),
    "grade": get_field("grade"),
    "subject": get_field("subject"),
    "needs": get_field("needs"),
    "availability": get_field("availability"),
    "location": get_field("location"),
    "additional_info": get_field("additional-info")
}


# ---------- Save inquiry ----------

inquiry_dir = "/var/www/rezniktestprep/inquiries"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
filename = f"inquiry_{timestamp}.json"
filepath = os.path.join(inquiry_dir, filename)

with open(filepath, "w", encoding="utf-8") as file:
    json.dump(inquiry, file, indent=4, ensure_ascii=False)


# ---------- Display confirmation ----------

parent_name = html.escape(inquiry["parent_name"])

print("Content-Type: text/html")
print()

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Thank You | Reznik Test Prep</title>

    <link rel="stylesheet" href="/css/style.css">
</head>

<body>

<header>
    <div class="container">

        <div class="logo">
            <a href="/index.html">
                <img src="/images/RTPlogo.png"
                     alt="Reznik Test Prep logo"
                     width="220"
                     height="220">
            </a>
        </div>

        <nav>
            <a href="/index.html">Home</a>
            <a href="/about.html">About Me</a>
            <a href="/index.html#services">Services</a>
            <a href="/index.html#rates">Rates</a>
            <a href="/contact.html">Contact</a>
        </nav>

    </div>
</header>

<main>

    <section class="contact">
        <div class="container">

            <h1>Thank You{", " + parent_name if parent_name else ""}!</h1>

            <p>
                Your message has been received. I'll review your inquiry
                and get back to you soon.
            </p>

            <p>
                I look forward to learning more about your student's needs.
            </p>

            <a href="/index.html" class="glow-btn">
                <span>Return to Home</span>
            </a>

        </div>
    </section>

</main>

<footer>
    <div class="container">
        <p>&copy; 2026 Reznik Test Prep. All rights reserved.</p>
    </div>
</footer>

</body>
</html>
""")
