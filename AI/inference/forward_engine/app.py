from inference_engliune import  decide_crop_engine


print("Cron Recommendation")
print("+++++++++++++++++++++++++++++++++++++++++++")
temperature = int(input("Enter average temperature(°C):"))
rainfall = int(input("Enter rainfall average (mm):"))
soil_type = input("Enter soil type (loamy, clay or sandy: ")


crop = decide_crop_engine(temperature, rainfall, soil_type)
print(crop)