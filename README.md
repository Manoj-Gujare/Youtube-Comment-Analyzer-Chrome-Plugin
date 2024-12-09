# YouTube Comment Analyzer Chrome Plugin

This project is a Flask-based API designed to analyze YouTube comments. It includes features like sentiment analysis, word cloud generation, trend visualization, and timestamp-based comment analysis. The API is built to work seamlessly with a Chrome plugin for real-time comment analysis.

## Features

1. **Sentiment Analysis**: 
   - Analyze the sentiment of YouTube comments (Positive, Neutral, Negative).
   - Supports preprocessing to enhance the accuracy of predictions.

2. **Word Cloud Generation**:
   - Creates a visually appealing word cloud based on YouTube comments.
   - Excludes stopwords to focus on meaningful content.

3. **Trend Visualization**:
   - Generates a trend graph to visualize sentiment trends over time.
   - Displays sentiment percentages for Positive, Neutral, and Negative comments.

4. **Timestamp-Based Analysis**:
   - Includes timestamp data with comments for enhanced contextual analysis.

5. **Chart Generation**:
   - Provides pie charts showcasing sentiment distribution.

## Tech Stack

- **Backend**: Flask
- **Machine Learning**: MLflow, Scikit-learn
- **Visualization**: Matplotlib, WordCloud
- **Data Preprocessing**: Pandas, NLTK
- **Deployment**: MLflow Model Registry, Dagshub
