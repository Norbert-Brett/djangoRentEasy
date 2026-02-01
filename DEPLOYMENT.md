# RentEasy - Production Deployment Guide

## 📋 Pre-Deployment Checklist

### 1. Environment Variables
Copy `.env.example` to `.env` and update all values:

```bash
cp .env.example .env
```

**Critical Production Settings:**
- `DEBUG=False` - **MUST** be False in production
- `SECRET_KEY` - Generate a new secret key (use `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- `ALLOWED_HOSTS` - Add your domain(s)
- `CSRF_TRUSTED_ORIGINS` - Add your HTTPS URLs
- `DATABASE_URL` - Your production database connection string

### 2. Security Checklist
- ✅ `DEBUG=False` in production
- ✅ Strong `SECRET_KEY` (never commit to git)
- ✅ HTTPS enabled (handled by deployment platform)
- ✅ Database credentials secured
- ✅ Email credentials secured
- ✅ Cloudinary credentials secured (if using)

### 3. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

### 4. Static Files
The app uses **WhiteNoise** for serving static files in production:
- Static files are automatically compressed and cached
- No CDN required (but recommended for large-scale apps)
- Files are collected to `staticfiles/` directory

### 5. Media Files
Two options:

**Option A: Local Storage (Small scale)**
- Set `USE_CLOUDINARY=False`
- Media files stored in `media/` directory
- Ensure your deployment platform persists the media directory

**Option B: Cloudinary (Recommended for production)**
- Set `USE_CLOUDINARY=True`
- Configure Cloudinary credentials in `.env`
- Media files automatically uploaded to Cloudinary

---

## 🚀 Deployment Platforms

### Heroku Deployment

1. **Install Heroku CLI**
```bash
brew install heroku/brew/heroku  # macOS
```

2. **Login and Create App**
```bash
heroku login
heroku create your-app-name
```

3. **Add PostgreSQL Database**
```bash
heroku addons:create heroku-postgresql:mini
```

4. **Set Environment Variables**
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
heroku config:set CSRF_TRUSTED_ORIGINS="https://your-app-name.herokuapp.com"
heroku config:set ADMIN_URL="your-secret-admin-path/"
# Add other variables as needed
```

5. **Deploy**
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py collectstatic --noinput
```

6. **Open App**
```bash
heroku open
```

---

### Railway Deployment

1. **Install Railway CLI**
```bash
npm install -g @railway/cli
```

2. **Login and Initialize**
```bash
railway login
railway init
```

3. **Add PostgreSQL Database**
- Go to Railway dashboard
- Click "New" → "Database" → "PostgreSQL"
- Copy the `DATABASE_URL` from the database settings

4. **Set Environment Variables**
In Railway dashboard, add:
- `DEBUG=False`
- `SECRET_KEY=your-secret-key`
- `ALLOWED_HOSTS=your-app.railway.app`
- `CSRF_TRUSTED_ORIGINS=https://your-app.railway.app`
- `DATABASE_URL` (automatically set by Railway)

5. **Deploy**
```bash
railway up
```

---

### Render Deployment

1. **Create Account** at [render.com](https://render.com)

2. **Create PostgreSQL Database**
- Dashboard → New → PostgreSQL
- Copy the "Internal Database URL"

3. **Create Web Service**
- Dashboard → New → Web Service
- Connect your GitHub repository
- Configure:
  - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
  - **Start Command**: `gunicorn djangorenteasy.wsgi:application`

4. **Set Environment Variables**
In Render dashboard, add:
- `DEBUG=False`
- `SECRET_KEY=your-secret-key`
- `ALLOWED_HOSTS=your-app.onrender.com`
- `CSRF_TRUSTED_ORIGINS=https://your-app.onrender.com`
- `DATABASE_URL` (from step 2)
- `PYTHON_VERSION=3.11.0`

5. **Deploy**
- Render automatically deploys on git push

---

### DigitalOcean App Platform

1. **Create Account** at [digitalocean.com](https://www.digitalocean.com)

2. **Create App**
- Apps → Create App
- Connect GitHub repository
- Choose branch to deploy

3. **Add Database**
- Add Component → Database → PostgreSQL
- Copy connection string

4. **Configure Build**
- **Build Command**: `pip install -r requirements.txt`
- **Run Command**: `gunicorn djangorenteasy.wsgi:application --bind 0.0.0.0:$PORT`

5. **Set Environment Variables**
- `DEBUG=False`
- `SECRET_KEY=your-secret-key`
- `ALLOWED_HOSTS=${APP_DOMAIN}`
- `CSRF_TRUSTED_ORIGINS=https://${APP_DOMAIN}`
- `DATABASE_URL` (from database)

6. **Run Migrations**
```bash
doctl apps create-deployment <app-id>
# Then run migrations via console or job
```

---

## 🔧 Post-Deployment Tasks

### 1. Create Superuser
```bash
# Heroku
heroku run python manage.py createsuperuser

# Railway
railway run python manage.py createsuperuser

# Render (use shell in dashboard)
python manage.py createsuperuser
```

### 2. Access Admin Panel
Navigate to: `https://your-domain.com/your-secret-admin-path/`

### 3. Create Host Profiles
- Login to admin panel
- Create Host profiles and link them to user accounts
- Users with host profiles can access `/hosts/dashboard`

### 4. Test Core Features
- ✅ User registration and login
- ✅ Browse listings
- ✅ Save listings (requires login)
- ✅ Contact host (requires login)
- ✅ Share listings (public)
- ✅ Host dashboard (for users with host profiles)
- ✅ User dashboard (saved listings, inquiries)

---

## 📊 Monitoring & Logs

### View Logs
```bash
# Heroku
heroku logs --tail

# Railway
railway logs

# Render
# View in dashboard under "Logs" tab
```

### Error Tracking
Production logging is configured to:
- Log errors to `logs/django_errors.log`
- Output INFO level to console
- Capture Django errors automatically

---

## 🔒 Security Best Practices

1. **Never commit `.env` file** - Already in `.gitignore`
2. **Use strong SECRET_KEY** - Generate new for production
3. **Enable HTTPS** - Handled by deployment platform
4. **Regular updates** - Keep dependencies updated
5. **Database backups** - Enable on your platform
6. **Monitor logs** - Check for suspicious activity
7. **Rate limiting** - Consider adding django-ratelimit for API endpoints

---

## 🆘 Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
# Ensure STATIC_ROOT is set correctly
```

### Database Connection Issues
- Verify `DATABASE_URL` is correct
- Check database is running
- Ensure IP whitelist includes your app

### 500 Errors
- Check logs for detailed error
- Verify all environment variables are set
- Ensure migrations are applied

### CSRF Errors
- Verify `CSRF_TRUSTED_ORIGINS` includes your domain with `https://`
- Check `ALLOWED_HOSTS` includes your domain

---

## 📈 Performance Optimization

### Recommended Additions
1. **Redis** - For caching and sessions
2. **CDN** - For static files (Cloudflare, AWS CloudFront)
3. **Database Connection Pooling** - pgBouncer
4. **Monitoring** - Sentry for error tracking
5. **APM** - New Relic or DataDog for performance monitoring

---

## 📝 Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DEBUG` | Yes | False | Debug mode (MUST be False in production) |
| `SECRET_KEY` | Yes | - | Django secret key |
| `ALLOWED_HOSTS` | Yes | - | Comma-separated list of allowed hosts |
| `CSRF_TRUSTED_ORIGINS` | Yes | - | Comma-separated HTTPS origins |
| `DATABASE_URL` | Yes | - | PostgreSQL connection string |
| `ADMIN_URL` | No | admin/ | Custom admin URL path |
| `USE_CLOUDINARY` | No | False | Enable Cloudinary for media files |
| `CLOUD_NAME` | If Cloudinary | - | Cloudinary cloud name |
| `API_KEY` | If Cloudinary | - | Cloudinary API key |
| `API_SECRET` | If Cloudinary | - | Cloudinary API secret |
| `EMAIL_BACKEND` | No | console | Email backend class |
| `EMAIL_HOST` | No | localhost | SMTP host |
| `EMAIL_PORT` | No | 587 | SMTP port |
| `EMAIL_USE_TLS` | No | True | Use TLS for email |
| `EMAIL_HOST_USER` | No | - | SMTP username |
| `EMAIL_HOST_PASSWORD` | No | - | SMTP password |

---

## ✅ Production Checklist

Before going live:
- [ ] `DEBUG=False`
- [ ] Strong `SECRET_KEY` set
- [ ] `ALLOWED_HOSTS` configured
- [ ] `CSRF_TRUSTED_ORIGINS` configured
- [ ] Database migrations applied
- [ ] Superuser created
- [ ] Static files collected
- [ ] Media storage configured (local or Cloudinary)
- [ ] Email configured
- [ ] HTTPS enabled
- [ ] Logs directory created (`mkdir -p logs`)
- [ ] All environment variables set
- [ ] Database backups enabled
- [ ] Error monitoring setup (optional but recommended)

---

## 🎉 You're Ready!

Your RentEasy application is now production-ready with:
- ✅ Security hardening (HTTPS, HSTS, secure cookies)
- ✅ Static file optimization (WhiteNoise compression)
- ✅ Database-backed saved listings
- ✅ Authentication-required features
- ✅ Host and user dashboards
- ✅ Production logging
- ✅ Environment-based configuration

For support or questions, refer to the Django documentation or create an issue in the repository.
