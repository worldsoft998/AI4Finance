#import  DeepNeuralNetworksStockPredictBbMain.*
from DeepNeuralNetworksStockPredictBbMain import DeepNeuralNetworksStockPriceForecasting
  
DeepNeuralNetworksStockPriceForecasting(
      portfolio=["TSLA", "AAPL", "NVDA", "NFLX"], #stocks whose prices you want to forecast 
      start_date = "2022-01-01", #starting date from there you want to take data to predict
      weights = [0.2, 0.3, 0.3, 0.2], #assign 20% to TSLA, 30% to AAPL etc (default to equal weight )
      prediction_days=30 #no of days for prediction
)