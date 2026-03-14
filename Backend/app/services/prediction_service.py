from app.services import preprocess_service

def predict_text(user_text: str):

    # Step 1: Clean the text
    cleaned_text = preprocess_service.clean_text(user_text)

    # Step 2: Temporary dummy logic (still no ML)
    if "urgent hiring" in cleaned_text or "pay" in cleaned_text:
        prediction = "Fake Job"
        confidence = 0.85
    else:
        prediction = "Real Job"
        confidence = 0.75

    return {
        "cleaned_text": cleaned_text,
        "prediction": prediction,
        "confidence": confidence
    }
