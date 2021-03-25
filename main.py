from regression_model import train_model, predict
from sanic import Sanic, response as res

train_model()

app = Sanic('app')

@app.post('/api/predict')

async def predict_click(req):
    values = req.json

    prediction = predict(values['gender'], values['age'], values['hypertension'], values['heart_disease'], values['ever_married'], values['work_type'], values['residence_type'], values['avg_glucose_level'], values['bmi'], values['smoking_status'])

    return res.json(prediction)


if __name__ == '__main__':
    app.run(port=5000)