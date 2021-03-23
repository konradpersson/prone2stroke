from regression_model import train_model, predict
from sanic import Sanic, response as res

train_model()

app = Sanic('app')

@app.post('/api/predict')

async def predict_click(req):
    values = req.json

    prediction = predict(values['age'], values['income'])

    return res.json(prediction)


if __name__ == '__main__':
    app.run(port=5000)