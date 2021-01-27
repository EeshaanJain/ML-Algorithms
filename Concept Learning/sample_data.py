import pandas as pd
# Let's create a sample dataframe
def get_sport_data():
    data_dict = {
                'Example' : [1, 2, 3, 4],
                'Sky' : ['Sunny', 'Sunny', 'Rainy', 'Sunny'],
                'AirTemp' : ['Warm', 'Warm', 'Cold', 'Warm'],
                'Humidity' : ['Normal', 'High', 'High', 'High'],
                'Wind' : ['Strong', 'Strong', 'Strong', 'Strong'],
                'Water' : ['Warm', 'Warm', 'Warm', 'Cool'],
                'Forecast' : ['Same', 'Same', 'Change', 'Change'],
                'EnjoySport' : ['Yes', 'Yes', 'No', 'Yes']
    }
    df = pd.DataFrame.from_dict(data_dict).set_index('Example')
    return df


def get_poison_data():
    data_dict = {
                'Example' : [1,2,3,4,5,6,7],
                'Color' : ['Green', 'Green', 'Brown', 'Orange', 'Green', 'Green', 'Orange'],
                'Toughness' : ['Hard', 'Hard', 'Soft', 'Hard', 'Soft', 'Hard', 'Hard'],
                'Fungus' : ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No'],
                'Appearance' : ['Wrinkled', 'Smooth', 'Wrinkled', 'Wrinkled', 'Smooth', 'Wrinkled', 'Wrinkled'],
                'Poisonous' : ['Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes']
    }
    df = pd.DataFrame.from_dict(data_dict).set_index('Example')
    return df
