# Deployment Guide - Vercel + Render

## 📦 Files Created:
- `render.yaml` - Render configuration
- `vercel.json` - Vercel configuration  
- `index.html` - Root HTML file for Vercel
- `.gitignore` - Git ignore file
- Updated `app.py` - Added CORS support
- Updated `requirements.txt` - Added gunicorn & flask-cors
- Updated `script.js` - API URL configuration

---

## 🚀 STEP 1: Deploy Backend to Render

1. **Push code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to https://render.com
   - Sign up/Login with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect `render.yaml`
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment

3. **Copy your Render URL:**
   - Example: `https://fruit-classifier-api-xxxx.onrender.com`

---

## 🌐 STEP 2: Update Frontend with Backend URL

1. **Edit `static/js/script.js`:**
   - Replace `https://your-app-name.onrender.com` 
   - With your actual Render URL

2. **Commit the change:**
   ```bash
   git add static/js/script.js
   git commit -m "Update API URL"
   git push
   ```

---

## 🎨 STEP 3: Deploy Frontend to Vercel

1. **Deploy on Vercel:**
   - Go to https://vercel.com
   - Sign up/Login with GitHub
   - Click "Add New" → "Project"
   - Import your GitHub repository
   - Vercel will auto-detect `vercel.json`
   - Click "Deploy"
   - Wait 1-2 minutes

2. **Your app is live!**
   - Vercel URL: `https://your-app.vercel.app`

---

## ✅ Testing

1. Open your Vercel URL
2. Upload a fruit image
3. Click "Predict"
4. See the result!

---

## ⚠️ Important Notes

- **Render free tier**: App sleeps after 15 min inactivity (30s cold start)
- **Model size**: 512MB RAM limit on Render (MobileNetV2 should fit)
- **First request**: May take 30-60 seconds if app is sleeping

---

## 🐛 Troubleshooting

**Backend not responding:**
- Check Render logs for errors
- Verify model files are in repository

**CORS errors:**
- Ensure `flask-cors` is installed
- Check API URL in `script.js`

**Model too large:**
- Consider using Hugging Face Spaces instead
