from flask import Flask, request, render_template
import joblib
import pandas as pd


app = Flask(__name__, template_folder='app/templates')

# Cargar el modelo entrenado
with open('app/model/nba_predictor_model.pkl', 'rb') as f:
    model = joblib.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    home_team = request.form['home_team']
    away_team = request.form['away_team']

    # Crear un DataFrame con los datos de entrada
    input_df = pd.DataFrame([[home_team, away_team]], columns=['Home Team', 'Away Team'])

    try:
        # Realizar la predicción
        prediction = model.predict(input_df)[0]  # Predicción binaria: 0 o 1

        # Determinar el equipo ganador
        if prediction == 1:
            winner = home_team
        else:
            winner = away_team

        return render_template('index.html', prediction_result=f'🏀 Ganador predicho: {winner}')
    
    except Exception as e:
        return render_template('index.html', prediction_result=f'❌ Error en la predicción: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
