# Reznik Test Prep

A responsive website for **Reznik Test Prep**, a private tutoring and academic coaching practice serving students in the Los Angeles area.

The site provides information about tutoring services, instructor background, rates, and contact options, with a focus on clear communication and a straightforward user experience for parents and students.

## Project Overview

This project was designed and built as a complete website for a solo tutoring practice.

The site includes:

- Responsive layouts for desktop and mobile devices
- Home, About, and Contact pages
- Service descriptions and tutoring approach
- Session rates and location information
- Contact and consultation request form
- Server-side form processing
- Private storage of submitted inquiries
- HTTPS encryption
- Production deployment on a self-managed web server

## Technology Stack

### Front End

- HTML5
- CSS3
- Responsive CSS media queries
- JavaScript

### Back End

- Python
- Python CGI
- Apache HTTP Server

### Deployment & Infrastructure

- Linux
- Apache
- Let's Encrypt
- Cloudflare DNS and proxy
- Git / GitHub
- Self-hosted web server

## Key Features

### Responsive Design

The website was designed to work across desktop, tablet, and mobile screen sizes.

Responsive behavior includes:

- Flexible page containers
- Responsive image sizing
- Mobile navigation
- Stacked service and rate cards
- Mobile-friendly contact forms
- Adjusted spacing and typography for smaller screens

### Contact Form

The contact page provides a structured inquiry form for prospective clients.

Submitted information is processed by a Python CGI application and stored privately on the server rather than being exposed through the public website.

The application handles:

- Form parsing
- Input validation
- HTML escaping
- Timestamped inquiry records
- Private server-side storage

### HTTPS

The production site uses HTTPS with a Let's Encrypt TLS certificate.

HTTP requests are redirected to HTTPS to ensure that visitors interact with the secure version of the site.

### DNS & Deployment

Cloudflare is used for DNS management and web traffic proxying.

The site itself is deployed on a Linux-based self-managed server running Apache.

The deployment architecture provides hands-on experience with:

- DNS configuration
- TLS certificates
- Apache virtual hosts
- HTTP-to-HTTPS redirection
- Linux server administration
- Git-based source control

## Project Structure

```text
rezniktestprep/
├── .gitignore
├── cgi-bin/
│   └── contact.py
└── htdocs/
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── css/
    │   ├── style.css
    │   └── style-generic-new-feel.css
    ├── images/
    │   ├── Chalkboard.png
    │   └── RTPlogo.png
    └── js/

