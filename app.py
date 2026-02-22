from flask import Flask, render_template, request, jsonify
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

app = Flask(__name__)

# Load model and tokenizer from Hugging Face
MODEL_NAME = "ajaykumarreddynelavetla/youtube-viral-predictor"

print("Loading model from Hugging Face...")
try:
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    model.eval()
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None
    tokenizer = None


def predict_virality(title, tags, category, likes, comments, views):
    """Predict if a YouTube video has viral potential"""
    
    if model is None or tokenizer is None:
        return "Error: Model not loaded"
    
    prompt = f"""Analyze this YouTube video and predict viral potential:

Title: {title}
Tags: {tags}
Category: {category}
Likes: {likes:,}
Comments: {comments:,}
Views: {views:,}

Prediction:"""
    
    try:
        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=30,
                do_sample=False,
                temperature=0.7,
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        prediction = response.split("Prediction:")[-1].strip()
        
        if not prediction or prediction.lower() == "none":
            # Fallback prediction based on views
            if views > 1000000:
                return "🎯 VIRAL POTENTIAL: High - This video shows strong viral indicators!"
            elif views > 100000:
                return "📈 MODERATE POTENTIAL: This video could perform well with the right audience."
            else:
                return "📊 LOW POTENTIAL: This video may need optimization for viral reach."
        
        return prediction
    except Exception as e:
        return f"Error generating prediction: {str(e)}"


@app.route('/')
def home():
    """Render homepage"""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint for predictions"""
    try:
        data = request.json
        
        # Validate inputs
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        title = str(data.get('title', '')).strip()
        tags = str(data.get('tags', '')).strip()
        category = str(data.get('category', '')).strip()
        
        try:
            likes = int(data.get('likes', 0))
            comments = int(data.get('comments', 0))
            views = int(data.get('views', 0))
        except (ValueError, TypeError):
            return jsonify({"error": "Likes, comments, and views must be numbers"}), 400
        
        if not title or not tags or not category:
            return jsonify({"error": "Title, tags, and category are required"}), 400
        
        # Get prediction
        prediction = predict_virality(title, tags, category, likes, comments, views)
        
        return jsonify({
            "success": True,
            "title": title,
            "tags": tags,
            "category": category,
            "likes": likes,
            "comments": comments,
            "views": views,
            "prediction": prediction
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None,
        "model_name": MODEL_NAME
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
