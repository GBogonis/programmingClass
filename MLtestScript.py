import numpy as np
#from sklearn.preprocessing import Imputer
import pandas as pd
import tensorflow as tf
import keras
from keras.utils import FeatureSpace
'''
data1 = np.array([34.1, 32.2, 40.0, 31.8, 36.6, 45.9, 35.8, 35.2, 18.3, 25.9, 32.9, 53.0, 34.5, 42.7, 35.1, 37.2, 43.2, 48.2, 41.7, 47.9, 24.1, 39.3, 39.8]).reshape((-1,1))
data2 = np.array([34.1, 32.2, 40.0, 31.8, 36.6, 45.9, 35.8, 35.2, 18.3, 25.9, 32.9, 53.0, 34.5, 42.7, 35.1, 37.2, 43.2, 48.2, 41.7, 47.9, 24.1, 39.3, 37.8])

model = LinearRegression()
model.fit(data1,data2)
pred = model.predict(data1)
print(pred)
'''
file = open('weatherData2.txt','r')
dataFrame = pd.read_csv(file)
print(dataFrame.shape)

val_dataframe = dataFrame.sample(frac=0.2, random_state=1337)
train_dataframe = dataFrame.drop(val_dataframe.index)

print(
    "Using %d samples for training and %d for validation"
    % (len(train_dataframe), len(val_dataframe))
)

def dataframe_to_dataset(dataframe):
    dataframe = dataframe.copy()
    labels = dataframe.pop("target")
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
    ds = ds.shuffle(buffer_size=len(dataframe))
    return ds


train_ds = dataframe_to_dataset(train_dataframe)
val_ds = dataframe_to_dataset(val_dataframe)

for x, y in train_ds.take(8):
    print("Input:", x)
    print("Target:", y)
    
train_ds = train_ds.batch(32)
val_ds = val_ds.batch(32)

#month,target,sunshine,precipitation,windspeed,radiation

feature_space = FeatureSpace(
    features={
        # Categorical features encoded as integers
        "month": "integer_categorical",
        "sunshine": "integer_categorical",
        "precipitation": "float_normalized",
        "windspeed": "float_normalized",
        "radiation": "float_normalized",
    },
    output_mode="concat",)

train_ds_with_no_labels = train_ds.map(lambda x, _: x)
feature_space.adapt(train_ds_with_no_labels)

preprocessed_train_ds = train_ds.map(
    lambda x, y: (feature_space(x), y), num_parallel_calls=tf.data.AUTOTUNE
)
preprocessed_train_ds = preprocessed_train_ds.prefetch(tf.data.AUTOTUNE)

preprocessed_val_ds = val_ds.map(
    lambda x, y: (feature_space(x), y), num_parallel_calls=tf.data.AUTOTUNE
)
preprocessed_val_ds = preprocessed_val_ds.prefetch(tf.data.AUTOTUNE)

dict_inputs = feature_space.get_inputs()
encoded_features = feature_space.get_encoded_features()

x = keras.layers.Dense(32, activation="relu")(encoded_features)
x = keras.layers.Dropout(0.5)(x)
predictions = keras.layers.Dense(1, activation="sigmoid")(x)

training_model = keras.Model(inputs=encoded_features, outputs=predictions)
training_model.compile(
    optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
)

inference_model = keras.Model(inputs=dict_inputs, outputs=predictions)

training_model.fit(
    preprocessed_train_ds,
    epochs=30,
    validation_data=preprocessed_val_ds,
    verbose=2,
)

sample = {
    "month": 1,
    "sunshine": 24296.4,
    "precipitation": 0.0,
    "windspeed": 8.7,
    "radiation": 6.6,
}

input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
predictions = inference_model.predict(input_dict)

print(
    f"the perdicted temp would be{predictions[0][0]:.2f} degrees "
)