# SB MUCH REX GLOBAL ENTERPRISES – Django website

A professional multi-page website covering every service listed on the LinkedIn profile:

**Import · Export · General Merchant · General Contractor · Travel & Tours · Immigration Consultancy · Real Estate · FMCG · Business Registration · Wines & Spirits · Pharma**

- Everything public (home, about, services, FAQ, contact) works **without logging in**.
- Optional accounts: visitors can register/log in to get a **personal dashboard** (submit service requests, track status, read notes from you, edit their profile, change password).
- You manage everything (services text, FAQs, enquiries, client requests) from the Django admin.

## Quick start

```bash
cd agujioke_site

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations core accounts
python manage.py migrate
python manage.py seed_services     # loads the 11 services + long-form content + FAQs
python manage.py createsuperuser   # your admin login

python manage.py runserver
```

Open http://127.0.0.1:8000/ and the admin at http://127.0.0.1:8000/admin/.

Run the tests with `python manage.py test` (after the `makemigrations` step above).

## Things to edit before going live

1. **Contact details**: `config/settings.py` → `SITE_CONFIG` (email, phone, WhatsApp number, address, LinkedIn URL). They are placeholders now. You can also set the environment variables `SITE_EMAIL`, `SITE_PHONE`, `SITE_WHATSAPP`, `SITE_ADDRESS`, `SITE_LINKEDIN`.
2. **Site/brand name**: `SITE_CONFIG["name"]` (currently "SB MUCH REX GLOBAL ENTERPRISES").
3. **Service text**: edit in the admin (Core → Services), or in `core/seed_data_part1.py` / `core/seed_data_part2.py` and re-run `python manage.py seed_services` (this overwrites service text and FAQs).
4. **Photo / logo**: the About page uses an "SA" initials avatar. Put a photo in `static/img/` and swap it into `templates/core/about.html`.
5. **Review the content** with the business owner. The copy is general guidance written from the profile headline; check that it matches what is actually offered, and that regulatory statements (NAFDAC, SON, CAC, immigration, licences) are current.

## Project layout

```
agujioke_site/
├── manage.py
├── requirements.txt
├── config/                 # settings, root urls, wsgi/asgi
├── core/                   # public site: Service, FAQ, Inquiry models, pages, seed command
│   ├── seed_data_part1.py  # long-form content: services 1-6
│   ├── seed_data_part2.py  # long-form content: services 7-11 + general FAQs
│   └── management/commands/seed_services.py
├── accounts/               # registration, login, dashboard, profile, service requests
├── templates/              # base.html, core/, accounts/, partials/
└── static/                 # css/style.css, js/main.js
```

## Pages & URLs

| URL | Description | Login needed |
|---|---|---|
| `/` | Home | No |
| `/about/` | About | No |
| `/services/` | All services | No |
| `/services/<slug>/` | Service detail (long-form) | No |
| `/faq/` | FAQ | No |
| `/contact/` | Enquiry form | No |
| `/accounts/register/` `/accounts/login/` | Sign up / log in | No |
| `/accounts/dashboard/` | Client dashboard | **Yes** |
| `/accounts/requests/`, `/new/`, `/<id>/` | Service requests | **Yes** |
| `/accounts/profile/`, `/accounts/password/` | Profile & password | **Yes** |
| `/staff/` | **Staff review panel** (dashboard) | **Staff only** |
| `/staff/requests/` | Every client's requests, with search and filters | **Staff only** |
| `/staff/requests/<id>/` | Review a request: **Accept / Reject**, write a note | **Staff only** |
| `/staff/enquiries/` | Contact-form enquiries, mark as handled | **Staff only** |
| `/admin/` | Django admin site | Staff |

Clients only ever see their own requests. In the admin you can change a request's status and add a note that appears on the client's dashboard.

## How the owner/admin reviews client requests

1. Log in with the account created by `createsuperuser` (or any user you tick **Staff status** for in `/admin/`). A gold **Staff Panel** button appears in the top menu. Clients never see it.
2. The staff dashboard shows how many requests are Pending, In review, Accepted, In progress, Completed and Rejected, and lists the ones **waiting for your decision**.
3. Open a request to read the full details and the client's contact/company information, then press **Accept** or **Reject**. A rejection needs a short reason. You can also set other statuses (In review, In progress, Completed) and write a note.
4. The client sees the new status and your note on their own dashboard, and gets an email notification (printed in the terminal during development until SMTP is configured).
5. `/staff/` is protected: visitors who are not logged in are redirected to the login page; logged-in clients get an "Access denied" page.

To add another staff member: Django admin → Users → tick **Staff status**.

## Deploying

Set these environment variables in production:

```
DJANGO_DEBUG=0
DJANGO_SECRET_KEY=<long random string>
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

Then run `python manage.py collectstatic`, serve with gunicorn/uWSGI behind nginx (or a platform such as Render/Railway), and serve `/static/` (for example with WhiteNoise or nginx). Switch `DATABASES` to PostgreSQL for real traffic. To receive enquiry emails, configure SMTP settings and send mail from `core.views.contact`; for now enquiries are stored in the admin.
"# Agujioke_Business_Services" 
