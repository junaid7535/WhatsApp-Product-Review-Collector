from fastapi import FastAPI, Depends, Form
from sqlalchemy.orm import Session
from twilio.twiml.messaging_response import MessagingResponse
from database import SessionLocal, Review
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="WhatsApp Reviews API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

user_states = {}

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(
    From: str = Form(...),
    Body: str = Form(...),
    db: Session = Depends(get_db)
):
    response = MessagingResponse()
    msg = response.message()
    
    state = user_states.get(From, {"step": 0})
    
    if state["step"] == 0:
        msg.body("Which product is this review for?")
        state["step"] = 1
        state["contact_number"] = From
        
    elif state["step"] == 1:
        state["product_name"] = Body.strip()
        msg.body("What's your name?")
        state["step"] = 2
        
    elif state["step"] == 2:
        state["user_name"] = Body.strip()
        msg.body(f"Please send your review for {state['product_name']}.")
        state["step"] = 3
        
    elif state["step"] == 3:
        review = Review(
            contact_number=state["contact_number"],
            user_name=state["user_name"],
            product_name=state["product_name"],
            product_review=Body.strip()
        )
        db.add(review)
        db.commit()
        
        msg.body(f"Thanks {state['user_name']} -- your review for {state['product_name']} has been recorded.")
        del user_states[From]
    
    user_states[From] = state
    return str(response)

@app.get("/api/reviews")
def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(Review).order_by(Review.created_at.desc()).all()
    return [
        {
            "id": review.id,
            "contact_number": review.contact_number,
            "user_name": review.user_name,
            "product_name": review.product_name,
            "product_review": review.product_review,
            "created_at": review.created_at.isoformat()
        }
        for review in reviews
    ]

@app.get("/")
def root():
    return {"message": "WhatsApp Reviews API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)