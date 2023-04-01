import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from django.http import JsonResponse

def train_model(request):
    # Using double backslashes
    car_dataset = pd.read_csv('C:\\Users\\Achyut\\Desktop\\joycar\\joycar-backend\\joycar\\car_price_prediction\\data\\car_data.csv')

    # Encode categorical variables
    car_dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)
    car_dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)
    car_dataset.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)

    # Split the dataset into training and testing sets
    X = car_dataset.drop(['Car_Name','Selling_Price'],axis=1)
    Y = car_dataset['Selling_Price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state=2)

    # Train a Linear Regression model on the training set
    lin_reg_model = LinearRegression()
    lin_reg_model.fit(X_train,Y_train)

    # Save the trained model to a .pkl file
    joblib.dump(lin_reg_model, "C:/Users/Achyut/Desktop/joycar/joycar-backend/joycar/car_price_prediction/models/model.pkl")

    # Return a response indicating that the model has been trained and saved
    return JsonResponse({'message': 'Model trained and saved successfully'})

import joblib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarPricePredictionSerializer
from .models import ai

class CarPricePrediction(APIView):
    def post(self, request):
        # Load the trained model from the .pkl file
        model = joblib.load(r'C:\Users\Achyut\Desktop\joycar\joycar-backend\joycar\car_price_prediction\models\model.pkl')

        # Validate the input data using the serializer
        serializer = CarPricePredictionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # Load the car data from the database
        cars = ai.objects.filter(car_name=validated_data['car_name'], year=validated_data['year'], kms_driven=validated_data['kms_driven'], fuel_type=validated_data['fuel_type'])
       
        if len(cars) == 0:
            return Response({'error': 'Car data not found'}, status=status.HTTP_404_NOT_FOUND)

        # Make a prediction using the trained model
        car_data = {'Year': validated_data['year'], 'Car_Name': validated_data['car_name'], 'Kms_Driven': validated_data['kms_driven'], 'Fuel_Type': validated_data['fuel_type']}
        car_data_encoded = pd.DataFrame(car_data, index=[0])
        car_data_encoded.replace({'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2}}, inplace=True)
        prediction = model.predict(car_data_encoded.drop(['Selling_Price'], axis=1))
        predicted_price = round(prediction[0], 2)

        return Response({'selling_price': predicted_price}, status=status.HTTP_200_OK)