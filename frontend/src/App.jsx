import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const API_BASE_URL = 'http://localhost:8001';

  useEffect(() => {
    fetchReviews();
  }, []);

  const fetchReviews = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/reviews`);
      if (!response.ok) {
        throw new Error('Failed to fetch reviews');
      }
      const data = await response.json();
      setReviews(data);
    } catch (err) {
      setError('Error loading reviews: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleString();
  };

  if (loading) {
    return (
      <div className="app">
        <div className="loading">Loading reviews...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app">
        <div className="error">{error}</div>
      </div>
    );
  }

  return (
    <div className="app">
      <header className="header">
        <h1>Product Reviews</h1>
        <p>Reviews submitted via WhatsApp</p>
        <button onClick={fetchReviews} className="refresh-btn">
          Refresh Reviews
        </button>
      </header>

      <div className="reviews-container">
        {reviews.length === 0 ? (
          <div className="no-reviews">
            No reviews yet. Send a message to the WhatsApp number to get started!
          </div>
        ) : (
          <div className="reviews-list">
            {reviews.map((review) => (
              <div key={review.id} className="review-card">
                <div className="review-header">
                  <h3 className="product-name">{review.product_name}</h3>
                  <span className="timestamp">{formatDate(review.created_at)}</span>
                </div>
                <p className="review-text">"{review.product_review}"</p>
                <div className="review-footer">
                  <span className="user-info">{review.user_name}</span>
                  <span className="contact">{review.contact_number}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;