# Deployment Guide - Render

## 📦 What's Configured:
- `render.yaml` - Render configuration
- `requirements.txt` - Python dependencies with gunicorn & flask-cors
- `app.py` - Flask app serving frontend + backend
- `.gitignore` - Git ignore file

---

## 🚀 Deployment Steps

### STEP 1: Push to GitHub

1. **Initialize Git (if not done):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   ```

2. **Create GitHub repository:**
   - Go to https://github.com/new
   - Repository name: `fruit-image-classifier`
   - Make it **PUBLIC** (required for free tier)
   - Don't initialize with README
   - Click "Create repository"

3. **Push code:**
   ```bash
   git remote add origin https://github.com/vaironix/fruit-image-classifier.git
   git push -u origin main
   ```

---

### STEP 2: Deploy on Render

1. **Sign up/Login:**
   - Go to https://render.com
   - Sign up or login with GitHub

2. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Click "Connect account" to authorize GitHub
   - Find and select your `fruit-image-classifier` repository
   - Click "Connect"

3. **Configure (Auto-detected from render.yaml):**
   - **Name**: fruit-classifier (or your choice)
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free

4. **Deploy:**
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Watch the logs for progress

5. **Your app is live!**
   - URL: `https://fruit-classifier-xxxx.onrender.com`
   - Copy this URL

---

## ✅ Testing Your Deployment

1. Open your Render URL in browser
2. You should see the Fruit Classifier interface
3. Upload a fruit image (apple, banana, cherry, or mango)
4. Click "Predict"
5. See the prediction result with confidence score

---

## ⚠️ Important Notes

### Free Tier Limitations:
- **Spin down**: App sleeps after 15 minutes of inactivity
- **Cold start**: First request after sleep takes 30-60 seconds
- **RAM**: 512MB limit (MobileNetV2 fits within this)
- **Build time**: 5-10 minutes on first deploy

### Keep Your App Awake (Optional):
Use a service like **UptimeRobot** or **Cron-job.org** to ping your app every 10 minutes:
- Ping URL: `https://your-app.onrender.com`
- Interval: Every 10 minutes

---

## 🔄 Updating Your App

When you make changes:

```bash
git add .
git commit -m "Your update message"
git push
```

Render will automatically detect the push and redeploy (takes 3-5 minutes).

---

## 🐛 Troubleshooting

### Build Failed:
- Check Render logs for error messages
- Verify all files are committed to GitHub
- Ensure `model/fruit_model.h5` is in repository

### App Not Loading:
- Wait 30-60 seconds (cold start)
- Check Render logs for errors
- Verify Python version compatibility

### Model Not Found:
- Ensure `model/` folder is in GitHub
- Check file paths in `app.py`
- Verify `fruit_model.h5` and `labels.txt` exist

### Out of Memory:
- Model is too large for 512MB
- Consider using a smaller model
- Or upgrade to paid Render plan

---

## 📊 Monitoring

**View Logs:**
- Go to Render dashboard
- Click your service
- Click "Logs" tab
- See real-time application logs

**Check Metrics:**
- CPU usage
- Memory usage
- Request count
- Response times

---

## 🎉 Success!

Your Fruit Image Classifier is now live and accessible worldwide!

Share your app URL and let others try it out! 🚀

---

## 💡 Next Steps

- Add more fruit categories
- Improve model accuracy
- Add image preprocessing
- Implement caching
- Add analytics
- Custom domain (paid feature)
