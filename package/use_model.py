import pickle
import pandas as pd
from sklearn.calibration import LabelEncoder

def use_model(price, gpu_memory, processor_brand, ssd, ram, expandable_memory, screen_resolution,
              storage, battery_backup):

    refresh_rate = 60

    with open('package/models/model.pkl', 'rb') as file:
        loaded_data = pickle.load(file)

    loaded_model = loaded_data['model']
    X_train = loaded_data['X_train']
    y_train = loaded_data['y_train']

    new_data = pd.DataFrame({
        'price': [],
        'gpu_memory': [],
        'processor_brand': [],
        'ssd': [],
        'ram': [],
        'expandable_memory': [],
        'refresh_rate': [refresh_rate],
        'screen_resolution': [],
        'storage': [],
        'battery_backup': []
    })

    binary_cols = ['SSD', 'Expandable Memory']
    label_encoder = LabelEncoder()
    for col in binary_cols:
        new_data[col] = label_encoder.fit_transform(new_data[col])
    categorical_cols = ['Price (in Rupiah)', 'Dedicated Graphic Memory Capacity', 'Processor Brand', 'RAM (in GB)',
                        'Refresh Rate', 'screen_resolution', 'Storage', 'battery_backup']
    new_data = pd.get_dummies(new_data, columns=categorical_cols, drop_first=True)
    
    new_data = new_data.reindex(columns=X_train.columns, fill_value=0)

    predictions = loaded_model.predict(new_data)
    probabilities = loaded_model.predict_proba(new_data)

    return print(X_train)
